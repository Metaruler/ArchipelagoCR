#Checks
from typing import NamedTuple, Dict, Optional
from .Items import CRItemData
from .Helpers import CRRawData

class CRLocationData(NamedTuple):
  game:str = "Custom Robo"
  code:Optional[int]
  ram_addr: Optional[CRRawData] = None

# Begin check logic
# Each battle counts as a check
BATTLE_COUNTER: dict[str, CRLocationData] = {
  "Battles Won": CRLocationData(
    name="Battles",
    code=1,
    ram_addr=CRRawData(0x803BE7A7, ram_byte_size=7)
  )
}

# Check for each part being used in a victory
PART_USE: dict[str, CRLocationData] = {
  "Use Ray 01": CRLocationData(
    name="Battles",
    code=2,
    ram_addr=CRRawData(0x803BE7A7, ram_byte_size=7)
  )
}



LOCATION_TABLE: dict[str, CRLocationData] = {
  **BATTLE_COUNTER,
  **PART_USE
}
