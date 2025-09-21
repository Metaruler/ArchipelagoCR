# Python related Imports
from typing import ClassVar
import random

# AP Related Imports
from BaseClasses import Item, Region, Location
from worlds.AutoWorld import WebWorld, World

# Relative Imports
from .helpers import *
from .items import ALL_ITEMS_TABLE, CRItem, FILLER_ITEMS
from .locations import LOCATION_TABLE, CHAPTER_COUNTER
from .options import *
from .rules import *

class CRWeb(WebWorld):
    theme = "stone"

class CRWorld(World):
    """
    Custom Robo is an action RPG where you become a Commander, taking control of your custom robo to dominate the holoseum!
    """

    game: ClassVar[str] = "Custom Robo"
    options_dataclass = options.CROptions
    options: options.CROptions

    topology_present = False
    item_name_to_id: ClassVar[dict[str, int]] = {
        name: CRItem.get_apid(data.code) for name, data in ALL_ITEMS_TABLE.items()
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
        # Add all randomizable regions
        region_data = {"Default": ""}

        menu_region = Region("Menu", self.player, self.multiworld)

        for location_name, location_data in LOCATION_TABLE.items():
#            region=self.multiworld.get_region("Menu", self.player)
            location = Location(
                self.player,
                location_name,
                location_data.code,
                menu_region
            )
            menu_region.locations.append(location)
        self.multiworld.regions.append(menu_region)
            

    def create_items(self):
        item_pool = []
        for item_name, item_data in ALL_ITEMS_TABLE.items():
            item_pool.append(self.create_item(item_name))

        self.multiworld.itempool.extend(item_pool)

        location_count = len(self.multiworld.get_locations())
        items_in_pool = len(self.multiworld.itempool)
        filler_needed = location_count - items_in_pool

        filler_items_to_add = random.choices(list(FILLER_ITEMS.keys()), k=filler_needed)

        for filler_item_name in filler_items_to_add:
            self.multiworld.itempool.append(self.create_item(filler_item_name))

    def create_item(self, name: str) -> Item:
        item_data = ALL_ITEMS_TABLE[name]
        return Item(name, item_data.classification, item_data.code, self.player)
    
#    def set_rules(self):
#        set_rules(self)

    def set_completion_rules(self):
        self.multiworld.completion_condition[self.player] = (CHAPTER_COUNTER == 18)

    def fill_slot_data(self):
        try:
            slot_data = {
                "total_locations": len(LOCATION_TABLE)
            }
        except AttributeError:
            slot_data = {
                "total_locations": len(LOCATION_TABLE)
            }
        return slot_data
