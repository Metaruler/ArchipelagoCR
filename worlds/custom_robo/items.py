from typing import NamedTuple, Dict, Optional, Set

from BaseClasses import Item
from BaseClasses import ItemClassification as IC

# Item Class
class CRItemData(NamedTuple):
  type: str
  code: Optional[int]
  classification: IC
  item_id: Optional[int] = None # Unique ID for item
  update_ram_addr: Optional[list[CRRawData]] = None

# Begin item list for AP
PROGRESSION_SCENARIO_TABLE: dict[str, CRItemData] = {
  "Progressive Scenario": [
    CRItemData(
      type="Chapter",
      code=1,
      classification=IC.progression,
      item_id=1,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=2,
      classification=IC.progression,
      item_id=2,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=3,
      classification=IC.progression,
      item_id=3,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=4,
      classification=IC.progression,
      item_id=4,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=5,
      classification=IC.progression,
      item_id=5,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=6,
      classification=IC.progression,
      item_id=6,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=7,
      classification=IC.progression,
      item_id=7,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=8,
      classification=IC.progression,
      item_id=8,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=9,
      classification=IC.progression,
      item_id=9,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=10,
      classification=IC.progression,
      item_id=10,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=11,
      classification=IC.progression,
      item_id=11,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=12,
      classification=IC.progression,
      item_id=12,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=13,
      classification=IC.progression,
      item_id=13,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=14,
      classification=IC.progression,
      item_id=14,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=15,
      classification=IC.progression,
      item_id=15,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=16,
      classification=IC.progression,
      item_id=16,
      update_ram_addr=None
    ),
    CRItemData(
      type="Chapter",
      code=17,
      classification=IC.progression,
      item_id=17,
      update_ram_addr=None
    ),
  ]
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
  **PROGRESSION_SCENARIO_TABLE,
  **PARTS_ITEM_TABLE
}
