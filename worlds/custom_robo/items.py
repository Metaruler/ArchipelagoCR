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
    )
  ]
}

PARTS_ITEM_TABLE: dict[str, CRItemData] = {
  "Ray 01": CRItemData(
    type="Body",
    code=18,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9F, bit_position=1)]
  ),
  "Splendor": CRItemData(
    type="Body",
    code=19,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9F, bit_position=2)]
  ),
  "Glory": CRItemData(
    type="Body",
    code=20,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9F, bit_position=3)]
  ),
  "Milky Way": CRItemData(
    type="Body",
    code=21,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9F, bit_position=4)]
  ),
  "Earth": CRItemData(
    type="Body",
    code=22,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9F, bit_position=5)]
  ),
  "Sol": CRItemData(
    type="Body",
    code=23,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9F, bit_position=6)]
  ),
  "Metal Ape": CRItemData(
    type="Body",
    code=24,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9F, bit_position=7)]
  ),
  "Metal Bear": CRItemData(
    type="Body",
    code=25,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9F, bit_position=8)]
  ),
  "Metal Ox": CRItemData(
    type="Body",
    code=26,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9E, bit_position=1)]
  ),
  "Swift": CRItemData(
    type="Body",
    code=27,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9E, bit_position=2)]
  ),
  "Shrike": CRItemData(
    type="Body",
    code=28,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9E, bit_position=3)]
  ),
  "Peregrine": CRItemData(
    type="Body",
    code=29,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9E, bit_position=4)]
  ),
  "Javelin": CRItemData(
    type="Body",
    code=30,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9E, bit_position=5)]
  ),
  "Glaive": CRItemData(
    type="Body",
    code=31,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9E, bit_position=6)]
  ),
  "Halberd": CRItemData(
    type="Body",
    code=32,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9E, bit_position=7)]
  ),
  "Criminal": CRItemData(
    type="Body",
    code=33,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9E, bit_position=8)]
  ),
  "Buggy": CRItemData(
    type="Body",
    code=34,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9D, bit_position=1)]
  ),
  "Juggler": CRItemData(
    type="Body",
    code=35,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9D, bit_position=2)]
  ),
  "Defender": CRItemData(
    type="Body",
    code=36,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9D, bit_position=3)]
  ),
  "Seeker": CRItemData(
    type="Body",
    code=37,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9D, bit_position=4)]
  ),
  "Breaker": CRItemData(
    type="Body",
    code=38,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9D, bit_position=5)]
  ),
  "Seal Head": CRItemData(
    type="Body",
    code=39,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9D, bit_position=6)]
  ),
  "Dour Head": CRItemData(
    type="Body",
    code=40,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9D, bit_position=7)]
  ),
  "Tank Head": CRItemData(
    type="Body",
    code=41,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9D, bit_position=8)]
  ),
  "Ray Legend": CRItemData(
    type="Body",
    code=42,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9C, bit_position=1)]
  ),
  "Oil Can": CRItemData(
    type="Body",
    code=43,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9C, bit_position=2)]
  ),
  "Ray Warrior": CRItemData(
    type="Body",
    code=44,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9C, bit_position=3)]
  ),
  "Rakansen": CRItemData(
    type="Body",
    code=45,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9C, bit_position=4)]
  ),
  "Ruhiel": CRItemData(
    type="Body",
    code=46,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9C, bit_position=5)]
  ),
  "Athena": CRItemData(
    type="Body",
    code=47,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9C, bit_position=6)]
  ),
  "Rahu I": CRItemData(
    type="Body",
    code=48,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9C, bit_position=7)]
  ),
  "Rahu II": CRItemData(
    type="Body",
    code=44,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9C, bit_position=3)]
  ),
}

PROGRESSION_RAHU_BODY: dict[str, CRItemData] = {
  "Rahu Body Upgrade": [
    CRItemData(
      type="Rahu I",
      code=1,
      classification=IC.progression,
      item_id=1,
      update_ram_addr=None
    ),
    CRItemData(
      type="Rahu II",
      code=2,
      classification=IC.progression,
      item_id=2,
      update_ram_addr=None
    ),
    CRItemData(
      type="Rahu III",
      code=3,
      classification=IC.progression,
      item_id=3,
      update_ram_addr=None
    )
  ]
}

ALL_ITEMS_TABLE = {
  **PROGRESSION_SCENARIO_TABLE,
  **PARTS_ITEM_TABLE
  **PROGRESSION_RAHU_BODY
}
