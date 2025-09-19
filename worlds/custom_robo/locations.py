#Checks
from typing import NamedTuple, Dict, Optional
from .Items import CRItemData
from .Helpers import CRRawData

class CRLocationData(NamedTuple):
  game:str = "Custom Robo"
  code:Optional[int]
  ram_addr: Optional[CRRawData] = None

# Begin check logic
# Check for each part being used in a victory
PART_USE: dict[str, CRLocationData] = {
  "Use Ray 01": CRLocationData(
    code=1,
    ram_addr=CRRawData(0x803BFBA7, bit_position=1)
  ),
  "Use Splendor": CRLocationData(
    code=2,
    ram_addr=CRRawData(0x803BFBA7, bit_position=2)
  ),
  "Use Glory": CRLocationData(
    code=3,
    ram_addr=CRRawData(0x803BFBA7, bit_position=3)
  ),
  "Use Milky Way": CRLocationData(
    code=4,
    ram_addr=CRRawData(0x803BFBA7, bit_position=4)
  ),
  "Use Earth": CRLocationData(
    code=5,
    ram_addr=CRRawData(0x803BFBA7, bit_position=5)
  ),
  "Use Sol": CRLocationData(
    code=6,
    ram_addr=CRRawData(0x803BFBA7, bit_position=6)
  ),
  "Use Metal Ape": CRLocationData(
    code=7,
    ram_addr=CRRawData(0x803BFBA7, bit_position=7)
  ),
  "Use Metal Bear": CRLocationData(
    code=8,
    ram_addr=CRRawData(0x803BFBA7, bit_position=8)
  ),
  "Use Metal Ox": CRLocationData(
    code=9,
    ram_addr=CRRawData(0x803BFBA6, bit_position=1)
  ),
  "Use Swift": CRLocationData(
    code=10,
    ram_addr=CRRawData(0x803BFBA6, bit_position=2)
  ),
  "Use Shrike": CRLocationData(
    code=11,
    ram_addr=CRRawData(0x803BFBA6, bit_position=3)
  ),
  "Use Peregrine": CRLocationData(
    code=12,
    ram_addr=CRRawData(0x803BFBA6, bit_position=4)
  ),
  "Use Javelin": CRLocationData(
    code=13,
    ram_addr=CRRawData(0x803BFBA6, bit_position=5)
  ),
  "Use Glaive": CRLocationData(
    code=14,
    ram_addr=CRRawData(0x803BFBA6, bit_position=6)
  ),
  "Use Halberd": CRLocationData(
    code=15,
    ram_addr=CRRawData(0x803BFBA6, bit_position=7)
  ),
  "Use Criminal": CRLocationData(
    code=16,
    ram_addr=CRRawData(0x803BFBA6, bit_position=8)
  ),
  "Use Buggy": CRLocationData(
    code=17,
    ram_addr=CRRawData(0x803BFBA5, bit_position=1)
  ),
  "Use Juggler": CRLocationData(
    code=18,
    ram_addr=CRRawData(0x803BFBA5, bit_position=2)
  ),
  "Use Defender": CRLocationData(
    code=19,
    ram_addr=CRRawData(0x803BFBA5, bit_position=3)
  ),
  "Use Seeker": CRLocationData(
    code=20,
    ram_addr=CRRawData(0x803BFBA5, bit_position=4)
  ),
  "Use Breaker": CRLocationData(
    code=21,
    ram_addr=CRRawData(0x803BFBA5, bit_position=5)
  ),
  "Use Seal Head": CRLocationData(
    code=22,
    ram_addr=CRRawData(0x803BFBA5, bit_position=6)
  ),
  "Use Dour Head": CRLocationData(
    code=23,
    ram_addr=CRRawData(0x803BFBA5, bit_position=7)
  ),
  "Use Tank Head": CRLocationData(
    code=24,
    ram_addr=CRRawData(0x803BFBA5, bit_position=8)
  ),
  "Use Ray Legend": CRLocationData(
    code=25,
    ram_addr=CRRawData(0x803BFBA4, bit_position=1)
  ),
  "Use Oil Can": CRLocationData(
    code=26,
    ram_addr=CRRawData(0x803BFBA4, bit_position=2)
  ),
  "Use Ray Warrior": CRLocationData(
    code=27,
    ram_addr=CRRawData(0x803BFBA4, bit_position=3)
  ),
  "Use Rakansen": CRLocationData(
    code=28,
    ram_addr=CRRawData(0x803BFBA4, bit_position=4)
  ),
  "Use Ruhiel": CRLocationData(
    code=29,
    ram_addr=CRRawData(0x803BFBA4, bit_position=5)
  ),
  "Use Athena": CRLocationData(
    code=30,
    ram_addr=CRRawData(0x803BFBA4, bit_position=6)
  ),
  "Use Rahu I": CRLocationData(
    code=31,
    ram_addr=CRRawData(0x803BFBA4, bit_position=7)
  ),
  "Use Rahu II": CRLocationData(
    code=32,
    ram_addr=CRRawData(0x803BFBA4, bit_position=8)
  ),
  "Use Rahu III": CRLocationData(
    code=33,
    ram_addr=CRRawData(0x803BFBAB, bit_position=1)
  ),
  "Use Chickenheart": CRLocationData(
    code=34,
    ram_addr=CRRawData(0x803BFBAB, bit_position=2)
  ),
}

# Each battle counts as a check
BATTLE_COUNTER: dict[str, CRLocationData] = {
  "Battles Won": CRLocationData(
    name="Battles",
    code=???,
    ram_addr=CRRawData(0x803BE7A7, ram_byte_size=7)
  )
}



LOCATION_TABLE: dict[str, CRLocationData] = {
  **PART_USE,
  **BATTLE_COUNTER
}
