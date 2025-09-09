#Checks
from typing import NamedTuple, Dict, Optional
from .Items import CRItemData
from .Helpers import CRRawData

class CRLocationData(NamedTuple):
  name:str
  code:Optional[int]
  ram_addr: Optional[CRRawData] = None

# Begin check logic
BATTLE_COUNTER: dict[str, CRLocationData] = {
  "Battles Won": CRLocationData(
    name="Battle 1",
    code=1,
    ram_addr=CRRawData(0x803BE7A7, ram_byte_size=7)
  )
}
