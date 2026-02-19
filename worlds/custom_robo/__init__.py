# Python related Imports
from typing import ClassVar
import random
import os

# AP Related Imports
from BaseClasses import Item, Region, Location
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import launch_subprocess, Component, components, Type, SuffixIdentifier

# Relative Imports
from .helpers import *
from .items import ALL_ITEMS_TABLE, PARTS_ITEM_TABLE, CRItem, FILLER_ITEMS, COMPLETION_CONDITIONS, PROGRESSIVE_BASE_ITEM_TABLE, PROGRESSION_RAHU
from .locations import CRLocation, LOCATION_TABLE
from .options import *
from .rules import *
from .cr_rom import CRPlayerContainer
from .cr_settings import CRSettings

def run_client(*args):
    from .CRClient import sync_main
    launch_subprocess(sync_main, name="CustomRoboClient", args=args)

# Add Client launcher to Archi list
components.append(
    Component(display_name="Custom Robo Client",
              game_name="Custom Robo",
              description="Client to interface with Custom Robo AP",
              func=run_client,
              component_type=Type.CLIENT,
              file_identifier=SuffixIdentifier(".apcr"))
)

class CRWeb(WebWorld):
    theme = "stone"

class CRWorld(World):
    """
    Custom Robo is an action RPG where you become a Commander, taking control of your custom robo to dominate the holoseum!
    """

    game: ClassVar[str] = "Custom Robo"
    options_dataclass = CROptions
    options: CROptions
    topology_present = False
    settings: CRSettings

    item_name_to_id: ClassVar[dict[str, int]] = {
        name: data.code for name, data in ALL_ITEMS_TABLE.items()
    }
    location_name_to_id: ClassVar[dict[str, int]] = {
        name: data.code for name, data in LOCATION_TABLE.items()
    }
    data_version = 1
    web = CRWeb()

    def __init__(self, *args, **kwargs):
        super(CRWorld, self).__init__(*args, **kwargs)

    @staticmethod
    def interpret_slot_data(slot_data):
        return slot_data

    def create_regions(self):
        # Add all regions
        chapter_1_region = Region("Chapter 1 - Steel Hearts", self.player, self.multiworld)
        region_data = {
            "Chapter 2 - Test Hall Trials": "Chapter 1 Memories",
            "Chapter 3 - License Test": "Chapter 2 Memories",
            "Chapter 4 - Family Matters": "Chapter 3 Memories",
            "Chapter 5 - Shiner Style": "Chapter 4 Memories",
            "Chapter 6 - Gym Tourney": "Chapter 5 Memories",
            "Chapter 7 - Lab Guard Duty": "Chapter 6 Memories",
            "Chapter 8 - Rahu Appears": "Chapter 7 Memories",
            "Chapter 9 - Police 2v2": "Chapter 8 Memories",
            "Chapter 10 - Secret Police": "Chapter 9 Memories",
            "Chapter 11 - Rahu Returns": "Chapter 10 Memories",
            "Chapter 12 - To The Outside": "Chapter 11 Memories",
            "Chapter 13 - Rahu's Amusement": "Chapter 12 Memories",
        }

        menu_region = Region("Menu", self.player, self.multiworld)

        # Part Checks are always accessible with the correct Part, so add all to Menu region
        for location_name, location_data in LOCATION_TABLE.items():
#            region=self.multiworld.get_region("Menu", self.player)
            if location_data.type == "Part Use":
                location = Location(
                    self.player,
                    location_name,
                    location_data.code,
                    menu_region
                )
                menu_region.locations.append(location)
        self.multiworld.regions.append(menu_region)
        self.multiworld.regions.append(chapter_1_region)
        menu_region.connect(chapter_1_region)

        previous_region = chapter_1_region
        # Create regions from all other chapters
        for region_name, access_condition in region_data.items():
            new_region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(new_region)

            previous_region.connect(new_region, rule=lambda state, access_mem=access_condition: state.has(access_mem, self.player))
            previous_region = new_region

        # Add each battle location to the correct Chapter
        for location_name, location_data in LOCATION_TABLE.items():
            if location_data.type == "Battle Win":
                region = self.multiworld.get_region(location_data.parent_region, self.player)
                location = Location(
                    self.player,
                    location_name,
                    location_data.code,
                    region
                )
                region.locations.append(location)
            else:
                if location_data.type == "Victory":
                    region = self.multiworld.get_region(location_data.parent_region, self.player)
                    location = Location(
                        self.player,
                        location_name,
                        location_data.code,
                        region
                    )
                    region.locations.append(location)


    def generate_basic(self):
        # Set New Journey chapter clear items to organize AP World progression
        self.multiworld.get_location("Chapter 1 - VS Bandit #4", self.player).place_locked_item(
            self.create_item("Chapter 1 Memories"))
        self.multiworld.get_location("Chapter 2 - VS Thomas/Anthony", self.player).place_locked_item(
            self.create_item("Chapter 2 Memories"))
        self.multiworld.get_location("Chapter 3 - VS Test Computer", self.player).place_locked_item(
            self.create_item("Chapter 3 Memories"))
        self.multiworld.get_location("Chapter 4 - VS Walt & Carmen", self.player).place_locked_item(
            self.create_item("Chapter 4 Memories"))
        self.multiworld.get_location("Chapter 5 - VS Shiner", self.player).place_locked_item(
            self.create_item("Chapter 5 Memories"))
        self.multiworld.get_location("Chapter 6 - VS Marcia", self.player).place_locked_item(
            self.create_item("Chapter 6 Memories"))
        self.multiworld.get_location("Chapter 7 - VS Eliza", self.player).place_locked_item(
            self.create_item("Chapter 7 Memories"))
        self.multiworld.get_location("Chapter 8 - VS Sergei", self.player).place_locked_item(
            self.create_item("Chapter 8 Memories"))
        self.multiworld.get_location("Chapter 9 - VS Linda & Ernest", self.player).place_locked_item(
            self.create_item("Chapter 9 Memories"))
        self.multiworld.get_location("Chapter 10 - VS S-Rank Computer", self.player).place_locked_item(
            self.create_item("Chapter 10 Memories"))
        self.multiworld.get_location("Chapter 11 - VS Oboro & Sergei", self.player).place_locked_item(
            self.create_item("Chapter 11 Memories"))
        self.multiworld.get_location("Chapter 12 - VS Rahu II", self.player).place_locked_item(
            self.create_item("Chapter 12 Memories"))
        self.multiworld.get_location("Rahu III Defeated", self.player).place_locked_item(
            self.create_item("Defeat Rahu III"))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Defeat Rahu III", self.player)

    def create_items(self):
        starting_parts = []
        item_pool = []
        # Standard Starting Parts
        if self.options.starting_parts.value == self.options.starting_parts.option_standard:
            print("Standard selected")
            for item_name, item_data in PARTS_ITEM_TABLE.items():
                #if item_data.illegal == False | self.options.illegal_parts_enabled.value:
                if (item_name == "Ray 01" or item_name == "Basic Gun" or item_name == "Standard Bomb"
                        or item_name == "Standard Pod" or item_name == "Standard Legs"):
                    starting_parts.append(self.create_item(item_name))
                else:
                    item_pool.append(self.create_item(item_name))
        # Random Starting Parts
        elif self.options.starting_parts.value == self.options.starting_parts.option_randomized:
            print("Random selected")
            body_list = []
            gun_list = []
            bomb_list = []
            pod_list = []
            legs_list = []
            for item_name, item_data in PARTS_ITEM_TABLE.items():
                if item_data.type == "Body": body_list.append(item_name)
                elif item_data.type == "Gun": gun_list.append(item_name)
                elif item_data.type == "Bomb": bomb_list.append(item_name)
                elif item_data.type == "Pod": pod_list.append(item_name)
                elif item_data.type == "Legs": legs_list.append(item_name)
            start_body = body_list[random.randint(0, (len(body_list)-1))]
            start_gun = gun_list[random.randint(0, (len(gun_list)-1))]
            start_bomb = bomb_list[random.randint(0, (len(bomb_list)-1))]
            start_pod = pod_list[random.randint(0, (len(pod_list)-1))]
            start_legs = legs_list[random.randint(0, (len(legs_list)-1))]
            for item_name, item_data in PARTS_ITEM_TABLE.items():
                if (item_name == start_body or item_name == start_gun or item_name == start_bomb
                        or item_name == start_pod or item_name == start_legs):
                    starting_parts.append(self.create_item(item_name))
                else:
                    item_pool.append(self.create_item(item_name))

        # Add all Rahu Evolution progression parts to the pool
        rahu_evo_total = len(PROGRESSION_RAHU.get("Rahu Evolution Steps"))
        for _ in range(rahu_evo_total):
            item_pool.append(self.create_item("Rahu Evolution"))

        # Pre-collect all starting parts, then send the rest to the multiworld
        for initial_part in starting_parts:
            self.multiworld.push_precollected(initial_part)
        self.multiworld.itempool.extend(item_pool)

        location_count = len(self.multiworld.get_unfilled_locations(self.player))
        items_in_pool = len(item_pool)
        filler_needed = location_count - items_in_pool - 13 # Used to subtract Memory items & Boss defeated value

        filler_items_to_add = random.choices(list(FILLER_ITEMS.keys()), k=filler_needed)

        for filler_item_name in filler_items_to_add:
            self.multiworld.itempool.append(self.create_item(filler_item_name))

        # Set completion condition up with item drop
        # self.multiworld.get_location("Rahu III Defeated", self.player).item = COMPLETION_CONDITIONS.get("Defeat Rahu III")

    def create_item(self, name: str) -> Item:
        item_data = ALL_ITEMS_TABLE[name]
        return Item(name, item_data.classification, item_data.code, self.player)

    def set_rules(self):
        set_rules(self)

    def set_completion_rules(self):
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Defeat Rahu III", self.player)

  
    # Output options and locations for patcher
    def generate_output(self, output_directory: str):
        # Outputs the plando details to our expected output file
        # Create the output path based on the current player + expected patch file ending.
        patch_path = os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}"
            f"{CRPlayerContainer.patch_file_ending}")
        # Output seed name and slot number to seed RNG in randomizer client
        output_data = {
            "Seed": self.multiworld.seed,
            "Slot": self.player,
            "Name": self.player_name,
            "Locations": {},
            "APWorldVersion": CLIENT_VERSION
        }
        # Create a zip (container) that will contain all the necessary output files for us to use during patching.
        cr_container = CRPlayerContainer(output_data, patch_path, self.multiworld.player_name[self.player], self.player)
        # Write the expected output zip container to the Generated Seed folder.
        cr_container.write()

    def fill_slot_data(self):
        return {
            "seed": self.multiworld.seed,
#            "illegal_parts_enabled": self.options.illegal_parts_enabled.value,
            "starting_parts": self.options.starting_parts.value,
            "total_locations": len(LOCATION_TABLE)
        }
