import os
import json
import zipfile

from gclib.gcm import GCM
from gclib.dol import DOL

import Utils

from .items import ALL_ITEMS_TABLE, CRItemData
from .locations import LOCATION_TABLE, CRLocationData
from .helpers import CLIENT_VERSION, AP_WORLD_VERSION_NAME, StringByteFunction as sbf

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
        bin_data = self.gcm.read_file_data("sys/boot.bin")
        bin_data.seek(0x01)
        bin_data.write(sbf.string_to_bytes(magic_seed, len(magic_seed)))
        self.gcm.changed_files["sys/boot.bin"] = bin_data

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

        for _, _ in self.export_files_from_memory():
            continue

    def export_files_from_memory(self):
        yield from self.gcm.export_disc_to_iso_with_changed_files(self.output_file_path)

