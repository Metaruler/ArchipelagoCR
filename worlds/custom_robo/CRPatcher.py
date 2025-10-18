import os
import json
import struct
import zipfile

from gclib.gcm import GCM
from gclib.dol import DOL

import Utils

from .items import ALL_ITEMS_TABLE, CRItemData
from .locations import LOCATION_TABLE, CRLocationData
from .helpers import CLIENT_VERSION, AP_WORLD_VERSION_NAME, StringByteFunction as sbf
from CommonClient import logger

from ..oot.Messages import bytes_to_int

class CRPatcher:
    def __init__(self, patch_file_path: str):
        from .cr_rom import get_base_rom_path, CRUSAPatch
        self.clean_iso_path = get_base_rom_path()

        base_path = os.path.splitext(patch_file_path)[0]
        self.output_file_path = base_path + CRUSAPatch.result_file_ending
        self.gcm = None
        self.dol = None

        try:
            if os.path.isfile(patch_file_path):
                temp_file = open(patch_file_path, "r+")
                temp_file.close()
        except IOError:
            raise Exception("'" + patch_file_path + "' is currently used in another program.")
        
        with zipfile.ZipFile(patch_file_path, "r") as zf:
            apcr_bytes = zf.read("patch.apcr")
        self.output_data = json.loads(apcr_bytes.decode('utf-8'))

        # This will make sure client and server versions match
        self._check_apworld_version(self.output_data)

        # Read the entire ISO, system files, etc after checking versions
        self.gcm = GCM(self.clean_iso_path)
        self.gcm.read_entire_disc()
        self.dol = DOL()
        self.dol.read(self.gcm.read_file_data("sys/main.dol"))

        # Change game ID so save files are different
        from CommonClient import logger

        logger.info("Updating the ISO game id with the AP generated seed.")
        self.seed = self.output_data["Seed"]
        magic_seed = str(self.seed)
        print("Magic Seed is :" + magic_seed)
        bin_data = self.gcm.read_file_data("sys/boot.bin")
        # Seek will put us right after the first letter G of the Disk ID
        bin_data.seek(0x01)
        # Modify ISO ID to make it unique to our patch
        #bin_data.write(sbf.string_to_bytes("MT", 2))
        # Write the Seed into the Disk ID to make it unique to multiworld
        bin_data.write(sbf.string_to_bytes(magic_seed, len(magic_seed)))
        self.gcm.changed_files["sys/boot.bin"] = bin_data

    def write_item_to_location(self, location_name: str, item_name: str):
        """
        This function to look up the correct addresses and IDs and write the new item into the memory.
        """
        try:
            # 1 - We will look up the locations address from Location table
            if location_name not in LOCATION_TABLE:
                print(f"Warning: Skipping unknown '{location_name}'.")
                return

            # 2 - Look up the Item's ID from ALL_ITEMS_TABLE
            if item_name not in ALL_ITEMS_TABLE:
                print(f"Warning: Skipping Unknown Item '{item_name}'.")
                return

            #location_data: CRLocationData = LOCATION_TABLE[location_name]
            #dol_address = location_data.ram_addr
#
            #item_data: CRItemData = ALL_ITEMS_TABLE[item_name]
            ## This access our item ID from our Data class to tell this randomizer WHICH item it is.
            #item_ramloc = item_data.update_ram_addr[0].ram_addr
            #item_bitpos = item_data.update_ram_addr[0].bit_position
            #logger.info("Position accessed")
#
            ## Writes the New Item ID to the DOL - - - - -
            ## This coverts the Item ID into the byte sequence.
            ##item_id_bytes = struct.pack(">I", item_rom_id)
            #self.dol.data.seek(item_ramloc)
            #part_flags = self.dol.data.read1(1)
            #part_flags_int = bytes_to_int(part_flags)
            #item_id_bytes = (part_flags_int & (1 << item_bitpos))
            #self.dol.data.seek(item_ramloc)
            #self.dol.data.write(item_id_bytes)
            #logger.info("Line 90")

        except Exception as e:
            print(f"An error occured while writing data for location '{location_name}' and item '{item_name}': {e}")
            return

    def _check_apworld_version(self, output_data):
        """
        Compares the AP version in the patch to the client version
        """

        ap_world_version = output_data[AP_WORLD_VERSION_NAME]
        if ap_world_version != CLIENT_VERSION:
            raise Utils.VersionException("Error! Client/World version mismatch detected.")
        
    def create_patch(self):
        """
        This function will create the Custom Robo patch
        """

        print("Entering patch save")
        print("Applying Randomized Item Patches...")
        for location_name, item_name in self.output_data["Locations"].items():
            self.write_item_to_location(location_name, item_name)
        print("Randomized item patching complete")

        self.dol.save_changes()
        self.gcm.changed_files["sys/main.dol"] = self.dol.data

        for _, _ in self.export_files_from_memory():
            continue

    def export_files_from_memory(self):
        yield from self.gcm.export_disc_to_iso_with_changed_files(self.output_file_path)

