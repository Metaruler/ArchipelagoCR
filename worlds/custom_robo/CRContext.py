# Python imports
import copy
from typing import Dict
import asyncio

import NetUtils
# AP imports
from CommonClient import CommonContext, logger, logging

# 3rd party imports
import dolphin_memory_engine as dolphin

# Relative imports
from .CRClient import CRCommandProcessor
from .helpers import *
from .locations import BATTLE_TABLE, LOCATION_TABLE, BATTLE_COUNTER_ADDR, CHAPTER_COUNTER_ADDR, PROG_FLAG_1_ADDR, PROG_FLAG_2_ADDR, PROG_FLAG_3_ADDR, PROG_FLAG_4_ADDR
from .items import ALL_ITEMS_TABLE, PARTS_ITEM_TABLE, PROGRESSION_RAHU

from worlds.tww.TWWClient import read_string
from ..oot.Messages import bytes_to_int, int_to_bytes

WAIT_TIMER_SHORT_TIMEOUT: float = 0.125

# Unused memory in-game that will hold our item counters
LAST_RECV_ITEM_ADDR = 0x803BFB8E
NOT_SAVE_LAST_RECV_ITEM_ADDR = 0x803BFB92

GAME_STARTED_ADDR = 0x803BF933 # Location that changes to 116 whenever loaded into a file
DROP_TRIGGER_TOGGLE_ADDR = 0x803BFBEA # Location used to do memory clear logic (Bit 2)
RAHU_INDEX_ADDR = 0x803BFBEA # Stores at bit locations 3-6

CHAPTER_INDEX_ADDR = 0x803BE7A7
CAI_2_7 = 0x803BFBA3 # Chapter accesses for Ch 2-7
CAI_8_12 = 0x803BFBAB # Chapter accesses for Ch 8-12

CH2_CMP = 0b00000100
CH3_CMP = 0b00001000
CH4_CMP = 0b00010000
CH5_CMP = 0b00100000
CH6_CMP = 0b01000000
CH7_CMP = 0b10000000
CH8_CMP = 0b00000100
CH9_CMP = 0b00001000
CH10_CMP = 0b00010000
CH11_CMP = 0b00100000
CH12_CMP = 0b01000000

FLAG_DELAY_FRAMES = 60

#--------------------------------------------------------------------
#Context for CR
class CRContext(CommonContext):
    """
    This is the context class for the Custom Robo client. 
    This will inherit from the core class "CommonContext" in AP.
    This will hold all the game information, state, and functionality to run the client.
    """
    command_processor = CRCommandProcessor
    game = "Custom Robo"
    items_handling = 0b111
    dolphin_connected: bool = False
    seed_verified: bool = False
    already_fired_events = False
    game_running = False
    parts_not_suppressed = True
    chapters_loaded = False
    chapter_order = []
    stored_chapter = -1 # This will prevent us from constantly flipping new chapter flags
    flag_delay_counter = 0 # This counter will give the game enough time to flip the chapter before adjusting flags
    flag_flip = False

    item_id_to_name: Dict[int, str]
    slot_to_player_name: Dict[int, str]

    dolphin_server_task = None
    dolphin_status = None

    logger = logging.getLogger(CLIENT_NAME)

    def __init__(self, server_address, password):
        """
        Initialize the Custom Robo Context
        :param server_address: Address of AP Server.
        :param password: Password for the Server.
        """
        super().__init__(server_address, password)
        self.dolphin_status = CONNECTION_INITIAL_STATUS
        self.arg_seed = ""

        self.last_received_idx: int = 0
        self.non_save_last_recv_idx: int = 0


    def run_gui(self):
        """Import kivy UI system from make_gui() and start running it as self.ui_task"""
        ui_class = self.make_gui()
        ui_class.base_title = CLIENT_NAME
        self.ui = ui_class(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def on_package(self, cmd: str , args: dict): 
        """
        Handles incoming network packages from the server
        """
        super().on_package(cmd, args)
        slot_data = args.get("slot_data", {})

        match cmd:
            case "Connected":
                self.arg_seed = "CR" + str(slot_data["seed"])
                self.game_running = True

    async def disconnect(self, allow_autoreconnect = False):
        await super().disconnect(allow_autoreconnect)
    
        dolphin.un_hook()
        self.checked_locations = set()
        self.seed_verified = False
        self.dolphin_connected = False
        self.already_fired_events = False

    async def write_bytes_and_validate(self, addr: int, ram_offset: list[str] | None, curr_value: bytes) -> None:
        if not ram_offset:
            dolphin.write_bytes(addr, curr_value)
        else:
            dolphin.write_bytes(dolphin.follow_pointers(addr, ram_offset), curr_value)

    def update_received_index(self, last_recov_idx: int):
        """
        This will write the current item index to saveable and non-saveable RAM address using 4 byte write
        to overall prevent player from getting EVERY check every time they log in.
        """
        self.last_received_idx = last_recov_idx

        byte_data = last_recov_idx.to_bytes(4, 'big')

        try:
            dolphin.write_bytes(LAST_RECV_ITEM_ADDR, byte_data)
        except Exception as e:
            logger.info(f"Error writing 4-byte index to LAST RECOV ITEM ADDR: {e}")

        if last_recov_idx > self.non_save_last_recv_idx:
            self.non_save_last_recv_idx = last_recov_idx
            try:
                dolphin.write_bytes(NOT_SAVE_LAST_RECV_ITEM_ADDR, byte_data)
            except Exception as e:
                logger.info(f"Error writing 4-byte index to NOT SAVE LAST RECOV ITEM")


    async def game_watcher(self):
        """
        This is the main loop that will handle checking locations and giving items.
        It will run as long as the client is connected to the server.
        """

        #logger.info("Entering game watcher loop")


        #Lazy implementation to prevent natural part drops from the game
        #if self.parts_not_suppressed:
        if bytes_to_int(dolphin.read_bytes(0x803BF9D7, 1)) != 0xFF:
            dolphin.write_bytes(0x803BF9D7, int_to_bytes(0xFF, 1))
            #self.parts_not_suppressed = False

        # Load Chapters into array for logic
        if not self.chapters_loaded:
            # Chapters are read from patched locations
            chaps = [
                bytes_to_int(dolphin.read_bytes(0x80000017, 1)),
                bytes_to_int(dolphin.read_bytes(0x80000018, 1)),
                bytes_to_int(dolphin.read_bytes(0x80000019, 1)),
                bytes_to_int(dolphin.read_bytes(0x8000001A, 1)),
                bytes_to_int(dolphin.read_bytes(0x8000001B, 1))
            ]
            for chap in chaps:
                self.chapter_order.append(chap >> 4)
                self.chapter_order.append(chap % 16)
            self.chapter_order.append(12)
            self.chapters_loaded = True


        # Reset Chapter battles for proper counting (MUST BE DONE AFTER CHAPTER ALTERATION)
        current_chapter = bytes_to_int(dolphin.read_bytes(CHAPTER_COUNTER_ADDR, 1))

        # Chapter advance logic to control the counter for flipping flags
        chap_advance = self.stored_chapter + 1 == current_chapter
        if chap_advance:
            self.flag_delay_counter += 1
            if self.flag_delay_counter > FLAG_DELAY_FRAMES:
                self.flag_flip = True
                self.flag_delay_counter = 0

        battle_wins = bytes_to_int(dolphin.read_bytes(BATTLE_COUNTER_ADDR, 1))
        local_missing_locations = copy.deepcopy(self.missing_locations)
        for missing_locations in local_missing_locations:
            local_location_name = self.location_names.lookup_in_game(missing_locations)
            cr_local_data = LOCATION_TABLE[local_location_name]
            match cr_local_data.type:
                case "Part Use":
                    # Check if part has been used
                    location_value = bytes_to_int(dolphin.read_bytes(cr_local_data.ram_addr.ram_addr, 1))
                    location_value_flag = (location_value & (1 << cr_local_data.ram_addr.bit_position)) > 0
                    # Check if part has been obtained
                    obtained_part_name = ALL_ITEMS_TABLE.get(local_location_name[4:])
                    obtained_part_addr = obtained_part_name.update_ram_addr[0]
                    obtained_part_value = bytes_to_int(dolphin.read_bytes(obtained_part_addr.ram_addr, 1))
                    obtained_part_flag = (obtained_part_value & (1 << obtained_part_addr.bit_position)) > 0
                    if (not location_value_flag) & obtained_part_flag:
                        #logger.info(f"Location Value: {location_value} and Obtained Part Address: {obtained_part_addr}")
                        #logger.info(f"Ram Location accessed: {obtained_part.ram_addr} at Bit Location: {obtained_part.bit_position}")
                        #logger.info(str(dolphin.read_bytes(obtained_part.ram_addr, 8)))
                        self.locations_checked.add(missing_locations)
                case "Battle Win":
                    # Check if we've defeated the opponent yet
                    if cr_local_data.parent_ch == self.stored_chapter and cr_local_data.battle_number <= battle_wins:
                        self.locations_checked.add(missing_locations)



        await self.check_locations(self.locations_checked)
        # Locations Checked is LOCAL locations in game
        # Checked Locations is AP SERVER STATE of locations

        #logger.info("Locations checked, checking for endgame")

        if not self.finished_game:
            try:
                # Get the RAM data for the final scene in the New Journey scenario. This is our "beating the game".
                # Read the value at the event's memory address.
                boss_defeated_value = dolphin.read_bytes(CHAPTER_INDEX_ADDR, 1)[0]

                # Check if the bit for defeating Rahu is set.
                if boss_defeated_value == 18:
                    rahu_item_name = "Defeated Rahu III"
                    rahu_item_info = ALL_ITEMS_TABLE.get(rahu_item_name)

                    # Ensure item data exists
                    if rahu_item_info and rahu_item_info.update_ram_addr and len(rahu_item_info.update_ram_addr) > 0:
                        addr_to_update = rahu_item_info.update_ram_addr[0]
                        ram_addr = addr_to_update.ram_addr
                        bit_position = addr_to_update.bit_position
                        byte_size = 1

                        # Read current value
                        curr_val = int.from_bytes(dolphin.read_bytes(ram_addr, byte_size), 'big')

                        # Apply the item's bit-set effect
                        new_val = (curr_val | (1 << bit_position))

                        # Write the new value back to RAM
                        await self.write_bytes_and_validate(
                            ram_addr, None, new_val.to_bytes(byte_size, 'big')
                        )
                    else:
                        logger.error("Rahu defeat item data not found or misconfigured, cannot grant item for goal.")

                    # Display victory on the log then send victory ping to multiworld server
                    print("Final boss defeated! Signaling game completion to the server.")
                    self.finished_game = True # Ends loop on next pass
                    await self.send_msgs([{
                        "cmd": "StatusUpdate",
                        "status": NetUtils.ClientStatus.CLIENT_GOAL,
                    }])
            except Exception as e:
                # This will catch errors if the game state is not readable or the address is invalid.
                print(f"Error checking for game completion: {e}")

            #logger.info("Endgame checked, checking for items")

            if bytes_to_int(dolphin.read_bytes(GAME_STARTED_ADDR, 1)) > 0:
                # On first start, wipe part memory before receiving starter items
                if not (bytes_to_int(dolphin.read_bytes(DROP_TRIGGER_TOGGLE_ADDR, 1)) & (1 << 1)):
                    # Clear all initial part flags before processing items
                    mem_zeroes = int_to_bytes(0x00,1)
                    dolphin.write_bytes(0x803BFB9F, mem_zeroes)
                    dolphin.write_bytes(0x803BFBBF, mem_zeroes)
                    dolphin.write_bytes(0x803BFBDF, mem_zeroes)
                    dolphin.write_bytes(0x803BFBFF, mem_zeroes)
                    dolphin.write_bytes(0x803BFC1F, mem_zeroes)
                    dolphin.write_bytes(0x803BFBA7, mem_zeroes)
                    dolphin.write_bytes(0x803BFBC7, mem_zeroes)
                    dolphin.write_bytes(0x803BFBE7, mem_zeroes)
                    dolphin.write_bytes(0x803BFC07, mem_zeroes)
                    dolphin.write_bytes(0x803BFC27, mem_zeroes)
                    toggle_int = bytes_to_int(dolphin.read_bytes(DROP_TRIGGER_TOGGLE_ADDR, 1))
                    item_mesh = int_to_bytes(toggle_int | (1 << 1), 1)
                    dolphin.write_bytes(DROP_TRIGGER_TOGGLE_ADDR, item_mesh)

                # Chapter & Flag adjustment logic (also controls access to Chapters)
                not_yet_set = bytes_to_int(dolphin.read_bytes(PROG_FLAG_4_ADDR, 1)) == 0
                match current_chapter:
                    case 0:
                        if not_yet_set and self.stored_chapter == -1:
                            dolphin.write_bytes(PROG_FLAG_1_ADDR, int_to_bytes(0x07, 1))
                            dolphin.write_bytes(PROG_FLAG_2_ADDR, int_to_bytes(0xF8, 1))
                            dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0x08, 1))
                            self.stored_chapter = current_chapter
                        # Reset battles before moving to Ch 1
                        if bytes_to_int(dolphin.read_bytes(PROG_FLAG_1_ADDR, 1)) & 0x08 > 0:
                            dolphin.write_bytes(BATTLE_COUNTER_ADDR, int_to_bytes(0x00, 1))
                    case 1:
                        if not_yet_set and self.flag_flip:
                            dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0x04, 1))
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                        if self.flag_delay_counter == 0 and bytes_to_int(dolphin.read_bytes(PROG_FLAG_3_ADDR, 1)) & 0x08 > 0:
                            chap_count = 0
                            while self.chapter_order[chap_count] != current_chapter:
                                chap_count += 1
                            next_chap = self.chapter_order[chap_count+1]
                            ob_mem = False # Obtained Memory?
                            # Check if next chapter is unlocked, otherwise it's GROUNDHOG DAY
                            match next_chap:
                                case 1: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7,1)) & CH2_CMP > 0
                                case 2: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH3_CMP > 0
                                case 3: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH4_CMP > 0
                                case 5: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH5_CMP > 0
                                case 7: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH6_CMP > 0
                                case 8: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH7_CMP > 0
                                case 9: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH8_CMP > 0
                                case 10: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH9_CMP > 0
                                case 11: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH10_CMP > 0
                                case 13: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH11_CMP > 0
                                case 14: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH12_CMP > 0
                            if ob_mem: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(next_chap-1, 1))
                            else: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(current_chapter-1, 1))
                            #dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0xFF, 1)) # Prevents error in flag settings
                            dolphin.write_bytes(BATTLE_COUNTER_ADDR, int_to_bytes(0x00, 1))
                            self.stored_chapter = next_chap-1
                    case 2:
                        if not_yet_set and self.flag_flip:
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                        if self.flag_delay_counter == 0 and bytes_to_int(dolphin.read_bytes(PROG_FLAG_4_ADDR, 1)) & 0x20 > 0:
                            chap_count = 0
                            while self.chapter_order[chap_count] != current_chapter:
                                chap_count += 1
                            next_chap = self.chapter_order[chap_count+1]
                            ob_mem = False # Obtained Memory?
                            # Check if next chapter is unlocked, otherwise it's GROUNDHOG DAY
                            match next_chap:
                                case 1: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7,1)) & CH2_CMP > 0
                                case 2: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH3_CMP > 0
                                case 3: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH4_CMP > 0
                                case 5: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH5_CMP > 0
                                case 7: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH6_CMP > 0
                                case 8: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH7_CMP > 0
                                case 9: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH8_CMP > 0
                                case 10: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH9_CMP > 0
                                case 11: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH10_CMP > 0
                                case 13: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH11_CMP > 0
                                case 14: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH12_CMP > 0
                            if ob_mem: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(next_chap-1, 1))
                            else: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(current_chapter-1, 1))
                            #dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0xFF, 1)) # Prevents error in flag settings
                            dolphin.write_bytes(BATTLE_COUNTER_ADDR, int_to_bytes(0x00, 1))
                            self.stored_chapter = next_chap-1
                    case 3:
                        if not_yet_set and self.flag_flip:
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                    case 4:
                        if not_yet_set and self.flag_flip:
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                        if self.flag_delay_counter == 0 and bytes_to_int(dolphin.read_bytes(PROG_FLAG_4_ADDR, 1)) & 0x01 > 0:
                            chap_count = 0
                            while self.chapter_order[chap_count] != current_chapter:
                                chap_count += 1
                            next_chap = self.chapter_order[chap_count+1]
                            ob_mem = False # Obtained Memory?
                            # Check if next chapter is unlocked, otherwise it's GROUNDHOG DAY
                            match next_chap:
                                case 1: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7,1)) & CH2_CMP > 0
                                case 2: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH3_CMP > 0
                                case 3: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH4_CMP > 0
                                case 5: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH5_CMP > 0
                                case 7: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH6_CMP > 0
                                case 8: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH7_CMP > 0
                                case 9: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH8_CMP > 0
                                case 10: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH9_CMP > 0
                                case 11: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH10_CMP > 0
                                case 13: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH11_CMP > 0
                                case 14: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH12_CMP > 0
                            if ob_mem: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(next_chap-1, 1))
                            else: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(current_chapter-1, 1))
                            #dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0xFF, 1)) # Prevents error in flag settings
                            dolphin.write_bytes(BATTLE_COUNTER_ADDR, int_to_bytes(0x00, 1))
                            self.stored_chapter = next_chap-1
                    case 5:
                        if not_yet_set and self.flag_flip:
                            dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0xE0, 1))
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                    case 6:
                        if not_yet_set and self.flag_flip:
                            dolphin.write_bytes(PROG_FLAG_3_ADDR, int_to_bytes(0x08, 1))
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                        if self.flag_delay_counter == 0 and bytes_to_int(dolphin.read_bytes(PROG_FLAG_4_ADDR, 1)) & 0x08 > 0:
                            chap_count = 0
                            while self.chapter_order[chap_count] != current_chapter:
                                chap_count += 1
                            next_chap = self.chapter_order[chap_count+1]
                            ob_mem = False # Obtained Memory?
                            # Check if next chapter is unlocked, otherwise it's GROUNDHOG DAY
                            match next_chap:
                                case 1: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7,1)) & CH2_CMP > 0
                                case 2: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH3_CMP > 0
                                case 3: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH4_CMP > 0
                                case 5: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH5_CMP > 0
                                case 7: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH6_CMP > 0
                                case 8: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH7_CMP > 0
                                case 9: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH8_CMP > 0
                                case 10: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH9_CMP > 0
                                case 11: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH10_CMP > 0
                                case 13: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH11_CMP > 0
                                case 14: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH12_CMP > 0
                            if ob_mem: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(next_chap-1, 1))
                            else: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(current_chapter-1, 1))
                            #dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0xFF, 1)) # Prevents error in flag settings
                            dolphin.write_bytes(BATTLE_COUNTER_ADDR, int_to_bytes(0x00, 1))
                            self.stored_chapter = next_chap-1
                    case 7:
                        if not_yet_set and self.flag_flip:
                            dolphin.write_bytes(PROG_FLAG_2_ADDR, int_to_bytes(0x01, 1))
                            dolphin.write_bytes(PROG_FLAG_3_ADDR, int_to_bytes(0xFF, 1))
                            dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0xE1, 1))
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                        if self.flag_delay_counter == 0 and bytes_to_int(dolphin.read_bytes(PROG_FLAG_3_ADDR, 1)) & 0x10 > 0:
                            chap_count = 0
                            while self.chapter_order[chap_count] != current_chapter:
                                chap_count += 1
                            next_chap = self.chapter_order[chap_count+1]
                            ob_mem = False # Obtained Memory?
                            # Check if next chapter is unlocked, otherwise it's GROUNDHOG DAY
                            match next_chap:
                                case 1: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7,1)) & CH2_CMP > 0
                                case 2: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH3_CMP > 0
                                case 3: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH4_CMP > 0
                                case 5: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH5_CMP > 0
                                case 7: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH6_CMP > 0
                                case 8: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH7_CMP > 0
                                case 9: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH8_CMP > 0
                                case 10: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH9_CMP > 0
                                case 11: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH10_CMP > 0
                                case 13: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH11_CMP > 0
                                case 14: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH12_CMP > 0
                            if ob_mem: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(next_chap-1, 1))
                            else: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(current_chapter-1, 1))
                            #dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0xFF, 1)) # Prevents error in flag settings
                            dolphin.write_bytes(BATTLE_COUNTER_ADDR, int_to_bytes(0x00, 1))
                            self.stored_chapter = next_chap-1
                    case 8:
                        if not_yet_set and self.flag_flip:
                            dolphin.write_bytes(PROG_FLAG_1_ADDR, int_to_bytes(0x7F, 1))
                            dolphin.write_bytes(PROG_FLAG_2_ADDR, int_to_bytes(0xFC, 1))
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                        if self.flag_delay_counter == 0 and bytes_to_int(dolphin.read_bytes(PROG_FLAG_2_ADDR, 1)) & 0x01 > 0:
                            chap_count = 0
                            while self.chapter_order[chap_count] != current_chapter:
                                chap_count += 1
                            next_chap = self.chapter_order[chap_count+1]
                            ob_mem = False # Obtained Memory?
                            # Check if next chapter is unlocked, otherwise it's GROUNDHOG DAY
                            match next_chap:
                                case 1: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7,1)) & CH2_CMP > 0
                                case 2: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH3_CMP > 0
                                case 3: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH4_CMP > 0
                                case 5: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH5_CMP > 0
                                case 7: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH6_CMP > 0
                                case 8: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH7_CMP > 0
                                case 9: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH8_CMP > 0
                                case 10: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH9_CMP > 0
                                case 11: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH10_CMP > 0
                                case 13: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH11_CMP > 0
                                case 14: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH12_CMP > 0
                            if ob_mem: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(next_chap-1, 1))
                            else: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(current_chapter-1, 1))
                            #dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0xFF, 1)) # Prevents error in flag settings
                            dolphin.write_bytes(BATTLE_COUNTER_ADDR, int_to_bytes(0x00, 1))
                            self.stored_chapter = next_chap-1
                    case 9:
                        if not_yet_set and self.flag_flip:
                            dolphin.write_bytes(PROG_FLAG_3_ADDR, int_to_bytes(0x20, 1))
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                        if self.flag_delay_counter == 0 and bytes_to_int(dolphin.read_bytes(PROG_FLAG_3_ADDR, 1)) & 0x02 > 0:
                            chap_count = 0
                            while self.chapter_order[chap_count] != current_chapter:
                                chap_count += 1
                            next_chap = self.chapter_order[chap_count+1]
                            ob_mem = False # Obtained Memory?
                            # Check if next chapter is unlocked, otherwise it's GROUNDHOG DAY
                            match next_chap:
                                case 1: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7,1)) & CH2_CMP > 0
                                case 2: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH3_CMP > 0
                                case 3: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH4_CMP > 0
                                case 5: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH5_CMP > 0
                                case 7: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH6_CMP > 0
                                case 8: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH7_CMP > 0
                                case 9: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH8_CMP > 0
                                case 10: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH9_CMP > 0
                                case 11: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH10_CMP > 0
                                case 13: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH11_CMP > 0
                                case 14: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH12_CMP > 0
                            if ob_mem: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(next_chap-1, 1))
                            else: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(current_chapter-1, 1))
                            #dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0xFF, 1)) # Prevents error in flag settings
                            dolphin.write_bytes(BATTLE_COUNTER_ADDR, int_to_bytes(0x00, 1))
                            self.stored_chapter = next_chap-1
                    case 10:
                        if not_yet_set and self.flag_flip:
                            dolphin.write_bytes(PROG_FLAG_2_ADDR, int_to_bytes(0x0F, 1))
                            dolphin.write_bytes(PROG_FLAG_3_ADDR, int_to_bytes(0xFF, 1))
                            dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0xEE, 1))
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                        if self.flag_delay_counter == 0 and bytes_to_int(dolphin.read_bytes(PROG_FLAG_1_ADDR, 1)) & 0x20 > 0:
                            chap_count = 0
                            while self.chapter_order[chap_count] != current_chapter:
                                chap_count += 1
                            next_chap = self.chapter_order[chap_count+1]
                            ob_mem = False # Obtained Memory?
                            # Check if next chapter is unlocked, otherwise it's GROUNDHOG DAY
                            match next_chap:
                                case 1: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7,1)) & CH2_CMP > 0
                                case 2: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH3_CMP > 0
                                case 3: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH4_CMP > 0
                                case 5: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH5_CMP > 0
                                case 7: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH6_CMP > 0
                                case 8: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH7_CMP > 0
                                case 9: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH8_CMP > 0
                                case 10: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH9_CMP > 0
                                case 11: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH10_CMP > 0
                                case 13: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH11_CMP > 0
                                case 14: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH12_CMP > 0
                            if ob_mem: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(next_chap-1, 1))
                            else: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(current_chapter-1, 1))
                            #dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0xFF, 1)) # Prevents error in flag settings
                            dolphin.write_bytes(BATTLE_COUNTER_ADDR, int_to_bytes(0x00, 1))
                            self.stored_chapter = next_chap-1
                    case 11:
                        if not_yet_set and self.flag_flip:
                            dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0x20, 1))
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                    case 12:
                        if not_yet_set and self.flag_flip:
                            dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0x04, 1))
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                        if self.flag_delay_counter == 0 and bytes_to_int(dolphin.read_bytes(PROG_FLAG_2_ADDR, 1)) & 0x01 > 0:
                            chap_count = 0
                            while self.chapter_order[chap_count] != current_chapter:
                                chap_count += 1
                            next_chap = self.chapter_order[chap_count+1]
                            ob_mem = False # Obtained Memory?
                            # Check if next chapter is unlocked, otherwise it's GROUNDHOG DAY
                            match next_chap:
                                case 1: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7,1)) & CH2_CMP > 0
                                case 2: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH3_CMP > 0
                                case 3: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH4_CMP > 0
                                case 5: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH5_CMP > 0
                                case 7: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH6_CMP > 0
                                case 8: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH7_CMP > 0
                                case 9: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH8_CMP > 0
                                case 10: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH9_CMP > 0
                                case 11: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH10_CMP > 0
                                case 13: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH11_CMP > 0
                                case 14: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH12_CMP > 0
                            if ob_mem: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(next_chap-1, 1))
                            else: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(current_chapter-1, 1))
                            #dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0xFF, 1)) # Prevents error in flag settings
                            dolphin.write_bytes(BATTLE_COUNTER_ADDR, int_to_bytes(0x00, 1))
                            self.stored_chapter = next_chap-1
                    case 13:
                        if not_yet_set and self.flag_flip:
                            dolphin.write_bytes(PROG_FLAG_2_ADDR, int_to_bytes(0x04, 1))
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                        if self.flag_delay_counter == 0 and bytes_to_int(dolphin.read_bytes(PROG_FLAG_3_ADDR, 1)) & 0x80 > 0:
                            chap_count = 0
                            while self.chapter_order[chap_count] != current_chapter:
                                chap_count += 1
                            next_chap = self.chapter_order[chap_count+1]
                            ob_mem = False # Obtained Memory?
                            # Check if next chapter is unlocked, otherwise it's GROUNDHOG DAY
                            match next_chap:
                                case 1: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7,1)) & CH2_CMP > 0
                                case 2: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH3_CMP > 0
                                case 3: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH4_CMP > 0
                                case 5: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH5_CMP > 0
                                case 7: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH6_CMP > 0
                                case 8: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_2_7, 1)) & CH7_CMP > 0
                                case 9: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH8_CMP > 0
                                case 10: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH9_CMP > 0
                                case 11: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH10_CMP > 0
                                case 13: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH11_CMP > 0
                                case 14: ob_mem = bytes_to_int(dolphin.read_bytes(CAI_8_12, 1)) & CH12_CMP > 0
                            if ob_mem: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(next_chap-1, 1))
                            else: dolphin.write_bytes(CHAPTER_INDEX_ADDR, int_to_bytes(current_chapter-1, 1))
                            #dolphin.write_bytes(PROG_FLAG_4_ADDR, int_to_bytes(0xFF, 1)) # Prevents error in flag settings
                            dolphin.write_bytes(BATTLE_COUNTER_ADDR, int_to_bytes(0x00, 1))
                            self.stored_chapter = next_chap-1
                    case 14:
                        if not_yet_set and self.flag_flip:
                            dolphin.write_bytes(PROG_FLAG_2_ADDR, int_to_bytes(0x04, 1))
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                    case 15:
                        if not_yet_set and self.flag_flip:
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                    case 16:
                        if not_yet_set and self.flag_flip:
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                    case 17:
                        if not_yet_set and self.flag_flip:
                            self.stored_chapter = current_chapter
                            self.flag_flip = False
                    case 18:
                        if not_yet_set and self.flag_flip:
                            self.stored_chapter = current_chapter
                            self.flag_flip = False

                    # Check for new items.
                try:
                    ram_bytes = dolphin.read_bytes(LAST_RECV_ITEM_ADDR, 4)
                    last_recv_idx = int.from_bytes(ram_bytes, "big")
                except Exception as e:
                    logger.warning(f"Failed to read saveable index from RAM: {e}")
                    last_recv_idx = 0

                # If true, we have no items to account for
                if len(self.items_received) == last_recv_idx:
                    return

                # Otherwise, allocate items since last save
                self.last_received_idx = last_recv_idx
                try:
                    non_save_bytes = dolphin.read_bytes(NOT_SAVE_LAST_RECV_ITEM_ADDR, 4)
                    self.non_save_last_recv_idx = int.from_bytes(non_save_bytes, "big")
                except Exception as e:
                    logger.warning(f"Failed to read non-saveable index from RAM: {e}")
                    self.non_save_last_recv_idx = 0

                # Get only new items since last save
                recv_items = self.items_received[last_recv_idx:]

                # Process each new item
                for item_to_add in recv_items:
                    last_recv_idx += 1

                    item_name = self.item_names.lookup_in_game(item_to_add.item)
                    item_info = ALL_ITEMS_TABLE.get(item_name)
                    #logger.print(item_info)
                    # Sort as parts or not
                    #item_type = item_info.type
                    #player_name = self.slot_to_player_name[item_to_add.player]
                    #print(f"Received item: {item_name} from {player_name}.")
                    #logger.info("Received new item, updating memory")
                    if item_info:
                        item_type = item_info.type
                        if item_type == "Body" or item_type == "Gun" or item_type == "Bomb" or item_type == "Pod" or item_type == "Legs":
                            location_edit = "Use " + item_name
                            # Write location BEFORE item gain to enable the check
                            # logger.print("Writing to drop location in memory...")
                            usage_loc = LOCATION_TABLE[location_edit].ram_addr.ram_addr
                            usage_byte = bytes_to_int(dolphin.read_bytes(usage_loc, 1))
                            usage_flag = LOCATION_TABLE[location_edit].ram_addr.bit_position
                            usage_mesh = int_to_bytes(usage_byte | (1 << usage_flag), 1)
                            # Calculate matching item gain and assign simultaneously
                            item_loc = item_info.update_ram_addr[0].ram_addr
                            item_byte = bytes_to_int(dolphin.read_bytes(item_loc, 1))
                            item_flag = item_info.update_ram_addr[0].bit_position
                            item_mesh = int_to_bytes(item_byte | (1 << item_flag), 1)
                            # Write to memory
                            dolphin.write_bytes(usage_loc, usage_mesh)
                            dolphin.write_bytes(item_loc, item_mesh)
                        elif item_type == "Progressive Rahu":
                            # Rahu Evolution item code = 194
                            # rahu_count: int = len([netItem for netItem in self.items_received if netItem.item == 194])
                            rahu_origin = bytes_to_int(dolphin.read_bytes(RAHU_INDEX_ADDR, 1))
                            rahu_moder = rahu_origin
                            rahu_count = (rahu_moder >> 2)
                            # Prevent out-of-bounds issue when receiving more than the max Rahu parts
                            if rahu_count < 11:
                                rahu_piece = PROGRESSION_RAHU.get("Rahu Evolution Steps")[rahu_count]
                                location_edit = "Use " + rahu_piece.name
                                # We actually hold the counter for Rahu right next to Grand Cross Bomb's usage flag, so
                                # the below adjustment is to prevent the game from just instantly giving us the Use check
                                if rahu_piece.name == "Grand Cross Bomb":
                                    rahu_origin += 1
                                # Write location BEFORE item gain to enable the check
                                # logger.print("Writing to drop location in memory...")
                                usage_loc = LOCATION_TABLE[location_edit].ram_addr.ram_addr
                                usage_byte = bytes_to_int(dolphin.read_bytes(usage_loc, 1))
                                usage_flag = LOCATION_TABLE[location_edit].ram_addr.bit_position
                                usage_mesh = int_to_bytes(usage_byte | (1 << usage_flag), 1)
                                # Calculate matching item gain and assign simultaneously
                                item_loc = rahu_piece.update_ram_addr[0].ram_addr
                                item_byte = bytes_to_int(dolphin.read_bytes(item_loc, 1))
                                item_flag = rahu_piece.update_ram_addr[0].bit_position
                                item_mesh = int_to_bytes(item_byte | (1 << item_flag), 1)
                                # Write to memory
                                dolphin.write_bytes(usage_loc, usage_mesh)
                                dolphin.write_bytes(item_loc, item_mesh)
                                rahu_count += 1
                                rahu_index = int_to_bytes(((rahu_count << 2) + (rahu_origin & 0b00000011)), 1)
                                dolphin.write_bytes(RAHU_INDEX_ADDR, rahu_index)
                        elif item_type == "Chapter Access":
                            # Turn on bits in the part flags to indicate we have access to chapters
                            match item_name:
                                case "Chapter 2 Memories":
                                    dolphin.write_bytes(CAI_2_7, (int_to_bytes((bytes_to_int(dolphin.read_bytes(
                                        CAI_2_7, 1)) | CH2_CMP), 1)))
                                case "Chapter 3 Memories":
                                    dolphin.write_bytes(CAI_2_7, (int_to_bytes((bytes_to_int(dolphin.read_bytes(
                                        CAI_2_7, 1)) | CH3_CMP), 1)))
                                case "Chapter 4 Memories":
                                    dolphin.write_bytes(CAI_2_7, (int_to_bytes((bytes_to_int(dolphin.read_bytes(
                                        CAI_2_7, 1)) | CH4_CMP), 1)))
                                case "Chapter 5 Memories":
                                    dolphin.write_bytes(CAI_2_7, (int_to_bytes((bytes_to_int(dolphin.read_bytes(
                                        CAI_2_7, 1)) | CH5_CMP), 1)))
                                case "Chapter 6 Memories":
                                    dolphin.write_bytes(CAI_2_7, (int_to_bytes((bytes_to_int(dolphin.read_bytes(
                                        CAI_2_7, 1)) | CH6_CMP), 1)))
                                case "Chapter 7 Memories":
                                    dolphin.write_bytes(CAI_2_7, (int_to_bytes((bytes_to_int(dolphin.read_bytes(
                                        CAI_2_7, 1)) | CH7_CMP), 1)))
                                case "Chapter 8 Memories":
                                    dolphin.write_bytes(CAI_8_12, (int_to_bytes((bytes_to_int(dolphin.read_bytes(
                                        CAI_8_12, 1)) | CH8_CMP), 1)))
                                case "Chapter 9 Memories":
                                    dolphin.write_bytes(CAI_8_12, (int_to_bytes((bytes_to_int(dolphin.read_bytes(
                                        CAI_8_12, 1)) | CH9_CMP), 1)))
                                case "Chapter 10 Memories":
                                    dolphin.write_bytes(CAI_8_12, (int_to_bytes((bytes_to_int(dolphin.read_bytes(
                                        CAI_8_12, 1)) | CH10_CMP), 1)))
                                case "Chapter 11 Memories":
                                    dolphin.write_bytes(CAI_8_12, (int_to_bytes((bytes_to_int(dolphin.read_bytes(
                                        CAI_8_12, 1)) | CH11_CMP), 1)))
                                case "Dad's Watch":
                                    dolphin.write_bytes(CAI_8_12, (int_to_bytes((bytes_to_int(dolphin.read_bytes(
                                        CAI_8_12, 1)) | CH12_CMP), 1)))
                    else:
                        print(f"Error: Could not find type information for item ID {item_to_add.item}.")

                    self.update_received_index(last_recv_idx)
                    continue
                self.update_received_index(last_recv_idx)


    async def server_auth(self, password_requested: bool = False):
        """
        Authenticate with the Archipelago server.

        :param password_requested: Whether the server requires a password. Defaults to `False`.
        """
        if password_requested and not self.password:
            await super(CRContext, self).server_auth(password_requested)
        if self.dolphin_status != CONNECTION_VERIFY_SERVER:
            return
        if not self.auth:
            await self.get_username()
        await self.send_connect()

        if self.slot:
            logger.info(CONNECTION_CONNECTED_STATUS)
            self.dolphin_status = CONNECTION_CONNECTED_STATUS

    # Starts the full loop and debug messages for connecting to Dolphin.
    async def dolphin_connect_loop(self):
        """
        Connects to the Dolphin emulator and waits for the correct game to be running.
        """
        logger.info("Entering Dolphin Connection loop")
        while not self.exit_event.is_set():
            try:
                if not dolphin.is_hooked():
                    dolphin.hook()
                    if dolphin.get_status() == dolphin.get_status().noEmu or dolphin.get_status() == dolphin.get_status().notRunning:
                        dolphin.un_hook()
                        self.dolphin_status = CONNECTION_INITIAL_STATUS
                        logger.info(self.dolphin_status)
                        await wait_for_next_loop(5)
                        continue

                if not self.dolphin_status == CONNECTION_CONNECTED_STATUS:
                    game_id = read_string(0x80000000, 6)
                    # ID has not been modified, thus is a Vanilla ROM and should be Disconnected
                    if game_id in ["GXCE01"]:
                        logger.info(CONNECTION_REFUSED_STATUS)
                        self.dolphin_status = CONNECTION_REFUSED_STATUS
                        dolphin.un_hook()
                        await wait_for_next_loop(5)
                        continue

                    # Implement this eventually, would be nice
                    #if not self.auth:
                    #    self.auth = read_string(SLOT_NAME_ADDR, SLOT_NAME_STR_LENGTH)

                    self.locations_checked = set()

                    # Ready for connection
                    if not self.dolphin_status == CONNECTION_VERIFY_SERVER:
                        self.dolphin_status = CONNECTION_VERIFY_SERVER
                        logger.info(self.dolphin_status)

                    await self.server_auth()

                    if not self.slot:
                        await wait_for_next_loop(5)
                        continue

                    arg_seed = read_string(0x80000001, len(str(self.arg_seed)))
                    # logger.info("Seed in memory: " + arg_seed)
                    # logger.info("Seed in Context: " + self.arg_seed)
                    if arg_seed != self.arg_seed:
                        raise Exception(
                            "Incorrect Custom Robo ISO file selected. The seed does not match. " +
                            "Please verify that you are using the right ISO/seed/apcr file.")

                await self.game_watcher()
                await wait_for_next_loop(WAIT_TIMER_SHORT_TIMEOUT)

            except Exception as genericEx:
                dolphin.un_hook()
                logger.error(str(genericEx))
                logger.info(f"Could not connect to Dolphin")
                logger.info("Retrying in 5 seconds...")
                self.dolphin_status = CONNECTION_LOST_STATUS
                await self.disconnect()
                await asyncio.sleep(5)
                continue