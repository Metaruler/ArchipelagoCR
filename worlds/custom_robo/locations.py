#Checks
from typing import NamedTuple, Optional
from .helpers import CRRamData
from BaseClasses import Location, Region

class CRLocationData(NamedTuple):
  code:Optional[int]
  ram_addr: Optional[CRRamData] = None
  illegal: bool = False
  type: str = ""
  battle_number: int = 0
  parent_region: str = ""

BATTLE_COUNTER_ADDR = 0x803BF9D9

class CRLocation(Location):
  game: str = "Custom Robo"

  def __init__(self, player, name: str, parent: Region, data: CRLocationData):
    address = None if data.code is None else CRLocation.get_apid(data.code)
    super().__init__(player, name, address, parent)

    self.code = data.code
    self.ram_addr = data.ram_addr

  @staticmethod
  def get_apid(code: int):
    base_id: int = 8000
    return base_id + code

# Begin check logic
# Check for each part being used in a victory
PART_USE: dict[str, CRLocationData] = {
  "Use Ray 01": CRLocationData(
    code=1,
    ram_addr=CRRamData(0x803BFBA7, bit_position=0),
    type = "Part Use"
  ),
  "Use Splendor": CRLocationData(
    code=2,
    ram_addr=CRRamData(0x803BFBA7, bit_position=1),
    type = "Part Use"
  ),
  "Use Glory": CRLocationData(
    code=3,
    ram_addr=CRRamData(0x803BFBA7, bit_position=2),
    type = "Part Use"
  ),
  "Use Milky Way": CRLocationData(
    code=4,
    ram_addr=CRRamData(0x803BFBA7, bit_position=3),
    type = "Part Use"
  ),
  "Use Earth": CRLocationData(
    code=5,
    ram_addr=CRRamData(0x803BFBA7, bit_position=4),
    type = "Part Use"
  ),
  "Use Sol": CRLocationData(
    code=6,
    ram_addr=CRRamData(0x803BFBA7, bit_position=5),
    type = "Part Use"
  ),
  "Use Metal Ape": CRLocationData(
    code=7,
    ram_addr=CRRamData(0x803BFBA7, bit_position=6),
    type = "Part Use"
  ),
  "Use Metal Bear": CRLocationData(
    code=8,
    ram_addr=CRRamData(0x803BFBA7, bit_position=7),
    type = "Part Use"
  ),
  "Use Metal Ox": CRLocationData(
    code=9,
    ram_addr=CRRamData(0x803BFBA6, bit_position=0),
    type = "Part Use"
  ),
  "Use Swift": CRLocationData(
    code=10,
    ram_addr=CRRamData(0x803BFBA6, bit_position=1),
    type = "Part Use"
  ),
  "Use Shrike": CRLocationData(
    code=11,
    ram_addr=CRRamData(0x803BFBA6, bit_position=2),
    type = "Part Use"
  ),
  "Use Peregrine": CRLocationData(
    code=12,
    ram_addr=CRRamData(0x803BFBA6, bit_position=3),
    type = "Part Use"
  ),
  "Use Javelin": CRLocationData(
    code=13,
    ram_addr=CRRamData(0x803BFBA6, bit_position=4),
    type = "Part Use"
  ),
  "Use Glaive": CRLocationData(
    code=14,
    ram_addr=CRRamData(0x803BFBA6, bit_position=5),
    type = "Part Use"
  ),
  "Use Halberd": CRLocationData(
    code=15,
    ram_addr=CRRamData(0x803BFBA6, bit_position=6),
    type = "Part Use"
  ),
  "Use Criminal": CRLocationData(
    code=16,
    ram_addr=CRRamData(0x803BFBA6, bit_position=7),
    type = "Part Use"
  ),
  "Use Buggy": CRLocationData(
    code=17,
    ram_addr=CRRamData(0x803BFBA5, bit_position=0),
    type = "Part Use"
  ),
  "Use Juggler": CRLocationData(
    code=18,
    ram_addr=CRRamData(0x803BFBA5, bit_position=1),
    type = "Part Use"
  ),
  "Use Defender": CRLocationData(
    code=19,
    ram_addr=CRRamData(0x803BFBA5, bit_position=2),
    type = "Part Use"
  ),
  "Use Seeker": CRLocationData(
    code=20,
    ram_addr=CRRamData(0x803BFBA5, bit_position=3),
    type = "Part Use"
  ),
  "Use Breaker": CRLocationData(
    code=21,
    ram_addr=CRRamData(0x803BFBA5, bit_position=4),
    type = "Part Use"
  ),
  "Use Seal Head": CRLocationData(
    code=22,
    ram_addr=CRRamData(0x803BFBA5, bit_position=5),
    type = "Part Use"
  ),
  "Use Dour Head": CRLocationData(
    code=23,
    ram_addr=CRRamData(0x803BFBA5, bit_position=6),
    type = "Part Use"
  ),
  "Use Tank Head": CRLocationData(
    code=24,
    ram_addr=CRRamData(0x803BFBA5, bit_position=7),
    type = "Part Use"
  ),
  "Use Ray Legend": CRLocationData(
    code=25,
    ram_addr=CRRamData(0x803BFBA4, bit_position=0),
    illegal=True,
    type = "Part Use"
  ),
  "Use Oil Can": CRLocationData(
    code=26,
    ram_addr=CRRamData(0x803BFBA4, bit_position=1),
    type = "Part Use"
  ),
  "Use Ray Warrior": CRLocationData(
    code=27,
    ram_addr=CRRamData(0x803BFBA4, bit_position=2),
    illegal=True,
    type = "Part Use"
  ),
  "Use Rakansen": CRLocationData(
    code=28,
    ram_addr=CRRamData(0x803BFBA4, bit_position=3),
    illegal=True,
    type = "Part Use"
  ),
  "Use Ruhiel": CRLocationData(
    code=29,
    ram_addr=CRRamData(0x803BFBA4, bit_position=4),
    illegal=True,
    type = "Part Use"
  ),
  "Use Athena": CRLocationData(
    code=30,
    ram_addr=CRRamData(0x803BFBA4, bit_position=5),
    illegal=True,
    type = "Part Use"
  ),
  "Use Rahu I": CRLocationData(
    code=31,
    ram_addr=CRRamData(0x803BFBA4, bit_position=6),
    illegal=True,
    type = "Part Use"
  ),
  "Use Rahu II": CRLocationData(
    code=32,
    ram_addr=CRRamData(0x803BFBA4, bit_position=7),
    illegal=True,
    type = "Part Use"
  ),
  "Use Rahu III": CRLocationData(
    code=33,
    ram_addr=CRRamData(0x803BFBAB, bit_position=0),
    illegal=True,
    type = "Part Use"
  ),
  "Use Chickenheart": CRLocationData(
    code=34,
    ram_addr=CRRamData(0x803BFBAB, bit_position=1),
    type = "Part Use"
  ),
  "Use Basic Gun": CRLocationData(
    code=35,
    ram_addr=CRRamData(0x803BFBC7, bit_position=0),
    type = "Part Use"
  ),
  "Use 3-Way Gun": CRLocationData(
    code=36,
    ram_addr=CRRamData(0x803BFBC7, bit_position=1),
    type = "Part Use"
  ),
  "Use Gatling Gun": CRLocationData(
    code=37,
    ram_addr=CRRamData(0x803BFBC7, bit_position=2),
    type = "Part Use"
  ),
  "Use Vertical Gun": CRLocationData(
    code=38,
    ram_addr=CRRamData(0x803BFBC7, bit_position=3),
    type = "Part Use"
  ),
  "Use Sniper Gun": CRLocationData(
    code=39,
    ram_addr=CRRamData(0x803BFBC7, bit_position=4),
    type = "Part Use"
  ),
  "Use Stun Gun": CRLocationData(
    code=40,
    ram_addr=CRRamData(0x803BFBC7, bit_position=5),
    type = "Part Use"
  ),
  "Use Hornet Gun": CRLocationData(
    code=41,
    ram_addr=CRRamData(0x803BFBC7, bit_position=6),
    type = "Part Use"
  ),
  "Use Flame Gun": CRLocationData(
    code=42,
    ram_addr=CRRamData(0x803BFBC7, bit_position=7),
    type = "Part Use"
  ),
  "Use Dragon Gun": CRLocationData(
    code=43,
    ram_addr=CRRamData(0x803BFBC6, bit_position=0),
    type = "Part Use"
  ),
  "Use Splash Gun": CRLocationData(
    code=44,
    ram_addr=CRRamData(0x803BFBC6, bit_position=1),
    type = "Part Use"
  ),
  "Use Left Arc Gun": CRLocationData(
    code=45,
    ram_addr=CRRamData(0x803BFBC6, bit_position=2),
    type = "Part Use"
  ),
  "Use Right Arc Gun": CRLocationData(
    code=46,
    ram_addr=CRRamData(0x803BFBC6, bit_position=3),
    type = "Part Use"
  ),
  "Use Shotgun Gun": CRLocationData(
    code=47,
    ram_addr=CRRamData(0x803BFBC6, bit_position=4),
    type = "Part Use"
  ),
  "Use Rayfall Gun": CRLocationData(
    code=48,
    ram_addr=CRRamData(0x803BFBC6, bit_position=5),
    type = "Part Use"
  ),
  "Use Bubble Gun": CRLocationData(
    code=49,
    ram_addr=CRRamData(0x803BFBC6, bit_position=6),
    type = "Part Use"
  ),
  "Use Eagle Gun": CRLocationData(
    code=50,
    ram_addr=CRRamData(0x803BFBC6, bit_position=7),
    type = "Part Use"
  ),
  "Use V Laser Gun": CRLocationData(
    code=51,
    ram_addr=CRRamData(0x803BFBC5, bit_position=0),
    type = "Part Use"
  ),
  "Use Magnum Gun": CRLocationData(
    code=52,
    ram_addr=CRRamData(0x803BFBC5, bit_position=1),
    type = "Part Use"
  ),
  "Use Needle Gun": CRLocationData(
    code=53,
    ram_addr=CRRamData(0x803BFBC5, bit_position=2),
    type = "Part Use"
  ),
  "Use Starshot Gun": CRLocationData(
    code=54,
    ram_addr=CRRamData(0x803BFBC5, bit_position=3),
    type = "Part Use"
  ),
  "Use Glider Gun": CRLocationData(
    code=55,
    ram_addr=CRRamData(0x803BFBC5, bit_position=4),
    type = "Part Use"
  ),
  "Use Homing Star Gun": CRLocationData(
    code=56,
    ram_addr=CRRamData(0x803BFBC5, bit_position=5),
    type = "Part Use"
  ),
  "Use Trap Gun": CRLocationData(
    code=57,
    ram_addr=CRRamData(0x803BFBC5, bit_position=6),
    type = "Part Use"
  ),
  "Use Drill Gun": CRLocationData(
    code=58,
    ram_addr=CRRamData(0x803BFBC5, bit_position=7),
    type = "Part Use"
  ),
  "Use Titan Gun": CRLocationData(
    code=59,
    ram_addr=CRRamData(0x803BFBC4, bit_position=0),
    type = "Part Use"
  ),
  "Use Claw Gun": CRLocationData(
    code=60,
    ram_addr=CRRamData(0x803BFBC4, bit_position=1),
    type = "Part Use"
  ),
  "Use Knuckle Gun": CRLocationData(
    code=61,
    ram_addr=CRRamData(0x803BFBC4, bit_position=2),
    type = "Part Use"
  ),
  "Use Afterburner Gun": CRLocationData(
    code=62,
    ram_addr=CRRamData(0x803BFBC4, bit_position=3),
    type = "Part Use"
  ),
  "Use Blade Gun": CRLocationData(
    code=63,
    ram_addr=CRRamData(0x803BFBC4, bit_position=4),
    type = "Part Use"
  ),
  "Use Meteor Storm Gun": CRLocationData(
    code=64,
    ram_addr=CRRamData(0x803BFBC4, bit_position=5),
    type = "Part Use"
  ),
  "Use Twin Fang Gun": CRLocationData(
    code=65,
    ram_addr=CRRamData(0x803BFBC4, bit_position=6),
    type = "Part Use"
  ),
  "Use Gravity Gun": CRLocationData(
    code=66,
    ram_addr=CRRamData(0x803BFBC4, bit_position=7),
    type = "Part Use"
  ),
  "Use Phoenix Gun": CRLocationData(
    code=67,
    ram_addr=CRRamData(0x803BFBCB, bit_position=0),
    type = "Part Use"
  ),
  "Use Can Gun": CRLocationData(
    code=68,
    ram_addr=CRRamData(0x803BFBCB, bit_position=1),
    type = "Part Use"
  ),
  "Use Left Pulse Gun": CRLocationData(
    code=69,
    ram_addr=CRRamData(0x803BFBCB, bit_position=2),
    type = "Part Use"
  ),
  "Use Right Pulse Gun": CRLocationData(
    code=70,
    ram_addr=CRRamData(0x803BFBCB, bit_position=3),
    type = "Part Use"
  ),
  "Use Sword Storm Gun": CRLocationData(
    code=71,
    ram_addr=CRRamData(0x803BFBCB, bit_position=4),
    type = "Part Use"
  ),
  "Use Ion Gun": CRLocationData(
    code=72,
    ram_addr=CRRamData(0x803BFBCB, bit_position=5),
    type = "Part Use"
  ),
  "Use Flare Gun": CRLocationData(
    code=73,
    ram_addr=CRRamData(0x803BFBCB, bit_position=6),
    type = "Part Use"
  ),
  "Use Left 5-Way Gun": CRLocationData(
    code=74,
    ram_addr=CRRamData(0x803BFBCB, bit_position=7),
    type = "Part Use"
  ),
  "Use Right 5-Way Gun": CRLocationData(
    code=75,
    ram_addr=CRRamData(0x803BFBCA, bit_position=0),
    type = "Part Use"
  ),
  "Use Halo Gun": CRLocationData(
    code=76,
    ram_addr=CRRamData(0x803BFBCA, bit_position=1),
    type = "Part Use"
  ),
  "Use Wave Laser Gun": CRLocationData(
    code=77,
    ram_addr=CRRamData(0x803BFBCA, bit_position=2),
    illegal=True,
    type = "Part Use"
  ),
  "Use X Laser Gun": CRLocationData(
    code=78,
    ram_addr=CRRamData(0x803BFBCA, bit_position=3),
    illegal=True,
    type = "Part Use"
  ),
  "Use Crystal Strike Gun": CRLocationData(
    code=79,
    ram_addr=CRRamData(0x803BFBCA, bit_position=4),
    illegal=True,
    type = "Part Use"
  ),
  "Use Wyrm Gun": CRLocationData(
    code=80,
    ram_addr=CRRamData(0x803BFBCA, bit_position=5),
    illegal=True,
    type = "Part Use"
  ),
  "Use Raptor Gun": CRLocationData(
    code=81,
    ram_addr=CRRamData(0x803BFBCA, bit_position=6),
    illegal=True,
    type = "Part Use"
  ),
  "Use Waxing Arc Gun": CRLocationData(
    code=82,
    ram_addr=CRRamData(0x803BFBCA, bit_position=7),
    illegal=True,
    type = "Part Use"
  ),
  "Use Waning Arc Gun": CRLocationData(
    code=83,
    ram_addr=CRRamData(0x803BFBC9, bit_position=0),
    illegal=True,
    type = "Part Use"
  ),
  "Use Rahu I Gun": CRLocationData(
    code=84,
    ram_addr=CRRamData(0x803BFBC9, bit_position=1),
    illegal=True,
    type = "Part Use"
  ),
  "Use Rahu II Gun": CRLocationData(
    code=85,
    ram_addr=CRRamData(0x803BFBC9, bit_position=2),
    illegal=True,
    type = "Part Use"
  ),
  "Use Rahu III Gun": CRLocationData(
    code=86,
    ram_addr=CRRamData(0x803BFBC9, bit_position=3),
    illegal=True,
    type = "Part Use"
  ),
  "Use Standard Bomb": CRLocationData(
    code=87,
    ram_addr=CRRamData(0x803BFBE7, bit_position=0),
    type = "Part Use"
  ),
  "Use Standard F Bomb": CRLocationData(
    code=88,
    ram_addr=CRRamData(0x803BFBE7, bit_position=1),
    type = "Part Use"
  ),
  "Use Standard S Bomb": CRLocationData(
    code=89,
    ram_addr=CRRamData(0x803BFBE7, bit_position=2),
    type = "Part Use"
  ),
  "Use Wave Bomb": CRLocationData(
    code=90,
    ram_addr=CRRamData(0x803BFBE7, bit_position=3),
    type = "Part Use"
  ),
  "Use Straight G Bomb": CRLocationData(
    code=91,
    ram_addr=CRRamData(0x803BFBE7, bit_position=4),
    type = "Part Use"
  ),
  "Use Straight S Bomb": CRLocationData(
    code=92,
    ram_addr=CRRamData(0x803BFBE7, bit_position=5),
    type = "Part Use"
  ),
  "Use Straight T Bomb": CRLocationData(
    code=93,
    ram_addr=CRRamData(0x803BFBE7, bit_position=6),
    type = "Part Use"
  ),
  "Use Right Flank H Bomb": CRLocationData(
    code=94,
    ram_addr=CRRamData(0x803BFBE7, bit_position=7),
    type = "Part Use"
  ),
  "Use Left Flank H Bomb": CRLocationData(
    code=95,
    ram_addr=CRRamData(0x803BFBE6, bit_position=0),
    type = "Part Use"
  ),
  "Use Right Wave Bomb": CRLocationData(
    code=96,
    ram_addr=CRRamData(0x803BFBE6, bit_position=1),
    type = "Part Use"
  ),
  "Use Left Wave Bomb": CRLocationData(
    code=97,
    ram_addr=CRRamData(0x803BFBE6, bit_position=2),
    type = "Part Use"
  ),
  "Use Burrow D Bomb": CRLocationData(
    code=98,
    ram_addr=CRRamData(0x803BFBE6, bit_position=3),
    type = "Part Use"
  ),
  "Use Burrow P Bomb": CRLocationData(
    code=99,
    ram_addr=CRRamData(0x803BFBE6, bit_position=4),
    type = "Part Use"
  ),
  "Use Freeze Bomb": CRLocationData(
    code=100,
    ram_addr=CRRamData(0x803BFBE6, bit_position=5),
    type = "Part Use"
  ),
  "Use Tomahawk B Bomb": CRLocationData(
    code=101,
    ram_addr=CRRamData(0x803BFBE6, bit_position=6),
    type = "Part Use"
  ),
  "Use Tomahawk G Bomb": CRLocationData(
    # TODO FIX NUMBERING
    code=187,
    ram_addr=CRRamData(0x803BFBE6, bit_position=7),
    type = "Part Use"
  ),
  "Use Gemini B Bomb": CRLocationData(
    code=102,
    ram_addr=CRRamData(0x803BFBE5, bit_position=0),
    type = "Part Use"
  ),
  "Use Gemini P Bomb": CRLocationData(
    code=103,
    ram_addr=CRRamData(0x803BFBE5, bit_position=1),
    type = "Part Use"
  ),
  "Use Submarine D Bomb": CRLocationData(
    code=104,
    ram_addr=CRRamData(0x803BFBE5, bit_position=2),
    type = "Part Use"
  ),
  "Use Submarine P Bomb": CRLocationData(
    code=105,
    ram_addr=CRRamData(0x803BFBE5, bit_position=3),
    type = "Part Use"
  ),
  "Use Crescent P Bomb": CRLocationData(
    code=106,
    ram_addr=CRRamData(0x803BFBE5, bit_position=4),
    type = "Part Use"
  ),
  "Use Crescent C Bomb": CRLocationData(
    code=107,
    ram_addr=CRRamData(0x803BFBE5, bit_position=5),
    type = "Part Use"
  ),
  "Use Dual Bomb": CRLocationData(
    code=108,
    ram_addr=CRRamData(0x803BFBE5, bit_position=6),
    type = "Part Use"
  ),
  "Use Dual C Bomb": CRLocationData(
    code=109,
    ram_addr=CRRamData(0x803BFBE5, bit_position=7),
    type = "Part Use"
  ),
  "Use Acrobat Bomb": CRLocationData(
    code=110,
    ram_addr=CRRamData(0x803BFBE4, bit_position=0),
    type = "Part Use"
  ),
  "Use Delta Bomb": CRLocationData(
    code=111,
    ram_addr=CRRamData(0x803BFBE4, bit_position=1),
    type = "Part Use"
  ),
  "Use Wall Bomb": CRLocationData(
    code=112,
    ram_addr=CRRamData(0x803BFBE4, bit_position=2),
    type = "Part Use"
  ),
  "Use Smash Bomb": CRLocationData(
    code=113,
    ram_addr=CRRamData(0x803BFBE4, bit_position=3),
    type = "Part Use"
  ),
  "Use Double Mine Bomb": CRLocationData(
    code=114,
    ram_addr=CRRamData(0x803BFBE4, bit_position=4),
    type = "Part Use"
  ),
  "Use Geo Trap Bomb": CRLocationData(
    code=115,
    ram_addr=CRRamData(0x803BFBE4, bit_position=5),
    type = "Part Use"
  ),
  "Use Titan Bomb": CRLocationData(
    code=116,
    ram_addr=CRRamData(0x803BFBE4, bit_position=6),
    type = "Part Use"
  ),
  "Use Can Bomb": CRLocationData(
    code=117,
    ram_addr=CRRamData(0x803BFBE4, bit_position=7),
    type = "Part Use"
  ),
  "Use Standard K Bomb": CRLocationData(
    code=118,
    ram_addr=CRRamData(0x803BFBEB, bit_position=0),
    type = "Part Use"
  ),
  "Use Submarine K Bomb": CRLocationData(
    code=119,
    ram_addr=CRRamData(0x803BFBEB, bit_position=1),
    type = "Part Use"
  ),
  "Use Crescent K Bomb": CRLocationData(
    code=120,
    ram_addr=CRRamData(0x803BFBEB, bit_position=2),
    type = "Part Use"
  ),
  "Use Standard X Bomb": CRLocationData(
    code=121,
    ram_addr=CRRamData(0x803BFBEB, bit_position=3),
    type = "Part Use"
  ),
  "Use Treble Bomb": CRLocationData(
    code=122,
    ram_addr=CRRamData(0x803BFBEB, bit_position=4),
    illegal=True,
    type = "Part Use"
  ),
  "Use Wyvern Bomb": CRLocationData(
    code=123,
    ram_addr=CRRamData(0x803BFBEB, bit_position=5),
    illegal=True,
    type = "Part Use"
  ),
  "Use Waxing Arc Bomb": CRLocationData(
    code=124,
    ram_addr=CRRamData(0x803BFBEB, bit_position=6),
    illegal=True,
    type = "Part Use"
  ),
  "Use Waning Arc Bomb": CRLocationData(
    code=125,
    ram_addr=CRRamData(0x803BFBEB, bit_position=7),
    illegal=True,
    type = "Part Use"
  ),
  "Use Grand Cross Bomb": CRLocationData(
    code=126,
    ram_addr=CRRamData(0x803BFBEA, bit_position=0),
    illegal=True,
    type = "Part Use"
  ),
  "Use Standard Pod": CRLocationData(
    code=127,
    ram_addr=CRRamData(0x803BFC07, bit_position=0),
    type = "Part Use"
  ),
  "Use Seeker F Pod": CRLocationData(
    code=128,
    ram_addr=CRRamData(0x803BFC07, bit_position=1),
    type = "Part Use"
  ),
  "Use Seeker G Pod": CRLocationData(
    code=129,
    ram_addr=CRRamData(0x803BFC07, bit_position=2),
    type = "Part Use"
  ),
  "Use Speed D Pod": CRLocationData(
    code=130,
    ram_addr=CRRamData(0x803BFC07, bit_position=3),
    type = "Part Use"
  ),
  "Use Speed P Pod": CRLocationData(
    code=131,
    ram_addr=CRRamData(0x803BFC07, bit_position=4),
    type = "Part Use"
  ),
  "Use Cockroach G Pod": CRLocationData(
    code=132,
    ram_addr=CRRamData(0x803BFC07, bit_position=5),
    type = "Part Use"
  ),
  "Use Cockroach H Pod": CRLocationData(
    code=133,
    ram_addr=CRRamData(0x803BFC07, bit_position=6),
    type = "Part Use"
  ),
  "Use Dolphin Pod": CRLocationData(
    code=134,
    ram_addr=CRRamData(0x803BFC07, bit_position=7),
    type = "Part Use"
  ),
  "Use Dolphin G Pod": CRLocationData(
    code=135,
    ram_addr=CRRamData(0x803BFC06, bit_position=0),
    type = "Part Use"
  ),
  "Use Spider Pod": CRLocationData(
    code=136,
    ram_addr=CRRamData(0x803BFC06, bit_position=1),
    type = "Part Use"
  ),
  "Use Spider G Pod": CRLocationData(
    code=137,
    ram_addr=CRRamData(0x803BFC06, bit_position=2),
    type = "Part Use"
  ),
  "Use Sky Freeze Pod": CRLocationData(
    code=138,
    ram_addr=CRRamData(0x803BFC06, bit_position=3),
    type = "Part Use"
  ),
  "Use Ground Freeze Pod": CRLocationData(
    code=139,
    ram_addr=CRRamData(0x803BFC06, bit_position=4),
    type = "Part Use"
  ),
  "Use Feint F Pod": CRLocationData(
    code=140,
    ram_addr=CRRamData(0x803BFC06, bit_position=5),
    type = "Part Use"
  ),
  "Use Feint G Pod": CRLocationData(
    code=141,
    ram_addr=CRRamData(0x803BFC06, bit_position=6),
    type = "Part Use"
  ),
  "Use Float F Pod": CRLocationData(
    code=142,
    ram_addr=CRRamData(0x803BFC06, bit_position=7),
    type = "Part Use"
  ),
  "Use Jumping B Pod": CRLocationData(
    code=143,
    ram_addr=CRRamData(0x803BFC05, bit_position=0),
    type = "Part Use"
  ),
  "Use Jumping G Pod": CRLocationData(
    code=144,
    ram_addr=CRRamData(0x803BFC05, bit_position=1),
    type = "Part Use"
  ),
  "Use Diving Pod": CRLocationData(
    code=145,
    ram_addr=CRRamData(0x803BFC05, bit_position=2),
    type = "Part Use"
  ),
  "Use Wave Pod": CRLocationData(
    code=146,
    ram_addr=CRRamData(0x803BFC05, bit_position=3),
    type = "Part Use"
  ),
  "Use Satellite Pod": CRLocationData(
    code=147,
    ram_addr=CRRamData(0x803BFC05, bit_position=4),
    type = "Part Use"
  ),
  "Use Satellite H Pod": CRLocationData(
    code=148,
    ram_addr=CRRamData(0x803BFC05, bit_position=5),
    type = "Part Use"
  ),
  "Use Beast F Pod": CRLocationData(
    code=149,
    ram_addr=CRRamData(0x803BFC05, bit_position=6),
    type = "Part Use"
  ),
  "Use Trio H Pod": CRLocationData(
    code=150,
    ram_addr=CRRamData(0x803BFC05, bit_position=7),
    type = "Part Use"
  ),
  "Use Wall Pod": CRLocationData(
    code=151,
    ram_addr=CRRamData(0x803BFC04, bit_position=0),
    type = "Part Use"
  ),
  "Use Reflection Pod": CRLocationData(
    code=152,
    ram_addr=CRRamData(0x803BFC04, bit_position=1),
    type = "Part Use"
  ),
  "Use Caboose C Pod": CRLocationData(
    code=153,
    ram_addr=CRRamData(0x803BFC04, bit_position=2),
    type = "Part Use"
  ),
  "Use Caboose T Pod": CRLocationData(
    code=154,
    ram_addr=CRRamData(0x803BFC04, bit_position=3),
    type = "Part Use"
  ),
  "Use Twin Flank F Pod": CRLocationData(
    code=155,
    ram_addr=CRRamData(0x803BFC04, bit_position=4),
    type = "Part Use"
  ),
  "Use Twin Flank G Pod": CRLocationData(
    code=156,
    ram_addr=CRRamData(0x803BFC04, bit_position=5),
    type = "Part Use"
  ),
  "Use Umbrella Pod": CRLocationData(
    code=157,
    ram_addr=CRRamData(0x803BFC04, bit_position=6),
    type = "Part Use"
  ),
  "Use Throwing D Pod": CRLocationData(
    code=158,
    ram_addr=CRRamData(0x803BFC04, bit_position=7),
    type = "Part Use"
  ),
  "Use Throwing P Pod": CRLocationData(
    code=159,
    ram_addr=CRRamData(0x803BFC0B, bit_position=0),
    type = "Part Use"
  ),
  "Use Double Wave Pod": CRLocationData(
    code=160,
    ram_addr=CRRamData(0x803BFC0B, bit_position=1),
    type = "Part Use"
  ),
  "Use Titan Pod": CRLocationData(
    code=161,
    ram_addr=CRRamData(0x803BFC0B, bit_position=2),
    type = "Part Use"
  ),
  "Use Can Pod": CRLocationData(
    code=162,
    ram_addr=CRRamData(0x803BFC0B, bit_position=3),
    type = "Part Use"
  ),
  "Use Standard F Pod": CRLocationData(
    code=163,
    ram_addr=CRRamData(0x803BFC0B, bit_position=4),
    type = "Part Use"
  ),
  "Use Caboose X Pod": CRLocationData(
    code=164,
    ram_addr=CRRamData(0x803BFC0B, bit_position=5),
    type = "Part Use"
  ),
  "Use Cheetah Pod": CRLocationData(
    code=165,
    ram_addr=CRRamData(0x803BFC0B, bit_position=6),
    illegal=True,
    type = "Part Use"
  ),
  "Use Wolf Spider Pod": CRLocationData(
    code=166,
    ram_addr=CRRamData(0x803BFC0B, bit_position=7),
    illegal=True,
    type = "Part Use"
  ),
  "Use Orca Pod": CRLocationData(
    code=167,
    ram_addr=CRRamData(0x803BFC0A, bit_position=0),
    illegal=True,
    type = "Part Use"
  ),
  "Use Penumbra I Pod": CRLocationData(
    code=168,
    ram_addr=CRRamData(0x803BFC0A, bit_position=1),
    illegal=True,
    type = "Part Use"
  ),
  "Use Penumbra II Pod": CRLocationData(
    code=169,
    ram_addr=CRRamData(0x803BFC0A, bit_position=2),
    illegal=True,
    type = "Part Use"
  ),
  "Use Penumbra III Pod": CRLocationData(
    code=170,
    ram_addr=CRRamData(0x803BFC0A, bit_position=3),
    illegal=True,
    type = "Part Use"
  ),
  "Use Standard Legs": CRLocationData(
    code=171,
    ram_addr=CRRamData(0x803BFC27, bit_position=0),
    type = "Part Use"
  ),
  "Use High Jump Legs": CRLocationData(
    code=172,
    ram_addr=CRRamData(0x803BFC27, bit_position=1),
    type = "Part Use"
  ),
  "Use Ground Legs": CRLocationData(
    code=173,
    ram_addr=CRRamData(0x803BFC27, bit_position=2),
    type = "Part Use"
  ),
  "Use Formula Legs": CRLocationData(
    code=174,
    ram_addr=CRRamData(0x803BFC27, bit_position=3),
    type = "Part Use"
  ),
  "Use Stabilizer Legs": CRLocationData(
    code=175,
    ram_addr=CRRamData(0x803BFC27, bit_position=4),
    type = "Part Use"
  ),
  "Use Short Thrust Legs": CRLocationData(
    code=176,
    ram_addr=CRRamData(0x803BFC27, bit_position=5),
    type = "Part Use"
  ),
  "Use Long Thrust Legs": CRLocationData(
    code=177,
    ram_addr=CRRamData(0x803BFC27, bit_position=6),
    type = "Part Use"
  ),
  "Use Quick Jump Legs": CRLocationData(
    code=178,
    ram_addr=CRRamData(0x803BFC27, bit_position=7),
    type = "Part Use"
  ),
  "Use Feather Legs": CRLocationData(
    code=179,
    ram_addr=CRRamData(0x803BFC26, bit_position=0),
    type = "Part Use"
  ),
  "Use Wide Jump Legs": CRLocationData(
    code=180,
    ram_addr=CRRamData(0x803BFC26, bit_position=1),
    type = "Part Use"
  ),
  "Use Can Legs": CRLocationData(
    code=181,
    ram_addr=CRRamData(0x803BFC26, bit_position=2),
    type = "Part Use"
  ),
  "Use Booster Legs": CRLocationData(
    code=182,
    ram_addr=CRRamData(0x803BFC26, bit_position=3),
    type = "Part Use"
  ),
  "Use Swallow Legs": CRLocationData(
    code=183,
    ram_addr=CRRamData(0x803BFC26, bit_position=4),
    illegal=True,
    type = "Part Use"
  ),
  "Use Raven Legs": CRLocationData(
    code=184,
    ram_addr=CRRamData(0x803BFC26, bit_position=5),
    illegal=True,
    type = "Part Use"
  ),
  "Use Eclipse Legs": CRLocationData(
    code=185,
    ram_addr=CRRamData(0x803BFC26, bit_position=6),
    illegal=True,
    type = "Part Use"
  ),
  "Use Ultimate Legs": CRLocationData(
    code=186,
    ram_addr=CRRamData(0x803BFC26, bit_position=7),
    illegal=True,
    type = "Part Use"
  )
}

# Each battle counts as a check
BATTLE_TABLE: dict[str, CRLocationData] = {
    "Chapter 1 - VS Bandit #1": CRLocationData(
        code=261,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 1,
        parent_region = "Chapter 1 - Steel Hearts"
    ),
    "Chapter 1 - VS Bandit #2": CRLocationData(
        code=188,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 2,
        parent_region = "Chapter 1 - Steel Hearts"
    ),
    "Chapter 1 - VS Bandit #3": CRLocationData(
        code=189,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 3,
        parent_region = "Chapter 1 - Steel Hearts"
    ),
    "Chapter 1 - VS Bandit #4": CRLocationData(
        code=190,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 4,
        parent_region = "Chapter 1 - Steel Hearts"
    ),
    "Chapter 2 - VS Harry": CRLocationData(
        code=191,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 5,
        parent_region = "Chapter 2 - Test Hall Trials"
    ),
    "Chapter 2 - VS Gym Bot #1": CRLocationData(
        code=192,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 6,
        parent_region = "Chapter 2 - Test Hall Trials"
    ),
    "Chapter 2 - VS Gym Bot #2": CRLocationData(
        code=193,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 7,
        parent_region = "Chapter 2 - Test Hall Trials"
    ),
    "Chapter 2 - VS Gym Bot #3": CRLocationData(
        code=194,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 8,
        parent_region = "Chapter 2 - Test Hall Trials"
    ),
    "Chapter 2 - VS Gym Bot #4": CRLocationData(
        code=195,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 9,
        parent_region = "Chapter 2 - Test Hall Trials"
    ),
    "Chapter 2 - VS Thomas/Anthony": CRLocationData(
        code=196,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 10,
        parent_region = "Chapter 2 - Test Hall Trials"
    ),
    "Chapter 3 - VS Test Computer": CRLocationData(
        code=197,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 11,
        parent_region = "Chapter 3 - License Test"
    ),
    "Chapter 4 - VS Carmen": CRLocationData(
        code=198,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 12,
        parent_region = "Chapter 4 - Family Matters"
    ),
    "Chapter 4 - VS Walt & Carmen": CRLocationData(
        code=199,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 13,
        parent_region = "Chapter 4 - Family Matters"
    ),
    "Chapter 5 - VS Evil & Bubble": CRLocationData(
        code=200,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 14,
        parent_region = "Chapter 5 - Shiner Style"
    ),
    "Chapter 5 - VS Paulie": CRLocationData(
        code=201,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 15,
        parent_region = "Chapter 5 - Shiner Style"
    ),
    "Chapter 5 - VS Walt": CRLocationData(
        code=202,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 16,
        parent_region = "Chapter 5 - Shiner Style"
    ),
    "Chapter 5 - VS Harry": CRLocationData(
        code=203,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 17,
        parent_region = "Chapter 5 - Shiner Style"
    ),
    "Chapter 5 - VS Shiner": CRLocationData(
        code=204,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 18,
        parent_region = "Chapter 5 - Shiner Style"
    ),
    "Chapter 6 - VS Will": CRLocationData(
        code=205,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 19,
        parent_region = "Chapter 6 - Gym Tourney"
    ),
    "Chapter 6 - VS Don": CRLocationData(
        code=206,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 20,
        parent_region = "Chapter 6 - Gym Tourney"
    ),
    "Chapter 6 - VS Mary": CRLocationData(
        code=207,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 21,
        parent_region = "Chapter 6 - Gym Tourney"
    ),
    "Chapter 6 - VS Evil": CRLocationData(
        code=208,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 22,
        parent_region = "Chapter 6 - Gym Tourney"
    ),
    "Chapter 6 - VS Marcia": CRLocationData(
        code=209,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 23,
        parent_region = "Chapter 6 - Gym Tourney"
    ),
    "Chapter 7 - VS Z Lackey #1": CRLocationData(
        code=210,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 24,
        parent_region = "Chapter 7 - Lab Guard Duty"
    ),
    "Chapter 7 - VS Z Lackey #2": CRLocationData(
        code=211,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 25,
        parent_region = "Chapter 7 - Lab Guard Duty"
    ),
    "Chapter 7 - VS Z Lackey #3": CRLocationData(
        code=212,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 26,
        parent_region = "Chapter 7 - Lab Guard Duty"
    ),
    "Chapter 7 - VS Eliza": CRLocationData(
        code=213,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 27,
        parent_region = "Chapter 7 - Lab Guard Duty"
    ),
    "Chapter 8 - VS Rahu": CRLocationData(
        code=214,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 28,
        parent_region = "Chapter 8 - Rahu Appears"
    ),
    "Chapter 8 - VS Sergei": CRLocationData(
        code=215,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 29,
        parent_region = "Chapter 8 - Rahu Appears"
    ),
    "Chapter 9 - VS Will & Wendy": CRLocationData(
        code=216,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 30,
        parent_region = "Chapter 9 - Police 2v2"
    ),
    "Chapter 9 - VS Thomas & Anthony": CRLocationData(
        code=217,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 31,
        parent_region = "Chapter 9 - Police 2v2"
    ),
    "Chapter 9 - VS Police Officer Duo": CRLocationData(
        code=218,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 32,
        parent_region = "Chapter 9 - Police 2v2"
    ),
    "Chapter 9 - VS Walt & Carmen": CRLocationData(
        code=219,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 33,
        parent_region = "Chapter 9 - Police 2v2"
    ),
    "Chapter 9 - VS Bogey & Waiter": CRLocationData(
        code=220,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 34,
        parent_region = "Chapter 9 - Police 2v2"
    ),
    "Chapter 9 - VS Mira & Roy": CRLocationData(
        code=221,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 35,
        parent_region = "Chapter 9 - Police 2v2"
    ),
    "Chapter 9 - VS Evil": CRLocationData(
        code=222,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 36,
        parent_region = "Chapter 9 - Police 2v2"
    ),
    "Chapter 9 - VS Linda & Ernest": CRLocationData(
        code=223,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 37,
        parent_region = "Chapter 9 - Police 2v2"
    ),
    "Chapter 10 - VS Police Officer #1": CRLocationData(
        code=224,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 38,
        parent_region = "Chapter 10 - Secret Police"
    ),
    "Chapter 10 - VS Police Officer #2": CRLocationData(
        code=225,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 39,
        parent_region = "Chapter 10 - Secret Police"
    ),
    "Chapter 10 - VS Linda": CRLocationData(
        code=226,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 40,
        parent_region = "Chapter 10 - Secret Police"
    ),
    "Chapter 10 - VS Roy": CRLocationData(
        code=227,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 41,
        parent_region = "Chapter 10 - Secret Police"
    ),
    "Chapter 10 - VS Mira": CRLocationData(
        code=228,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 42,
        parent_region = "Chapter 10 - Secret Police"
    ),
    "Chapter 10 - VS Police Chief": CRLocationData(
        code=229,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 43,
        parent_region = "Chapter 10 - Secret Police"
    ),
    "Chapter 10 - VS S-Rank Computer": CRLocationData(
        code=230,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 44,
        parent_region = "Chapter 10 - Secret Police"
    ),
    "Chapter 11 - VS Isabella": CRLocationData(
        code=231,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 45,
        parent_region = "Chapter 11 - Rahu Returns"
    ),
    "Chapter 11 - VS Oboro & Sergei": CRLocationData(
        code=232,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 46,
        parent_region = "Chapter 11 - Rahu Returns"
    ),
    "Chapter 12 - VS Z Lackey #1": CRLocationData(
        code=233,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 47,
        parent_region = "Chapter 12 - To The Outside"
    ),
    "Chapter 12 - VS Shiner": CRLocationData(
        code=234,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 48,
        parent_region = "Chapter 12 - To The Outside"
    ),
    "Chapter 12 - VS Z Lackey #2": CRLocationData(
        code=235,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 49,
        parent_region = "Chapter 12 - To The Outside"
    ),
    "Chapter 12 - VS Z Lackey #3": CRLocationData(
        code=236,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 50,
        parent_region = "Chapter 12 - To The Outside"
    ),
    "Chapter 12 - VS Z Lackey #4": CRLocationData(
        code=237,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 51,
        parent_region = "Chapter 12 - To The Outside"
    ),
    "Chapter 12 - VS Z Tech #1": CRLocationData(
        code=238,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 52,
        parent_region = "Chapter 12 - To The Outside"
    ),
    "Chapter 12 - VS Z Tech #2": CRLocationData(
        code=239,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 53,
        parent_region = "Chapter 12 - To The Outside"
    ),
    "Chapter 12 - VS Z Lackey Duo #1": CRLocationData(
        code=240,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 54,
        parent_region = "Chapter 12 - To The Outside"
    ),
    "Chapter 12 - VS Z Lackey Duo #2": CRLocationData(
        code=241,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 55,
        parent_region = "Chapter 12 - To The Outside"
    ),
    "Chapter 12 - VS Oboro": CRLocationData(
        code=242,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 56,
        parent_region = "Chapter 12 - To The Outside"
    ),
    "Chapter 12 - VS Rahu II": CRLocationData(
        code=243,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 57,
        parent_region = "Chapter 12 - To The Outside"
    ),
    "Chapter 13 - VS Z Lackey": CRLocationData(
        code=244,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 58,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - VS Z Lackey Duo": CRLocationData(
        code=245,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 59,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 3": CRLocationData(
        code=246,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 60,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 4": CRLocationData(
        code=247,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 61,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 5": CRLocationData(
        code=248,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 62,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 6": CRLocationData(
        code=249,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 63,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 7": CRLocationData(
        code=250,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 64,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 8": CRLocationData(
        code=251,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 65,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 9": CRLocationData(
        code=252,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 66,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 10": CRLocationData(
        code=253,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 67,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 11": CRLocationData(
        code=254,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 68,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 12": CRLocationData(
        code=255,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 69,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 13": CRLocationData(
        code=256,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 70,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 14": CRLocationData(
        code=257,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 71,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 15": CRLocationData(
        code=258,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 72,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 16": CRLocationData(
        code=259,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 73,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
    "Chapter 13 - Amusement Battle 17": CRLocationData(
        code=260,
        ram_addr=CRRamData(BATTLE_COUNTER_ADDR, bit_position=1, ram_byte_size=8),
        type = "Battle Win",
        battle_number = 74,
        parent_region = "Chapter 13 - Rahu's Amusement"
    ),
}

#CHAPTER_COUNTER: dict[str, CRLocationData] = {
#   "Current Chapter": CRLocationData(
#      code=None,
#      ram_addr=CRRamData(0x803BE7A7, bit_position=1, ram_byte_size=8)
#   )
#}

RAHU_DEFEATED: dict[str, CRLocationData] = {
   "Rahu III Defeated": CRLocationData(
      code=None,
      ram_addr=CRRamData(0x803BE7A7, bit_position=0, ram_byte_size=8)
   )
}

LOCATION_TABLE: dict[str, CRLocationData] = {
  **PART_USE,
  **BATTLE_TABLE,
#  **CHAPTER_COUNTER,
  **RAHU_DEFEATED
}

#SELF_LOCATIONS_TO_RECV: list[int] = [
#    CRLocation.get_apid(value.code) for value in LOCATION_TABLE.values() if value.remote_only]
