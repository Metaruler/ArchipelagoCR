from typing import NamedTuple, Dict, Optional, Set

from BaseClasses import Item
from BaseClasses import ItemClassification as IC

# Item Class
class CRItemData(NamedTuple):
  type: str
  code: Optional[int]
  classification: IC
  update_ram_addr: Optional[list[CRRawData]] = None

# Begin item list for AP
PROGRESSION_ITEM_TABLE: dict[str, CRItemData] = {
  "Progressive Scenario": CRItemData(
    type="Key Item",
    code=1,
    classification=IC.progression,
    update_ram_addr=None
  )
}

PARTS_ITEM_TABLE: dict[str, CRItemData] = {
  "Ray 01": CRItemData(
    type="Body",
    code=2,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9F, bit_position=1)]
  )
}

ALL_ITEMS_TABLE = {
  **PROGRESSION_ITEM_TABLE,
  **PARTS_ITEM_TABLE
}
