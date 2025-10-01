import shutil

from worlds.Files import APPatch, APPlayerContainer, AutoPatchRegister
from settings import get_settings, Settings
from NetUtils import convert_to_base_types
import Utils

from hashlib import md5
from typing import Any
import json, logging, sys, os, zipfile, tempfile
import urllib.request

class CRPlayerContainer(APPlayerContainer):
    game = "Custom Robo"
    compression_method = zipfile.ZIP_DEFLATED
    patch_file_ending = ".apcr"

    def __init__(self, player_choices: dict, patch_path: str, player_name: str, player: int,
        server: str = ""):
        self.output_data = player_choices
        super().__init__(patch_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        opened_zipfile.writestr("patch.apcr", json.dumps(self.output_data, indent=4, default=convert_to_base_types))
        super().write_contents(opened_zipfile)