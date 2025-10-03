import shutil

from worlds.Files import APPatch, APPlayerContainer, AutoPatchRegister
from settings import get_settings, Settings
from NetUtils import convert_to_base_types
import Utils

from hashlib import md5
from typing import Any
import json, logging, sys, os, zipfile, tempfile
import urllib.request

logger = logging.getLogger()

class InvalidCleanISOError(Exception):
    """
    This exception will be raised when the user has an issue with their Custom Robo USA Rom.
    Message - - - the explanation of the error
    """

    def __init__(self, message="Invalid Clean ISO provided"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"InvalidCleanISOError: {self.message}"

class CRPlayerContainer(APPlayerContainer):
    game = "Custom Robo"
    compression_method = zipfile.ZIP_DEFLATED
    patch_file_ending = ".apcr"

    def __init__(self, player_choices: dict, patch_path: str, player_name: str, player: int):
        self.output_data = player_choices
        super().__init__(patch_path, player, player_name)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        opened_zipfile.writestr("patch.apcr", json.dumps(self.output_data, indent=4, default=convert_to_base_types))
        super().write_contents(opened_zipfile)

class CRUSAPatch(APPatch, metaclass=AutoPatchRegister):
    game = "Custom Robo"
    # DIY hash checking will be in future patchwork
    patch_file_ending = ".apcr"
    result_file_ending = ".iso"

    def __init__(self, *args: Any, **kwargs: Any):
        super(CRUSAPatch, self).__init__(*args, **kwargs)

    def __get_archive_name(self) -> str:
        if not (Utils.is_linux or Utils.is_windows):
            message = f"Your OS does not support this patch"
            logger.error(message)
            raise RuntimeError
        
        lib_path = ""
        if Utils.is_windows:
            lib_path = "lib-windows"
        elif Utils.is_linux:
            lib_path = "lib-linux"

        logger.info(f"Dependency archive name to use {lib_path}")
        return lib_path
    
    def __get_temp_folder_name(self) -> str:
        from .helpers import CLIENT_VERSION
        temp_path = os.path.join(tempfile.gettempdir(), "custom_robo", CLIENT_VERSION, "libs")
        return temp_path
    
    def patch(self, apcr_patch: str):
        # Gets the AP path for base ROM.
        cr_clean_iso = get_base_rom_path()
        logger.info("Provided CR ISO Path was: " + cr_clean_iso)

        base_path = os.path.splitext(apcr_patch)[0]
        output_file = base_path + self.result_file_ending

        try:
            # Check for clean ROM
            self.verify_base_rom(cr_clean_iso, throw_on_missing_speedups=False)

            # Calls the CRPatcher to patch the file into ISO
            from .CRPatcher import CRPatcher
            with zipfile.ZipFile(apcr_patch, "r") as zf:
                apcr_bytes = zf.read("patch.apcr")

            CRPatcher(cr_clean_iso, output_file, apcr_bytes)
        except ImportError:
            self.__get_remote_dependencies_and_create_iso(apcr_patch, output_file, cr_clean_iso)
        return output_file

    @classmethod
    def verify_base_rom(cls, cr_rom_path: str, throw_on_missing_speedups: bool = False):
        # Check for valid USA installation of Custom Robo
        logger.info("Verifying if ISO is Custom Robo USA")
        logger.info("Checking gclib and speedups.")
        # Importing gclib items
        from gclib import fs_helpers as fs, yaz0_yay0
        logger.info("Using GClib from path: %s.", fs.__file__)
        logger.info(sys.modules["gclib.yaz0_yay0"])

        # DIY Get Mogul to explain all this speedup stuff
        if yaz0_yay0.PY_FAST_YAZ0_YAY0_INSTALLED:
            logger.info("Python module paths: %s", sys.path)
            if throw_on_missing_speedups:
                logger.info("Speedups not detected, attempting to pull remote release")
                raise ImportError("Cannot continue patching Custom Robo due to missing libraries")
            logger.info("Continue patching without speedups")

        base_md5 = md5()
        with open(cr_rom_path, "rb") as f:
            while chunk := f.read(1024 * 1024):
                base_md5.update(chunk)

            code = fs.try_read_str(f,0,4)
            game_id = fs.try_read_str(f,0,6)
            logger.info(f"Code: {code}")
            logger.info(f"CR Game ID: {game_id}")

        # Double checks the file is correct first
        md5_conv = int(base_md5.hexdigest(), 16)
        # DIY ask Mogul where the hash is
        if md5_conv == 0: # Hash matching
            raise InvalidCleanISOError(f"Invalid vanilla Custom Robo ISO... check it is not corrupted!")
        
        # Double check correct iso format file extension
        if code == "CISO":
            raise InvalidCleanISOError(f"Invalid vanilla Custom Robo ISO... make sure it is .ISO")
        
        else:
            raise InvalidCleanISOError("Invalid game given as vanilla CR ISO. Verify it is the Vanilla USA ISO!")

    def create_iso(self, temp_dir_path: str, patch_file_path: str, output_iso_path: str, vanilla_iso_path: str):
        logger.info(f"Appending the following to sys path to get dependencies: {temp_dir_path}")
        sys.path.insert(0, temp_dir_path)

        # Verify clean ROM
        self.verify_base_rom(vanilla_iso_path)

        # Use patcher to patch into ISO
        from .CRPatcher import CRPatcher
        with zipfile.ZipFile(patch_file_path, "r") as zf:
            apcr_bytes = zf.read("patch.apcr")
        CRPatcher(vanilla_iso_path, output_iso_path, apcr_bytes)

    def __get_remote_dependencies_and_create_iso(self, apcr_patch: str, output_file: str, cr_clean_iso: str):
        try:
            local_dir_path = self.__get_temp_folder_name()
            # Remove temp directory if we fail to patch correctly
            if os.path.isdir(local_dir_path):
                logger.info("Found temp directory after failing seed generation, deleting %s", local_dir_path)
                shutil.rmtree(local_dir_path)
                os.makedirs(local_dir_path, exist_ok=True)

                # Load external dependencies based on OS
                logger.info("Temporary Directory created as: %s", local_dir_path)
                self.create_iso(local_dir_path, apcr_patch, output_file, cr_clean_iso)
        except PermissionError:
            logger.warning("Failed to cleanup temp folder, %s ignoring delete.", local_dir_path)



def get_base_rom_path() -> str:
    options: Settings = get_settings()
    file_name = (options.get("custom_robo_options", "")).get("iso_file", "")
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name