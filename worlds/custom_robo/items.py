from typing import NamedTuple, Dict, Optional, Set

from BaseClasses import Item
from BaseClasses import ItemClassification as IC

# Item Class
class CRItemData(NamedTuple):
  name: Optional[str] = None
  type: str
  code: Optional[int]
  classification: IC
  item_id: Optional[int] = None # Unique ID for item
  update_ram_addr: Optional[list[CRRawData]] = None

# Begin item list for AP
# Scenario progression gates needed to move to next chapter
PROGRESSION_SCENARIO_TABLE: dict[str, CRItemData] = {
  "Progressive Scenario": [
    CRItemData(
      name="Chapter 1",
      type="Chapter",
      code=1,
      classification=IC.progression,
      item_id=1,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 2",
      type="Chapter",
      code=2,
      classification=IC.progression,
      item_id=2,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 3",
      type="Chapter",
      code=3,
      classification=IC.progression,
      item_id=3,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 4",
      type="Chapter",
      code=4,
      classification=IC.progression,
      item_id=4,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 5",
      type="Chapter",
      code=5,
      classification=IC.progression,
      item_id=5,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 6",
      type="Chapter",
      code=6,
      classification=IC.progression,
      item_id=6,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 7",
      type="Chapter",
      code=7,
      classification=IC.progression,
      item_id=7,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 8",
      type="Chapter",
      code=8,
      classification=IC.progression,
      item_id=8,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 9",
      type="Chapter",
      code=9,
      classification=IC.progression,
      item_id=9,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 10",
      type="Chapter",
      code=10,
      classification=IC.progression,
      item_id=10,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 11",
      type="Chapter",
      code=11,
      classification=IC.progression,
      item_id=11,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 12",
      type="Chapter",
      code=12,
      classification=IC.progression,
      item_id=12,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 13",
      type="Chapter",
      code=13,
      classification=IC.progression,
      item_id=13,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 14",
      type="Chapter",
      code=14,
      classification=IC.progression,
      item_id=14,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 15",
      type="Chapter",
      code=15,
      classification=IC.progression,
      item_id=15,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 16",
      type="Chapter",
      code=16,
      classification=IC.progression,
      item_id=16,
      update_ram_addr=None
    ),
    CRItemData(
      name="Chapter 17",
      type="Chapter",
      code=17,
      classification=IC.progression,
      item_id=17,
      update_ram_addr=None
    )
  ]
}

# Full parts table minus Rahu
PARTS_ITEM_TABLE: dict[str, CRItemData] = {
  # Body Parts
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
    type="Illegal Body",
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
    type="Illegal Body",
    code=44,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9C, bit_position=3)]
  ),
  "Rakansen": CRItemData(
    type="Illegal Body",
    code=45,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9C, bit_position=4)]
  ),
  "Ruhiel": CRItemData(
    type="Illegal Body",
    code=46,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9C, bit_position=5)]
  ),
  "Athena": CRItemData(
    type="Illegal Body",
    code=47,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFB9C, bit_position=6)]
  ),
  "Chickenheart": CRItemData(
    type="Body",
    code=48,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBA3, bit_position=2)]
  ),
  
  # Gun Parts
  "Basic": CRItemData(
    type="Gun",
    code=49,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBF, bit_position=1)]
  ),
  "3-Way": CRItemData(
    type="Gun",
    code=50,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBF, bit_position=2)]
  ),
  "Gatling": CRItemData(
    type="Gun",
    code=51,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBF, bit_position=3)]
  ),
  "Vertical": CRItemData(
    type="Gun",
    code=52,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBF, bit_position=4)]
  ),
  "Sniper": CRItemData(
    type="Gun",
    code=53,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBF, bit_position=5)]
  ),
  "Stun": CRItemData(
    type="Gun",
    code=54,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBF, bit_position=6)]
  ),
  "Hornet": CRItemData(
    type="Gun",
    code=55,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBF, bit_position=7)]
  ),
  "Flame": CRItemData(
    type="Gun",
    code=56,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBF, bit_position=8)]
  ),
  "Dragon": CRItemData(
    type="Gun",
    code=57,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBE, bit_position=1)]
  ),
  "Splash": CRItemData(
    type="Gun",
    code=58,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBE, bit_position=2)]
  ),
  "Left Arc": CRItemData(
    type="Gun",
    code=59,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBE, bit_position=3)]
  ),
  "Right Arc": CRItemData(
    type="Gun",
    code=60,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBE, bit_position=4)]
  ),
  "Shotgun": CRItemData(
    type="Gun",
    code=61,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBE, bit_position=5)]
  ),
  "Rayfall": CRItemData(
    type="Gun",
    code=62,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBE, bit_position=6)]
  ),
  "Bubble": CRItemData(
    type="Gun",
    code=63,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBE, bit_position=7)]
  ),
  "Eagle": CRItemData(
    type="Gun",
    code=64,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBE, bit_position=8)]
  ),
  "V Laser": CRItemData(
    type="Gun",
    code=65,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBD, bit_position=1)]
  ),
  "Magnum": CRItemData(
    type="Gun",
    code=66,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBD, bit_position=2)]
  ),
  "Needle": CRItemData(
    type="Gun",
    code=67,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBD, bit_position=3)]
  ),
  "Starshot": CRItemData(
    type="Gun",
    code=68,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBD, bit_position=4)]
  ),
  "Glider": CRItemData(
    type="Gun",
    code=69,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBD, bit_position=5)]
  ),
  "Homing Star": CRItemData(
    type="Gun",
    code=70,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBD, bit_position=6)]
  ),
  "Trap": CRItemData(
    type="Gun",
    code=71,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBD, bit_position=7)]
  ),
  "Drill": CRItemData(
    type="Gun",
    code=72,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBD, bit_position=8)]
  ),
  "Titan Gun": CRItemData(
    type="Gun",
    code=73,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBC, bit_position=1)]
  ),
  "Claw": CRItemData(
    type="Gun",
    code=74,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBC, bit_position=2)]
  ),
  "Knuckle": CRItemData(
    type="Gun",
    code=75,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBC, bit_position=3)]
  ),
  "Afterburner": CRItemData(
    type="Gun",
    code=76,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBC, bit_position=4)]
  ),
  "Blade": CRItemData(
    type="Gun",
    code=77,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBC, bit_position=5)]
  ),
  "Meteor Storm": CRItemData(
    type="Gun",
    code=78,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBC, bit_position=6)]
  ),
  "Twin Fang": CRItemData(
    type="Gun",
    code=79,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBC, bit_position=7)]
  ),
  "Gravity": CRItemData(
    type="Gun",
    code=80,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBBC, bit_position=8)]
  ),
  "Phoenix": CRItemData(
    type="Gun",
    code=81,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC3, bit_position=1)]
  ),
  "Can Gun": CRItemData(
    type="Gun",
    code=82,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC3, bit_position=2)]
  ),
  "Left Pulse": CRItemData(
    type="Gun",
    code=83,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC3, bit_position=3)]
  ),
  "Right Pulse": CRItemData(
    type="Gun",
    code=84,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC3, bit_position=4)]
  ),
  "Sword Storm": CRItemData(
    type="Gun",
    code=85,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC3, bit_position=5)]
  ),
  "Ion": CRItemData(
    type="Gun",
    code=86,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC3, bit_position=6)]
  ),
  "Flare": CRItemData(
    type="Gun",
    code=87,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC3, bit_position=7)]
  ),
  "Left 5-Way": CRItemData(
    type="Gun",
    code=88,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC3, bit_position=8)]
  ),
  "Right 5-Way": CRItemData(
    type="Gun",
    code=89,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC2, bit_position=1)]
  ),
  "Halo": CRItemData(
    type="Gun",
    code=90,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC2, bit_position=2)]
  ),
  "Wave Laser": CRItemData(
    type="Illegal Gun",
    code=91,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC2, bit_position=3)]
  ),
  "X Laser": CRItemData(
    type="Illegal Gun",
    code=92,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC2, bit_position=4)]
  ),
  "Crystal Strike": CRItemData(
    type="Illegal Gun",
    code=93,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC2, bit_position=5)]
  ),
  "Wyrm": CRItemData(
    type="Illegal Gun",
    code=94,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC2, bit_position=6)]
  ),
  "Raptor": CRItemData(
    type="Illegal Gun",
    code=95,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC2, bit_position=7)]
  ),
  "Waxing Arc Gun": CRItemData(
    type="Illegal Gun",
    code=96,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC2, bit_position=8)]
  ),
  "Waning Arc Gun": CRItemData(
    type="Illegal Gun",
    code=97,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBC1, bit_position=1)]
  ),
  
  # Bomb Parts
  "Standard Bomb": CRItemData(
    type="Bomb",
    code=98,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDF, bit_position=1)]
  ),
  "Standard F": CRItemData(
    type="Bomb",
    code=99,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDF, bit_position=2)]
  ),
  "Standard S": CRItemData(
    type="Bomb",
    code=100,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDF, bit_position=3)]
  ),
  "Wave Bomb": CRItemData(
    type="Bomb",
    code=101,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDF, bit_position=4)]
  ),
  "Straight G": CRItemData(
    type="Bomb",
    code=102,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDF, bit_position=5)]
  ),
  "Straight S": CRItemData(
    type="Bomb",
    code=103,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDF, bit_position=6)]
  ),
  "Straight T": CRItemData(
    type="Bomb",
    code=104,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDF, bit_position=7)]
  ),
  "Right Flank H": CRItemData(
    type="Bomb",
    code=105,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDF, bit_position=8)]
  ),
  "Left Flank H": CRItemData(
    type="Bomb",
    code=106,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDE, bit_position=1)]
  ),
  "Right Wave": CRItemData(
    type="Bomb",
    code=107,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDE, bit_position=2)]
  ),
  "Left Wave": CRItemData(
    type="Bomb",
    code=108,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDE, bit_position=3)]
  ),
  "Burrow D": CRItemData(
    type="Bomb",
    code=109,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDE, bit_position=4)]
  ),
  "Burrow P": CRItemData(
    type="Bomb",
    code=110,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDE, bit_position=5)]
  ),
  "Freeze": CRItemData(
    type="Bomb",
    code=111,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDE, bit_position=6)]
  ),
  "Tomahawk B": CRItemData(
    type="Bomb",
    code=112,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDE, bit_position=7)]
  ),
  "Tomahawk G": CRItemData(
    type="Bomb",
    code=113,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDE, bit_position=8)]
  ),
  "Gemini B": CRItemData(
    type="Bomb",
    code=114,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDD, bit_position=1)]
  ),
  "Gemini P": CRItemData(
    type="Bomb",
    code=115,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDD, bit_position=2)]
  ),
  "Submarine D": CRItemData(
    type="Bomb",
    code=116,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDD, bit_position=3)]
  ),
  "Submarine P": CRItemData(
    type="Bomb",
    code=117,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDD, bit_position=4)]
  ),
  "Crescent P": CRItemData(
    type="Bomb",
    code=118,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDD, bit_position=5)]
  ),
  "Crescent C": CRItemData(
    type="Bomb",
    code=119,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDD, bit_position=6)]
  ),
  "Dual": CRItemData(
    type="Bomb",
    code=120,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDD, bit_position=7)]
  ),
  "Dual C": CRItemData(
    type="Bomb",
    code=121,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDD, bit_position=8)]
  ),
  "Acrobat": CRItemData(
    type="Bomb",
    code=122,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDC, bit_position=1)]
  ),
  "Delta": CRItemData(
    type="Bomb",
    code=123,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDC, bit_position=2)]
  ),
  "Wall Bomb": CRItemData(
    type="Bomb",
    code=124,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDC, bit_position=3)]
  ),
  "Smash": CRItemData(
    type="Bomb",
    code=125,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDC, bit_position=4)]
  ),
  "Double Mine": CRItemData(
    type="Bomb",
    code=126,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDC, bit_position=5)]
  ),
  "Geo Trap": CRItemData(
    type="Bomb",
    code=127,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDC, bit_position=6)]
  ),
  "Titan Bomb": CRItemData(
    type="Bomb",
    code=128,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDC, bit_position=7)]
  ),
  "Can Bomb": CRItemData(
    type="Bomb",
    code=129,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBDC, bit_position=8)]
  ),
  "Standard K": CRItemData(
    type="Bomb",
    code=130,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBE3, bit_position=1)]
  ),
  "Submarine K": CRItemData(
    type="Bomb",
    code=131,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBE3, bit_position=2)]
  ),
  "Crescent K": CRItemData(
    type="Bomb",
    code=132,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBE3, bit_position=3)]
  ),
  "Standard X": CRItemData(
    type="Bomb",
    code=133,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBE3, bit_position=4)]
  ),
  "Treble": CRItemData(
    type="Bomb",
    code=134,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBE3, bit_position=5)]
  ),
  "Wyvern": CRItemData(
    type="Bomb",
    code=135,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBE3, bit_position=6)]
  ),
  "Waxing Arc Bomb": CRItemData(
    type="Bomb",
    code=136,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBE3, bit_position=7)]
  ),
  "Waning Arc Bomb": CRItemData(
    type="Bomb",
    code=137,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBE3, bit_position=8)]
  ),

  #Pod Parts
  "Standard Pod": CRItemData(
    type="Pod",
    code=138,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFF, bit_position=1)]
  ),
  "Seeker F": CRItemData(
    type="Pod",
    code=139,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFF, bit_position=2)]
  ),
  "Seeker G": CRItemData(
    type="Pod",
    code=140,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFF, bit_position=3)]
  ),
  "Speed D": CRItemData(
    type="Pod",
    code=141,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFF, bit_position=4)]
  ),
  "Speed P": CRItemData(
    type="Pod",
    code=142,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFF, bit_position=5)]
  ),
  "Cockroach G": CRItemData(
    type="Pod",
    code=143,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFF, bit_position=6)]
  ),
  "Cockroach H": CRItemData(
    type="Pod",
    code=144,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFF, bit_position=7)]
  ),
  "Dolphin": CRItemData(
    type="Pod",
    code=145,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFF, bit_position=8)]
  ),
  "Dolphin G": CRItemData(
    type="Pod",
    code=146,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFE, bit_position=1)]
  ),
  "Spider": CRItemData(
    type="Pod",
    code=147,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFE, bit_position=2)]
  ),
  "Spider G": CRItemData(
    type="Pod",
    code=148,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFE, bit_position=3)]
  ),
  "Sky Freeze": CRItemData(
    type="Pod",
    code=149,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFE, bit_position=4)]
  ),
  "Ground Freeze": CRItemData(
    type="Pod",
    code=150,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFE, bit_position=5)]
  ),
  "Feint F": CRItemData(
    type="Pod",
    code=151,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFE, bit_position=6)]
  ),
  "Feint G": CRItemData(
    type="Pod",
    code=152,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFE, bit_position=7)]
  ),
  "Float F": CRItemData(
    type="Pod",
    code=153,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFE, bit_position=8)]
  ),
  "Jumping B": CRItemData(
    type="Pod",
    code=154,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFD, bit_position=1)]
  ),
  "Jumping G": CRItemData(
    type="Pod",
    code=155,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFD, bit_position=2)]
  ),
  "Diving": CRItemData(
    type="Pod",
    code=156,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFD, bit_position=3)]
  ),
  "Wave Pod": CRItemData(
    type="Pod",
    code=157,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFD, bit_position=4)]
  ),
  "Satellite": CRItemData(
    type="Pod",
    code=158,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFD, bit_position=5)]
  ),
  "Satellite H": CRItemData(
    type="Pod",
    code=159,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFD, bit_position=6)]
  ),
  "Beast F": CRItemData(
    type="Pod",
    code=160,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFD, bit_position=7)]
  ),
  "Trio H": CRItemData(
    type="Pod",
    code=161,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFD, bit_position=8)]
  ),
  "Wall Pod": CRItemData(
    type="Pod",
    code=162,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFC, bit_position=1)]
  ),
  "Reflection": CRItemData(
    type="Pod",
    code=163,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFC, bit_position=2)]
  ),
  "Caboose C": CRItemData(
    type="Pod",
    code=164,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFC, bit_position=3)]
  ),
  "Caboose T": CRItemData(
    type="Pod",
    code=165,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFC, bit_position=4)]
  ),
  "Twin Flank F": CRItemData(
    type="Pod",
    code=166,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFC, bit_position=5)]
  ),
  "Twin Flank G": CRItemData(
    type="Pod",
    code=167,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFC, bit_position=6)]
  ),
  "Umbrella": CRItemData(
    type="Pod",
    code=168,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFC, bit_position=7)]
  ),
  "Throwing D": CRItemData(
    type="Pod",
    code=169,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFBFC, bit_position=8)]
  ),
  "Throwing P": CRItemData(
    type="Pod",
    code=170,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC03, bit_position=1)]
  ),
  "Double Wave": CRItemData(
    type="Pod",
    code=171,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC03, bit_position=2)]
  ),
  "Titan Pod": CRItemData(
    type="Pod",
    code=172,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC03, bit_position=3)]
  ),
  "Can Pod": CRItemData(
    type="Pod",
    code=173,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC03, bit_position=4)]
  ),
  "Standard F": CRItemData(
    type="Pod",
    code=174,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC03, bit_position=5)]
  ),
  "Caboose X": CRItemData(
    type="Pod",
    code=175,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC03, bit_position=6)]
  ),
  "Cheetah": CRItemData(
    type="Illegal Pod",
    code=176,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC03, bit_position=7)]
  ),
  "Wolf Spider": CRItemData(
    type="Illegal Pod",
    code=177,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC03, bit_position=8)]
  ),
  "Orca": CRItemData(
    type="Illegal Pod",
    code=178,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC02, bit_position=1)]
  ),

  # Leg Parts
  "Standard Leg": CRItemData(
    type="Leg",
    code=179,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1F, bit_position=1)]
  ),
  "High Jump": CRItemData(
    type="Leg",
    code=180,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1F, bit_position=2)]
  ),
  "Ground": CRItemData(
    type="Leg",
    code=181,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1F, bit_position=3)]
  ),
  "Formula": CRItemData(
    type="Leg",
    code=182,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1F, bit_position=4)]
  ),
  "Stabilizer": CRItemData(
    type="Leg",
    code=183,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1F, bit_position=5)]
  ),
  "Short Thrust": CRItemData(
    type="Leg",
    code=184,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1F, bit_position=6)]
  ),
  "Long Thrust": CRItemData(
    type="Leg",
    code=185,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1F, bit_position=7)]
  ),
  "Quick Jump": CRItemData(
    type="Leg",
    code=186,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1F, bit_position=8)]
  ),
  "Feather": CRItemData(
    type="Leg",
    code=187,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1E, bit_position=1)]
  ),
  "Wide Jump": CRItemData(
    type="Leg",
    code=188,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1E, bit_position=2)]
  ),
  "Can Leg": CRItemData(
    type="Leg",
    code=189,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1E, bit_position=3)]
  ),
  "Booster": CRItemData(
    type="Leg",
    code=190,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1E, bit_position=4)]
  ),
  "Swallow": CRItemData(
    type="Illegal Leg",
    code=191,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1E, bit_position=5)]
  ),
  "Raven": CRItemData(
    type="Illegal Leg",
    code=192,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1E, bit_position=6)]
  ),
  "Eclipse": CRItemData(
    type="Illegal Leg",
    code=193,
    classification=IC.useful,
    update_ram_addr=[CRRawData(0x803BFC1E, bit_position=7)]
  )
}

# Rahu evolution table
PROGRESSION_RAHU: dict[str, list[CRItemData]] = {
  "Rahu Body Upgrade": [
    CRItemData(
      name="Rahu I",
      type="Rahu Part",
      code=194,
      classification=IC.useful,
      update_ram_addr=[CRRawData(0x803BFB9C, bit_position=7)]
    ),
    CRItemData(
      name="Penumbra I Pod",
      type="Rahu Part",
      code=195,
      classification=IC.useful,
      update_ram_addr=[CRRawData(0x803BFC02, bit_position=2)]
    ),
    CRItemData(
      name="Rahu I Gun",
      type="Rahu Part",
      code=196,
      classification=IC.useful,
      update_ram_addr=[CRRawData(0x803BFBC1, bit_position=2)]
    ),
    CRItemData(
      name="Rahu II",
      type="Rahu Part",
      code=197,
      classification=IC.useful,
      update_ram_addr=[CRRawData(0x803BFB9C, bit_position=8)]
    ),
    CRItemData(
      name="Penumbra II Pod",
      type="Rahu Part",
      code=198,
      classification=IC.useful,
      update_ram_addr=[CRRawData(0x803BFC02, bit_position=3)]
    ),
    CRItemData(
      name="Rahu II Gun",
      type="Rahu Part",
      code=199,
      classification=IC.useful,
      update_ram_addr=[CRRawData(0x803BFBC1, bit_position=3)]
    ),
    CRItemData(
      name="Grand Cross Bomb",
      type="Rahu Part",
      code=200,
      classification=IC.useful,
      update_ram_addr=[CRRawData(0x803BFBE2, bit_position=1)]
    ),
    CRItemData(
      name="Ultimate Legs",
      type="Rahu Part",
      code=201,
      classification=IC.useful,
      update_ram_addr=[CRRawData(0x803BFC1E, bit_position=1)]
    ),
    CRItemData(
      name="Rahu III",
      type="Rahu Part",
      code=202,
      classification=IC.useful,
      update_ram_addr=[CRRawData(0x803BFBA3, bit_position=1)]
    ),
    CRItemData(
      name="Penumbra III Pod",
      type="Rahu Part",
      code=203,
      classification=IC.useful,
      update_ram_addr=[CRRawData(0x803BFC02, bit_position=4)]
    ),
    CRItemData(
      name="Rahu III Gun",
      type="Rahu Part",
      code=204,
      classification=IC.useful,
      update_ram_addr=[CRRawData(0x803BFBC1, bit_position=4)]
    ),
  ]
}

ALL_ITEMS_TABLE = {
  **PROGRESSION_SCENARIO_TABLE,
  **PARTS_ITEM_TABLE,
  **PROGRESSION_RAHU
}
