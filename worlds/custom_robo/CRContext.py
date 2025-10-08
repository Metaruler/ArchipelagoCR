# Python imports
from typing import Dict
import asyncio

# AP imports
from CommonClient import CommonContext, logger, logging

# 3rd party imports
import dolphin_memory_engine as dolphin

# Relative imports
from .CRClient import CRCommandProcessor
from .helpers import *
from .locations import PART_USE, LOCATION_TABLE
from .items import ALL_ITEMS_TABLE

from worlds.tww.TWWClient import read_string


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
                self.arg_seed = str(slot_data["seed"])
                # try:
                #     # Read ISO seed
                #     iso_seed = read_string(0x80000000, len(arg_seed))
                # except Exception as genericEx:
                #     iso_seed = ""
                #     logger.error(str(genericEx))
                #
                # if arg_seed != iso_seed:
                #     raise Exception("Error: Incorrect Custom Robo ISO File launched")
                # else:
                #     self.seed_verified = True
                #     logger.info("Game seed verified")
                #
                # logger.info("Archipelago server connection successful")
                self.game_running = True
            case "RecievedItems":
                # Recieved Items are handled in a different function
                pass

    async def disconnect(self, allow_autoreconnect = False):
        await super().disconnect(allow_autoreconnect)
    
        dolphin.un_hook()
        self.checked_locations = set()
        self.seed_verified = False
        self.dolphin_connected = False
        self.already_fired_events = False

    async def game_watcher(self):
        """
        This is the main loop that will handle checking locations and giving items.
        It will run as long as the client is connected to the server.
        """

        logger.info("Entering game watcher loop")
        # This initializes the set locations checked.
        checked_locations_in_game = set()

        while not self.finished_game:
            # Check for new locations.
            # Replace these with the flags in locations py.
            set_check_locations = []
            newly_checked_locations = []

            # Check for the usage flag to be set before checking reset
            for location_name, location_info in PART_USE.items():
                ram_data = location_info.get("ram_addr")
                location_value = dolphin.read_bytes(ram_data.ram_addr, 1)[0]
                if (location_value & (1 << ram_data.bit_position)) > 0:
                    set_check_locations.append(location_name, location_info)

            # Check for part usage
            for location_name, location_info in set_check_locations.items():
                if location_name not in checked_locations_in_game:
                    # Reads the value at the locations RAM address.
                    try:
                        ram_data = location_info.get("ram_addr")
                        if ram_data:
                            # Read the value at the locations RAM address.
                            location_value = dolphin.read_bytes(ram_data.ram_addr, 1)[0]
                            # Check if the location's bit position has been reset in the value.
                            # (this indicates that the part has been used)
                            if (location_value & (1 << ram_data.bit_position)) < 1:
                                newly_checked_locations.append(location_name)
                                checked_locations_in_game.add(location_name)
                    except Exception as e:
                        print(f"Error reading location '{location_name}' at address {hex(location_info['ram_addr'])}: {e}")

            if newly_checked_locations:
                print(f"Found new locations: {newly_checked_locations}")
                await self.send_checked_locations(newly_checked_locations)

            if not self.finished_game:
                try:
                    # Get the RAM data for the final scene in the New Journey scenario. This is our "beating the game". 
                    scenario_ram_data = LOCATION_TABLE["Rahu III Defeated"].get("ram_addr")

                    if scenario_ram_data:
                        # Read the value at the event's memory address.
                        boss_defeated_value = dolphin.read_bytes(scenario_ram_data.ram_addr, 1)[0]

                        # Check if the bit for defeating Redips is set.
                        if boss_defeated_value == 18:
                            print("Final boss defeated! Signaling game completion to the server.")

                            await self.send_goal()
                            self.finished_game = True  # This ends the while loop on the next pass.
                except Exception as e:
                    # This will catch errors if the game state is not readable or the address is invalid.
                    print(f"Error checking for game completion: {e}")

            # Check for new items.
            while self.items_received:
                item_to_add = self.items_received.pop(0)

                item_name = self.item_id_to_name[item_to_add.item]
                player_name = self.slot_to_player_name[item_to_add.player]
                print(f"Received item: {item_name} from {player_name}.")

                item_info = ALL_ITEMS_TABLE.get(item_name)

                if item_info:
                    item_type = item_info["type"]
                    if item_type == "Body" or item_type == "Gun" or item_type == "Bomb" or item_type == "Pod" or item_type == "Legs":
                        dolphin.write_bytes(item_info.update_ram_addr, 1)
                        location_edit = "Use " + item_info.name
                        dolphin.write_bytes(LOCATION_TABLE[location_edit].ram_addr, 1)
                else:
                    print(f"Error: Could not find type information for item ID {item_to_add.item}.")

            await asyncio.sleep(1) # Can set this so sleep to avoid CPU usage.

        # dolphin.disconnect()
        print("Disconnected from Dolphin.")

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
                    if game_id not in ["GXCEMT"]:
                        logger.info(CONNECTION_REFUSED_STATUS)
                        self.dolphin_status = CONNECTION_REFUSED_STATUS
                        dolphin.un_hook()
                        await wait_for_next_loop(5)
                        continue

                    arg_seed = read_string(0x80000001, len(str(self.arg_seed)))
                    #logger.info("Seed in memory: " + arg_seed)
                    #logger.info("Seed in Context: " + self.arg_seed)
                    if arg_seed != self.arg_seed:
                        raise Exception(
                            "Incorrect Custom Robo ISO file selected. The seed does not match." +
                            "Please verify that you are using the right ISO/seed/apcr file.")

                    self.locations_checked = set()

                    # Ready for connection
                    if not self.dolphin_status == CONNECTION_VERIFY_SERVER:
                        self.dolphin_status = CONNECTION_VERIFY_SERVER
                        logger.info(self.dolphin_status)

                    await self.server_auth()

                    if not self.slot:
                        await wait_for_next_loop(5)
                        continue

            except Exception as genericEx:
                dolphin.un_hook()
                logger.error(str(genericEx))
                logger.info(f"Could not connect to Dolphin")
                logger.info("Retrying in 5 seconds...")
                self.dolphin_status = CONNECTION_LOST_STATUS
                await self.disconnect()
                await asyncio.sleep(5)
                continue