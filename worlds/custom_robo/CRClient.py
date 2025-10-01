# Imports
import asyncio

# AP Imports
from CommonClient import CommonContext, ClientCommandProcessor, logger, get_base_parser, server_loop, gui_enabled
from NetUtils import NetworkItem

# Local Imports
import dolphin_memory_engine as dolphin
from .locations import PART_USE, LOCATION_TABLE
from .items import ALL_ITEMS_TABLE


# Command Processor
class CRCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext, server_address: str = None):
        if server_address:
            ctx.server_address = server_address
        super().__init__(ctx)

#--------------------------------------------------------------------
#Context for CR
class CRContext(CommonContext):
    """
    This is the context class for the Custom Robo client. 
    This will inherit from the core class "CommonContext" in AP.
    This will hold all the game information, state, and functionality to run the client.
    """
    def __init__(self, server_address: str = "", settings: dict = {}, *args, **kwargs):
        super().__init__(server_address, *args, **kwargs)
    
        # Handle various Dolphin connection related tasks
#        self.instance_id = None
#        self.dolphin_sync_task: Optional[asyncio.Task[None]] = None
#        self.dolphin_status = CONNECTION_INITIAL_STATUS
#        self.item_display_queue: list[NetUtils.NetworkItem] = []

        # We will use this list to store every location already checked.
        # This also makes sure to not send duplicates!
        self.checked_locations = set()

        # We will use this list to hold all items received in the multiworld.
        # This will be needed to give items to the player! 
        self.items_received = []

        #This also stores our options from MMXCMOptions, which is determined by player.
        self.settings = settings

def run_gui(self):
    """
    Placeholder for GUI
    """
    pass

async def on_package(self, cmd: str , args: dict): 
    """
    This is the method that is called by CommonClient when a package is received from the server.
    """

    # This will check if the client is correctly connected to the AP server
    if cmd == "Connected":
        self.game_running = True
        await self.send_connect()
        print("Successfully connected to the Archipelago server!")
    # This checks if the incoming message from AP server is "Received Items"
    elif cmd == "ReceivedItems":
        # This is the package sent when we get something from a different player.
        items_to_add = []
        for item in args["items"]:
            # This is the format of the item.
            items_to_add.append(NetworkItem(*item))

    # This will check the list of items to give to player before continuing. 
    if items_to_add:
        self.items_received.extend(items_to_add)
        print(f"Received {len(items_to_add)} new item(s) from the MultiWorld.")
        for item in items_to_add:
            print(f" - {self.item_id_to_name.get(item.item, 'Unknown Item')} from {self.player_names[item.player]}")

    # Prints messages from the Server, like hints! 
    elif cmd == "Print":
        print(args["text"])

#--------------------------------------------------------------------

# Starts the full loop and debug messages for connecting to Dolphin.
async def dolphin_connect_loop(ctx: CommonContext):
    """
    Connects to the Dolphin emulator and waits for the correct game to be running.
    """
    while True:
        try:
            if not dolphin.is_hooked():
                dolphin.hook()

            if dolphin.get_status() == dolphin.Dolphin.DolphinStatus.no_emu or \
            dolphin.get_status() == dolphin.Dolphin.DolphinStatus.not_running:
                if dolphin.is_hooked():
                    dolphin.un_hook()
                print("Dolphin not running. Waiting for emulator...")
                await asyncio.sleep(5)
                continue

            game_id = dolphin.read_bytes(0x80000000, 6)
            if game_id.decode("ascii") not in ["GXCE01"]:
                print("Incorrect game ID. Make sure Custom Robo is running.")
                if dolphin.is_hooked():
                    dolphin.un_hook()
                await asyncio.sleep(5)
                continue
            
            print("Connected to Dolphin with the correct game running.")
            break

        except Exception as e:
            if dolphin.is_hooked():
                dolphin.un_hook()
            print(f"Could not connect to Dolphin: {e}")
            print("Retrying in 5 seconds...")
            await asyncio.sleep(5)
            continue

class CRCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CRContext):
        super().__init__(ctx)

    def _cmd_cr(self, *args):
        """
        These are the commands for our CR Client.
        Serving as a place holder until we need custom commands!
        """
        print("Custom Robo Client.")

async def game_watcher(ctx: CRContext):
    """
    This is the main loop that will handle checking locations and giving items.
    It will run as long as the client is connected to the server.
    """

    # This initializes the set locations checked.
    checked_locations_in_game = set()

    while not ctx.finished_game:
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
            await ctx.send_checked_locations(newly_checked_locations)

        if not ctx.finished_game:
            try:
                # Get the RAM data for the final scene in the New Journey scenario. This is our "beating the game". 
                scenario_ram_data = LOCATION_TABLE["Rahu III Defeated"].get("ram_addr")

                if scenario_ram_data:
                    # Read the value at the event's memory address.
                    boss_defeated_value = dolphin.read_bytes(scenario_ram_data.ram_addr, 1)[0]

                    # Check if the bit for defeating Redips is set.
                    if boss_defeated_value == 18:
                        print("Final boss defeated! Signaling game completion to the server.")
                        await ctx.send_goal()
                        ctx.finished_game = True  # This ends the while loop on the next pass.
            except Exception as e:
                # This will catch errors if the game state is not readable or the address is invalid.
                print(f"Error checking for game completion: {e}")
        
        # Check for new items.
        while ctx.items_received:
            item_to_add = ctx.items_received.pop(0)

            item_name = ctx.item_id_to_name[item_to_add.item]
            player_name = ctx.slot_to_player_name[item_to_add.player]
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
        
        # Checker to see if we have the initial parts (FIX: should be more elegant)
        #if not ray_checked:
        #    if ALL_ITEMS_TABLE.get("Ray 01")

        await asyncio.sleep(1) # Can set this so sleep to avoid CPU usage.

    dolphin.disconnect()
    print("Disconnected from Dolphin.")

def main(*launch_args: str):
    """
    This is the main function that will be called by the `CommonClient`
    to start our client.
    """
    
    # server_address: str = ""
    # rom_path: str = ""

    logger.info("Starting Custom Robo Client v0.1")

    parser = get_base_parser(ctx_defaults={"game": "Custom Robo"})
    parser.add_arguement('apcr_file', default="", type=str, nargs="?", help="Path to an APCR file")
    args = parser.parse_args(launch_args)

    async def _async_main(connect, password):

        print("Entering async main")

        # Create our context and initialize the command processor.
        ctx = CRContext(connect, password)
        ctx.command_processor = CRCommandProcessor(ctx)

        print("Command processor active")

        # Run the client!
        ctx.run_gui = gui_enabled

        print("GUI enabled")

        await dolphin_connect_loop(ctx)

        print("Dolphin connection complete")

        await server_loop(ctx, game_watcher, "Game")

    asyncio.run(_async_main(args.connect, args.password))

if __name__ == "__main__":
    # This ensures that the script will run the main function when executed.
    asyncio.run(main())