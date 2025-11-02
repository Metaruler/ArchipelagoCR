from typing import NamedTuple, Optional

from BaseClasses import Item
from BaseClasses import ItemClassification as IC
from .helpers import CRRamData


# Item Class
class CRItemData(NamedTuple):
  type: str
  code: Optional[int]
  classification: IC
  name: Optional[str] = None
  item_id: Optional[int] = None # Unique ID for item
  update_ram_addr: Optional[list[CRRamData]] = None
  illegal: bool = False

class CRItem(Item):
  game: str = "Custom Robo"
# doorid: Optional[int] = None

  def __init__(self, name: str, player: int, data: CRItemData, force_nonprogress: bool = False):
      adjusted_classification = IC.filler if force_nonprogress else data.classification
      super(CRItem, self).__init__(name, adjusted_classification, CRItem.get_apid(data.code), player)

      self.type = data.type
      self.item_id = data.code

  @staticmethod
  def get_apid(code: int):
      base_id: int = 8000
      return base_id + code if code is not None else None

# Begin item list for AP
# Scenario progression gates needed to move to next chapter
#PROGRESSION_SCENARIO_TABLE: dict[str, CRItemData] = {
#  "Progressive Scenario": [
#    CRItemData(
#      name="Chapter 1",
#      type="Chapter",
#      code=1,
#      classification=IC.progression,
#      item_id=1,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 2",
#      type="Chapter",
#      code=2,
#      classification=IC.progression,
#      item_id=2,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 3",
#      type="Chapter",
#      code=3,
#      classification=IC.progression,
#      item_id=3,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 4",
#      type="Chapter",
#      code=4,
#      classification=IC.progression,
#      item_id=4,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 5",
#      type="Chapter",
#      code=5,
#      classification=IC.progression,
#      item_id=5,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 6",
#      type="Chapter",
#      code=6,
#      classification=IC.progression,
#      item_id=6,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 7",
#      type="Chapter",
#      code=7,
#      classification=IC.progression,
#      item_id=7,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 8",
#      type="Chapter",
#      code=8,
#      classification=IC.progression,
#      item_id=8,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 9",
#      type="Chapter",
#      code=9,
#      classification=IC.progression,
#      item_id=9,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 10",
#      type="Chapter",
#      code=10,
#      classification=IC.progression,
#      item_id=10,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 11",
#      type="Chapter",
#      code=11,
#      classification=IC.progression,
#      item_id=11,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 12",
#      type="Chapter",
#      code=12,
#      classification=IC.progression,
#      item_id=12,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 13",
#      type="Chapter",
#      code=13,
#      classification=IC.progression,
#      item_id=13,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 14",
#      type="Chapter",
#      code=14,
#      classification=IC.progression,
#      item_id=14,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 15",
#      type="Chapter",
#      code=15,
#      classification=IC.progression,
#      item_id=15,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 16",
#      type="Chapter",
#      code=16,
#      classification=IC.progression,
#      item_id=16,
#      update_ram_addr=None
#    ),
#    CRItemData(
#      name="Chapter 17",
#      type="Chapter",
#      code=17,
#      classification=IC.progression,
#      item_id=17,
#      update_ram_addr=None
#    )
#  ]
#}

# Full parts table minus Rahu
PARTS_ITEM_TABLE: dict[str, CRItemData] = {
  # Body Parts
  "Ray 01": CRItemData(
    type="Body",
    code=18,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9F, bit_position=0)]
  ),
  "Splendor": CRItemData(
    type="Body",
    code=19,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9F, bit_position=1)]
  ),
  "Glory": CRItemData(
    type="Body",
    code=20,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9F, bit_position=2)]
  ),
  "Milky Way": CRItemData(
    type="Body",
    code=21,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9F, bit_position=3)]
  ),
  "Earth": CRItemData(
    type="Body",
    code=22,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9F, bit_position=4)]
  ),
  "Sol": CRItemData(
    type="Body",
    code=23,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9F, bit_position=5)]
  ),
  "Metal Ape": CRItemData(
    type="Body",
    code=24,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9F, bit_position=6)]
  ),
  "Metal Bear": CRItemData(
    type="Body",
    code=25,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9F, bit_position=7)]
  ),
  "Metal Ox": CRItemData(
    type="Body",
    code=26,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9E, bit_position=0)]
  ),
  "Swift": CRItemData(
    type="Body",
    code=27,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9E, bit_position=1)]
  ),
  "Shrike": CRItemData(
    type="Body",
    code=28,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9E, bit_position=2)]
  ),
  "Peregrine": CRItemData(
    type="Body",
    code=29,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9E, bit_position=3)]
  ),
  "Javelin": CRItemData(
    type="Body",
    code=30,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9E, bit_position=4)]
  ),
  "Glaive": CRItemData(
    type="Body",
    code=31,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9E, bit_position=5)]
  ),
  "Halberd": CRItemData(
    type="Body",
    code=32,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9E, bit_position=6)]
  ),
  "Criminal": CRItemData(
    type="Body",
    code=33,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9E, bit_position=7)]
  ),
  "Buggy": CRItemData(
    type="Body",
    code=34,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9D, bit_position=0)]
  ),
  "Juggler": CRItemData(
    type="Body",
    code=35,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9D, bit_position=1)]
  ),
  "Defender": CRItemData(
    type="Body",
    code=36,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9D, bit_position=2)]
  ),
  "Seeker": CRItemData(
    type="Body",
    code=37,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9D, bit_position=3)]
  ),
  "Breaker": CRItemData(
    type="Body",
    code=38,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9D, bit_position=4)]
  ),
  "Seal Head": CRItemData(
    type="Body",
    code=39,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9D, bit_position=5)]
  ),
  "Dour Head": CRItemData(
    type="Body",
    code=40,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9D, bit_position=6)]
  ),
  "Tank Head": CRItemData(
    type="Body",
    code=41,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9D, bit_position=7)]
  ),
  "Ray Legend": CRItemData(
    type="Body",
    code=42,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9C, bit_position=0)],
    illegal=True
  ),
  "Oil Can": CRItemData(
    type="Body",
    code=43,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9C, bit_position=1)]
  ),
  "Ray Warrior": CRItemData(
    type="Body",
    code=44,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9C, bit_position=2)],
    illegal=True
  ),
  "Rakansen": CRItemData(
    type="Body",
    code=45,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9C, bit_position=3)],
    illegal=True
  ),
  "Ruhiel": CRItemData(
    type="Body",
    code=46,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9C, bit_position=4)],
    illegal=True
  ),
  "Athena": CRItemData(
    type="Body",
    code=47,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFB9C, bit_position=5)],
    illegal=True
  ),
  "Chickenheart": CRItemData(
    type="Body",
    code=48,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBA3, bit_position=1)]
  ),
  
  # Gun Parts
  "Basic Gun": CRItemData(
    type="Gun",
    code=49,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBF, bit_position=0)]
  ),
  "3-Way Gun": CRItemData(
    type="Gun",
    code=50,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBF, bit_position=1)]
  ),
  "Gatling Gun": CRItemData(
    type="Gun",
    code=51,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBF, bit_position=2)]
  ),
  "Vertical Gun": CRItemData(
    type="Gun",
    code=52,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBF, bit_position=3)]
  ),
  "Sniper Gun": CRItemData(
    type="Gun",
    code=53,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBF, bit_position=4)]
  ),
  "Stun Gun": CRItemData(
    type="Gun",
    code=54,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBF, bit_position=5)]
  ),
  "Hornet Gun": CRItemData(
    type="Gun",
    code=55,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBF, bit_position=6)]
  ),
  "Flame Gun": CRItemData(
    type="Gun",
    code=56,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBF, bit_position=7)]
  ),
  "Dragon Gun": CRItemData(
    type="Gun",
    code=57,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBE, bit_position=0)]
  ),
  "Splash Gun": CRItemData(
    type="Gun",
    code=58,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBE, bit_position=1)]
  ),
  "Left Arc Gun": CRItemData(
    type="Gun",
    code=59,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBE, bit_position=2)]
  ),
  "Right Arc Gun": CRItemData(
    type="Gun",
    code=60,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBE, bit_position=3)]
  ),
  "Shotgun Gun": CRItemData(
    type="Gun",
    code=61,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBE, bit_position=4)]
  ),
  "Rayfall Gun": CRItemData(
    type="Gun",
    code=62,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBE, bit_position=5)]
  ),
  "Bubble Gun": CRItemData(
    type="Gun",
    code=63,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBE, bit_position=6)]
  ),
  "Eagle Gun": CRItemData(
    type="Gun",
    code=64,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBE, bit_position=7)]
  ),
  "V Laser Gun": CRItemData(
    type="Gun",
    code=65,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBD, bit_position=0)]
  ),
  "Magnum Gun": CRItemData(
    type="Gun",
    code=66,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBD, bit_position=1)]
  ),
  "Needle Gun": CRItemData(
    type="Gun",
    code=67,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBD, bit_position=2)]
  ),
  "Starshot Gun": CRItemData(
    type="Gun",
    code=68,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBD, bit_position=3)]
  ),
  "Glider Gun": CRItemData(
    type="Gun",
    code=69,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBD, bit_position=4)]
  ),
  "Homing Star Gun": CRItemData(
    type="Gun",
    code=70,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBD, bit_position=5)]
  ),
  "Trap Gun": CRItemData(
    type="Gun",
    code=71,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBD, bit_position=6)]
  ),
  "Drill Gun": CRItemData(
    type="Gun",
    code=72,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBD, bit_position=7)]
  ),
  "Titan Gun": CRItemData(
    type="Gun",
    code=73,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBC, bit_position=0)]
  ),
  "Claw Gun": CRItemData(
    type="Gun",
    code=74,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBC, bit_position=1)]
  ),
  "Knuckle Gun": CRItemData(
    type="Gun",
    code=75,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBC, bit_position=2)]
  ),
  "Afterburner Gun": CRItemData(
    type="Gun",
    code=76,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBC, bit_position=3)]
  ),
  "Blade Gun": CRItemData(
    type="Gun",
    code=77,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBC, bit_position=4)]
  ),
  "Meteor Storm Gun": CRItemData(
    type="Gun",
    code=78,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBC, bit_position=5)]
  ),
  "Twin Fang Gun": CRItemData(
    type="Gun",
    code=79,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBC, bit_position=6)]
  ),
  "Gravity Gun": CRItemData(
    type="Gun",
    code=80,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBBC, bit_position=7)]
  ),
  "Phoenix Gun": CRItemData(
    type="Gun",
    code=81,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC3, bit_position=0)]
  ),
  "Can Gun": CRItemData(
    type="Gun",
    code=82,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC3, bit_position=1)]
  ),
  "Left Pulse Gun": CRItemData(
    type="Gun",
    code=83,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC3, bit_position=2)]
  ),
  "Right Pulse Gun": CRItemData(
    type="Gun",
    code=84,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC3, bit_position=3)]
  ),
  "Sword Storm Gun": CRItemData(
    type="Gun",
    code=85,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC3, bit_position=4)]
  ),
  "Ion Gun": CRItemData(
    type="Gun",
    code=86,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC3, bit_position=5)]
  ),
  "Flare Gun": CRItemData(
    type="Gun",
    code=87,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC3, bit_position=6)]
  ),
  "Left 5-Way Gun": CRItemData(
    type="Gun",
    code=88,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC3, bit_position=7)]
  ),
  "Right 5-Way Gun": CRItemData(
    type="Gun",
    code=89,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC2, bit_position=0)]
  ),
  "Halo Gun": CRItemData(
    type="Gun",
    code=90,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC2, bit_position=1)]
  ),
  "Wave Laser Gun": CRItemData(
    type="Gun",
    code=91,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC2, bit_position=2)],
    illegal=True
  ),
  "X Laser Gun": CRItemData(
    type="Gun",
    code=92,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC2, bit_position=3)],
    illegal=True
  ),
  "Crystal Strike Gun": CRItemData(
    type="Gun",
    code=93,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC2, bit_position=4)],
    illegal=True
  ),
  "Wyrm Gun": CRItemData(
    type="Gun",
    code=94,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC2, bit_position=5)],
    illegal=True
  ),
  "Raptor Gun": CRItemData(
    type="Gun",
    code=95,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC2, bit_position=6)],
    illegal=True
  ),
  "Waxing Arc Gun": CRItemData(
    type="Gun",
    code=96,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC2, bit_position=7)],
    illegal=True
  ),
  "Waning Arc Gun": CRItemData(
    type="Gun",
    code=97,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBC1, bit_position=0)],
    illegal=True
  ),
  
  # Bomb Parts
  "Standard Bomb": CRItemData(
    type="Bomb",
    code=98,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDF, bit_position=0)]
  ),
  "Standard F Bomb": CRItemData(
    type="Bomb",
    code=99,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDF, bit_position=1)]
  ),
  "Standard S Bomb": CRItemData(
    type="Bomb",
    code=100,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDF, bit_position=2)]
  ),
  "Wave Bomb": CRItemData(
    type="Bomb",
    code=101,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDF, bit_position=3)]
  ),
  "Straight G Bomb": CRItemData(
    type="Bomb",
    code=102,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDF, bit_position=4)]
  ),
  "Straight S Bomb": CRItemData(
    type="Bomb",
    code=103,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDF, bit_position=5)]
  ),
  "Straight T Bomb": CRItemData(
    type="Bomb",
    code=104,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDF, bit_position=6)]
  ),
  "Right Flank H Bomb": CRItemData(
    type="Bomb",
    code=105,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDF, bit_position=7)]
  ),
  "Left Flank H Bomb": CRItemData(
    type="Bomb",
    code=106,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDE, bit_position=0)]
  ),
  "Right Wave Bomb": CRItemData(
    type="Bomb",
    code=107,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDE, bit_position=1)]
  ),
  "Left Wave Bomb": CRItemData(
    type="Bomb",
    code=108,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDE, bit_position=2)]
  ),
  "Burrow D Bomb": CRItemData(
    type="Bomb",
    code=109,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDE, bit_position=3)]
  ),
  "Burrow P Bomb": CRItemData(
    type="Bomb",
    code=110,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDE, bit_position=4)]
  ),
  "Freeze Bomb": CRItemData(
    type="Bomb",
    code=111,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDE, bit_position=5)]
  ),
  "Tomahawk B Bomb": CRItemData(
    type="Bomb",
    code=112,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDE, bit_position=6)]
  ),
  "Tomahawk G Bomb": CRItemData(
    type="Bomb",
    code=113,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDE, bit_position=7)]
  ),
  "Gemini B Bomb": CRItemData(
    type="Bomb",
    code=114,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDD, bit_position=0)]
  ),
  "Gemini P Bomb": CRItemData(
    type="Bomb",
    code=115,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDD, bit_position=1)]
  ),
  "Submarine D Bomb": CRItemData(
    type="Bomb",
    code=116,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDD, bit_position=2)]
  ),
  "Submarine P Bomb": CRItemData(
    type="Bomb",
    code=117,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDD, bit_position=3)]
  ),
  "Crescent P Bomb": CRItemData(
    type="Bomb",
    code=118,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDD, bit_position=4)]
  ),
  "Crescent C Bomb": CRItemData(
    type="Bomb",
    code=119,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDD, bit_position=5)]
  ),
  "Dual Bomb": CRItemData(
    type="Bomb",
    code=120,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDD, bit_position=6)]
  ),
  "Dual C Bomb": CRItemData(
    type="Bomb",
    code=121,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDD, bit_position=7)]
  ),
  "Acrobat Bomb": CRItemData(
    type="Bomb",
    code=122,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDC, bit_position=0)]
  ),
  "Delta Bomb": CRItemData(
    type="Bomb",
    code=123,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDC, bit_position=1)]
  ),
  "Wall Bomb": CRItemData(
    type="Bomb",
    code=124,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDC, bit_position=2)]
  ),
  "Smash Bomb": CRItemData(
    type="Bomb",
    code=125,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDC, bit_position=3)]
  ),
  "Double Mine Bomb": CRItemData(
    type="Bomb",
    code=126,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDC, bit_position=4)]
  ),
  "Geo Trap Bomb": CRItemData(
    type="Bomb",
    code=127,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDC, bit_position=5)]
  ),
  "Titan Bomb": CRItemData(
    type="Bomb",
    code=128,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDC, bit_position=6)]
  ),
  "Can Bomb": CRItemData(
    type="Bomb",
    code=129,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBDC, bit_position=7)]
  ),
  "Standard K Bomb": CRItemData(
    type="Bomb",
    code=130,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBE3, bit_position=0)]
  ),
  "Submarine K Bomb": CRItemData(
    type="Bomb",
    code=131,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBE3, bit_position=1)]
  ),
  "Crescent K Bomb": CRItemData(
    type="Bomb",
    code=132,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBE3, bit_position=2)]
  ),
  "Standard X Bomb": CRItemData(
    type="Bomb",
    code=133,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBE3, bit_position=3)]
  ),
  "Treble Bomb": CRItemData(
    type="Bomb",
    code=134,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBE3, bit_position=4)],
    illegal=True
  ),
  "Wyvern Bomb": CRItemData(
    type="Bomb",
    code=135,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBE3, bit_position=5)],
    illegal=True
  ),
  "Waxing Arc Bomb": CRItemData(
    type="Bomb",
    code=136,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBE3, bit_position=6)],
    illegal=True
  ),
  "Waning Arc Bomb": CRItemData(
    type="Bomb",
    code=137,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBE3, bit_position=7)],
    illegal=True
  ),

  #Pod Parts
  "Standard Pod": CRItemData(
    type="Pod",
    code=138,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFF, bit_position=0)]
  ),
  "Seeker F Pod": CRItemData(
    type="Pod",
    code=139,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFF, bit_position=1)]
  ),
  "Seeker G Pod": CRItemData(
    type="Pod",
    code=140,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFF, bit_position=2)]
  ),
  "Speed D Pod": CRItemData(
    type="Pod",
    code=141,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFF, bit_position=3)]
  ),
  "Speed P Pod": CRItemData(
    type="Pod",
    code=142,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFF, bit_position=4)]
  ),
  "Cockroach G Pod": CRItemData(
    type="Pod",
    code=143,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFF, bit_position=5)]
  ),
  "Cockroach H Pod": CRItemData(
    type="Pod",
    code=144,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFF, bit_position=6)]
  ),
  "Dolphin Pod": CRItemData(
    type="Pod",
    code=145,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFF, bit_position=7)]
  ),
  "Dolphin G Pod": CRItemData(
    type="Pod",
    code=146,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFE, bit_position=0)]
  ),
  "Spider Pod": CRItemData(
    type="Pod",
    code=147,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFE, bit_position=1)]
  ),
  "Spider G Pod": CRItemData(
    type="Pod",
    code=148,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFE, bit_position=2)]
  ),
  "Sky Freeze Pod": CRItemData(
    type="Pod",
    code=149,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFE, bit_position=3)]
  ),
  "Ground Freeze Pod": CRItemData(
    type="Pod",
    code=150,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFE, bit_position=4)]
  ),
  "Feint F Pod": CRItemData(
    type="Pod",
    code=151,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFE, bit_position=5)]
  ),
  "Feint G Pod": CRItemData(
    type="Pod",
    code=152,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFE, bit_position=6)]
  ),
  "Float F Pod": CRItemData(
    type="Pod",
    code=153,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFE, bit_position=7)]
  ),
  "Jumping B Pod": CRItemData(
    type="Pod",
    code=154,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFD, bit_position=0)]
  ),
  "Jumping G Pod": CRItemData(
    type="Pod",
    code=155,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFD, bit_position=1)]
  ),
  "Diving Pod": CRItemData(
    type="Pod",
    code=156,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFD, bit_position=2)]
  ),
  "Wave Pod": CRItemData(
    type="Pod",
    code=157,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFD, bit_position=3)]
  ),
  "Satellite Pod": CRItemData(
    type="Pod",
    code=158,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFD, bit_position=4)]
  ),
  "Satellite H Pod": CRItemData(
    type="Pod",
    code=159,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFD, bit_position=5)]
  ),
  "Beast F Pod": CRItemData(
    type="Pod",
    code=160,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFD, bit_position=6)]
  ),
  "Trio H Pod": CRItemData(
    type="Pod",
    code=161,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFD, bit_position=7)]
  ),
  "Wall Pod": CRItemData(
    type="Pod",
    code=162,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFC, bit_position=0)]
  ),
  "Reflection Pod": CRItemData(
    type="Pod",
    code=163,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFC, bit_position=1)]
  ),
  "Caboose C Pod": CRItemData(
    type="Pod",
    code=164,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFC, bit_position=2)]
  ),
  "Caboose T Pod": CRItemData(
    type="Pod",
    code=165,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFC, bit_position=3)]
  ),
  "Twin Flank F Pod": CRItemData(
    type="Pod",
    code=166,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFC, bit_position=4)]
  ),
  "Twin Flank G Pod": CRItemData(
    type="Pod",
    code=167,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFC, bit_position=5)]
  ),
  "Umbrella Pod": CRItemData(
    type="Pod",
    code=168,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFC, bit_position=6)]
  ),
  "Throwing D Pod": CRItemData(
    type="Pod",
    code=169,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFBFC, bit_position=7)]
  ),
  "Throwing P Pod": CRItemData(
    type="Pod",
    code=170,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC03, bit_position=0)]
  ),
  "Double Wave Pod": CRItemData(
    type="Pod",
    code=171,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC03, bit_position=1)]
  ),
  "Titan Pod": CRItemData(
    type="Pod",
    code=172,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC03, bit_position=2)]
  ),
  "Can Pod": CRItemData(
    type="Pod",
    code=173,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC03, bit_position=3)]
  ),
  "Standard F Pod": CRItemData(
    type="Pod",
    code=174,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC03, bit_position=4)]
  ),
  "Caboose X Pod": CRItemData(
    type="Pod",
    code=175,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC03, bit_position=5)]
  ),
  "Cheetah Pod": CRItemData(
    type="Pod",
    code=176,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC03, bit_position=6)],
    illegal=True
  ),
  "Wolf Spider Pod": CRItemData(
    type="Pod",
    code=177,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC03, bit_position=7)],
    illegal=True
  ),
  "Orca Pod": CRItemData(
    type="Pod",
    code=178,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC02, bit_position=0)],
    illegal=True
  ),

  # Leg Parts
  "Standard Legs": CRItemData(
    type="Legs",
    code=179,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1F, bit_position=0)]
  ),
  "High Jump Legs": CRItemData(
    type="Legs",
    code=180,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1F, bit_position=1)]
  ),
  "Ground Legs": CRItemData(
    type="Legs",
    code=181,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1F, bit_position=2)]
  ),
  "Formula Legs": CRItemData(
    type="Legs",
    code=182,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1F, bit_position=3)]
  ),
  "Stabilizer Legs": CRItemData(
    type="Legs",
    code=183,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1F, bit_position=4)]
  ),
  "Short Thrust Legs": CRItemData(
    type="Legs",
    code=184,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1F, bit_position=5)]
  ),
  "Long Thrust Legs": CRItemData(
    type="Legs",
    code=185,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1F, bit_position=6)]
  ),
  "Quick Jump Legs": CRItemData(
    type="Legs",
    code=186,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1F, bit_position=7)]
  ),
  "Feather Legs": CRItemData(
    type="Legs",
    code=187,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1E, bit_position=0)]
  ),
  "Wide Jump Legs": CRItemData(
    type="Legs",
    code=188,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1E, bit_position=1)]
  ),
  "Can Legs": CRItemData(
    type="Legs",
    code=189,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1E, bit_position=2)]
  ),
  "Booster Legs": CRItemData(
    type="Legs",
    code=190,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1E, bit_position=3)]
  ),
  "Swallow Legs": CRItemData(
    type="Legs",
    code=191,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1E, bit_position=4)],
    illegal=True
  ),
  "Raven Legs": CRItemData(
    type="Legs",
    code=192,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1E, bit_position=5)],
    illegal=True
  ),
  "Eclipse Legs": CRItemData(
    type="Legs",
    code=193,
    classification=IC.useful,
    update_ram_addr=[CRRamData(0x803BFC1E, bit_position=6)],
    illegal=True
  ),
}

# Base items used to trigger Progressive advance
PROGRESSIVE_BASE_ITEM_TABLE: dict[str, CRItemData] = {
    "Rahu Evolution" : CRItemData(
        type="Progressive Rahu",
        code = 194,
        classification=IC.useful,
        update_ram_addr=None,
        illegal=True
    )
}

# Rahu evolution table
PROGRESSION_RAHU: dict[str, list[CRItemData]] = {
  "Rahu Evolution Steps": [
    CRItemData(
      name="Rahu I",
      type="Rahu Part",
      code=None,
      classification=IC.useful,
      update_ram_addr=[CRRamData(0x803BFB9C, bit_position=6)],
      illegal=True
    ),
    CRItemData(
      name="Penumbra I Pod",
      type="Rahu Part",
      code=None,
      classification=IC.useful,
      update_ram_addr=[CRRamData(0x803BFC02, bit_position=1)],
      illegal=True
    ),
    CRItemData(
      name="Rahu I Gun",
      type="Rahu Part",
      code=None,
      classification=IC.useful,
      update_ram_addr=[CRRamData(0x803BFBC1, bit_position=1)],
      illegal=True
    ),
    CRItemData(
      name="Rahu II",
      type="Rahu Part",
      code=None,
      classification=IC.useful,
      update_ram_addr=[CRRamData(0x803BFB9C, bit_position=7)],
      illegal=True
    ),
    CRItemData(
      name="Penumbra II Pod",
      type="Rahu Part",
      code=None,
      classification=IC.useful,
      update_ram_addr=[CRRamData(0x803BFC02, bit_position=2)],
      illegal=True
    ),
    CRItemData(
      name="Rahu II Gun",
      type="Rahu Part",
      code=None,
      classification=IC.useful,
      update_ram_addr=[CRRamData(0x803BFBC1, bit_position=2)],
      illegal=True
    ),
    CRItemData(
      name="Grand Cross Bomb",
      type="Rahu Part",
      code=None,
      classification=IC.useful,
      update_ram_addr=[CRRamData(0x803BFBE2, bit_position=0)],
      illegal=True
    ),
    CRItemData(
      name="Ultimate Legs",
      type="Rahu Part",
      code=None,
      classification=IC.useful,
      update_ram_addr=[CRRamData(0x803BFC1E, bit_position=7)],
      illegal=True
    ),
    CRItemData(
      name="Penumbra III Pod",
      type="Rahu Part",
      code=None,
      classification=IC.useful,
      update_ram_addr=[CRRamData(0x803BFC02, bit_position=3)],
      illegal=True
    ),
    CRItemData(
      name="Rahu III Gun",
      type="Rahu Part",
      code=None,
      classification=IC.useful,
      update_ram_addr=[CRRamData(0x803BFBC1, bit_position=3)],
      illegal=True
    ),
    CRItemData(
      name="Rahu III",
      type="Rahu Part",
      code=None,
      classification=IC.useful,
      update_ram_addr=[CRRamData(0x803BFBA3, bit_position=0)],
      illegal=True
    )
  ]
}

FILLER_ITEMS: dict[str, CRItemData] = {
   "Robo Cube": CRItemData(
      name="Robo Cube",
      type="Filler Item",
      code=205,
      classification=IC.filler,
   )
}

COMPLETION_CONDITIONS: dict[str, CRItemData] = {
    "Defeat Rahu III": CRItemData(
        name="Defeat Rahu III",
        type="Completion Item",
        code=None,
        classification=IC.progression
    )
}

ALL_ITEMS_TABLE = {
# **PROGRESSION_SCENARIO_TABLE,
  **PARTS_ITEM_TABLE,
  **PROGRESSIVE_BASE_ITEM_TABLE,
  **{item.name: item for item_list in PROGRESSION_RAHU.values() for item in item_list}, # Needed for location checks
  **FILLER_ITEMS
}
