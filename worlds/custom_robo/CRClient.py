# Imports
import asyncio
import sys

# AP Imports
from CommonClient import CommonContext, ClientCommandProcessor, logger, get_base_parser, server_loop, gui_enabled
from NetUtils import NetworkItem
import Utils

# Local Imports
import dolphin_memory_engine as dolphin
from .locations import PART_USE, LOCATION_TABLE
from .items import ALL_ITEMS_TABLE
from .helpers import *


# Command Processor
class CRCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_cr(self, *args):
        """
        Commands for the Custom Robo Client.
        Currently a placeholder.
        """
        logger.info("Custom Robo Client.")

#--------------------------------------------------------------------

def sync_main(*launch_args: str):
    Utils.init_logging(CLIENT_NAME)

    parser = get_base_parser()
    parser.add_argument('apcr_file', default="", type=str, nargs="?", help="Path to an APCR file")
    args = parser.parse_args(launch_args)

    # Patch (will be used for future rando)
    if args.apcr_file:
        from .CRPatcher import CRPatcher
        cr_patch = CRPatcher(args.apcr_file)
        cr_patch.create_patch()

    asyncio.run(async_main(args.connect, args.password))

async def async_main(connect, password):
    """
    This is the main function that will be called by the `CommonClient`
    to start our client.
    """
    try:
        # Create our context and initialize the command processor.
        from .CRContext import CRContext
        ctx = CRContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")

        # Run the client!
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        ctx.dolphin_server_task = asyncio.create_task(ctx.dolphin_connect_loop(), name="Custom Robo Dolphin Loop")

        if ctx.dolphin_server_task:
            await ctx.dolphin_server_task
    except Exception as genericEX:
        logger.error("Unable to run Dolphin async. Ex: " + str(genericEX))

if __name__ == "__main__":
    # This ensures that the script will run the main function when executed.
    sync_main(*sys.argv[1:])