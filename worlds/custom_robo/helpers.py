from typing import NamedTuple, Optional
import asyncio

CLIENT_NAME = "Custom Robo"
CLIENT_VERSION = "v0.1.0"

AP_LOGGER_NAME = "Client"
AP_WORLD_VERSION_NAME = "APWorldVersion"

# All the dolphin connection messages used in the client
CONNECTION_REFUSED_STATUS = "Detected the incorrect ROM for Custom Robo. Please close and load a different one. Retrying in 5 seconds..."
CONNECTION_LOST_STATUS = "Dolphin connection was lost. Please restart your emulator and make sure Custom Robo is running."
NO_SLOT_NAME_STATUS = "No slot name was detected. Ensure the correct ROM is loaded. Retrying in 5 seconds..."
CONNECTION_VERIFY_SERVER = "Dolphin was confirmed to be opened and ready, Connect to the server when ready..."
CONNECTION_INITIAL_STATUS = "Dolphin emulator was not detected to be running. Retrying in 5 seconds..."
CONNECTION_CONNECTED_STATUS = "Dolphin is connected, AP is connected, it's time to test your metal in Custom Robo!"

class CRRamData(NamedTuple):
    ram_addr: Optional[int] = None
    bit_position: Optional[int] = None
    ram_byte_size: Optional[int] = None
    pointer_offset: Optional[int] = None
    in_game_room_id: Optional[int] = None
    item_count: Optional[int] = None

async def wait_for_next_loop(time_to_wait: int):
    await asyncio.sleep(time_to_wait)

class StringByteFunction:
    @staticmethod
    def string_to_bytes(user_string: str, encoded_byte_length: int) -> bytes:
        """
        Encodes a provided string to UTF-8 format. Adds padding until the expected length is reached.
        If provided string is longer than expected length, raise an exception

        :param user_string: String that needs to be encoded to bytes.
        :param encoded_byte_length: Expected length of the provided string.
        """
        #print("Encoded string before mods is: " + user_string)
        #print("Byte length is: " + str(encoded_byte_length))
        encoded_string = user_string.encode('utf-8')

        if len(encoded_string) < encoded_byte_length:
            encoded_string += b'\x00' * (encoded_byte_length - len(encoded_string))
        elif len(encoded_string) > encoded_byte_length:
            raise Exception("Provided string '" + user_string + "' was longer than the expected byte length of '" +
                            str(encoded_byte_length) + "', which will not be accepted by the info file.")

        #print("Byte length is: " + str(encoded_byte_length))

        return encoded_string