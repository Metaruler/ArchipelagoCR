#Checks
from typing import NamedTuple, Optional
from .helpers import CRRamData
from BaseClasses import Location, Region

class CRLocationData(NamedTuple):
  code:Optional[int]
  ram_addr: Optional[CRRamData] = None
  illegal: bool = False

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
    ram_addr=CRRamData(0x803BFBA7, bit_position=1)
  ),
  "Use Splendor": CRLocationData(
    code=2,
    ram_addr=CRRamData(0x803BFBA7, bit_position=2)
  ),
  "Use Glory": CRLocationData(
    code=3,
    ram_addr=CRRamData(0x803BFBA7, bit_position=3)
  ),
  "Use Milky Way": CRLocationData(
    code=4,
    ram_addr=CRRamData(0x803BFBA7, bit_position=4)
  ),
  "Use Earth": CRLocationData(
    code=5,
    ram_addr=CRRamData(0x803BFBA7, bit_position=5)
  ),
  "Use Sol": CRLocationData(
    code=6,
    ram_addr=CRRamData(0x803BFBA7, bit_position=6)
  ),
  "Use Metal Ape": CRLocationData(
    code=7,
    ram_addr=CRRamData(0x803BFBA7, bit_position=7)
  ),
  "Use Metal Bear": CRLocationData(
    code=8,
    ram_addr=CRRamData(0x803BFBA7, bit_position=8)
  ),
  "Use Metal Ox": CRLocationData(
    code=9,
    ram_addr=CRRamData(0x803BFBA6, bit_position=1)
  ),
  "Use Swift": CRLocationData(
    code=10,
    ram_addr=CRRamData(0x803BFBA6, bit_position=2)
  ),
  "Use Shrike": CRLocationData(
    code=11,
    ram_addr=CRRamData(0x803BFBA6, bit_position=3)
  ),
  "Use Peregrine": CRLocationData(
    code=12,
    ram_addr=CRRamData(0x803BFBA6, bit_position=4)
  ),
  "Use Javelin": CRLocationData(
    code=13,
    ram_addr=CRRamData(0x803BFBA6, bit_position=5)
  ),
  "Use Glaive": CRLocationData(
    code=14,
    ram_addr=CRRamData(0x803BFBA6, bit_position=6)
  ),
  "Use Halberd": CRLocationData(
    code=15,
    ram_addr=CRRamData(0x803BFBA6, bit_position=7)
  ),
  "Use Criminal": CRLocationData(
    code=16,
    ram_addr=CRRamData(0x803BFBA6, bit_position=8)
  ),
  "Use Buggy": CRLocationData(
    code=17,
    ram_addr=CRRamData(0x803BFBA5, bit_position=1)
  ),
  "Use Juggler": CRLocationData(
    code=18,
    ram_addr=CRRamData(0x803BFBA5, bit_position=2)
  ),
  "Use Defender": CRLocationData(
    code=19,
    ram_addr=CRRamData(0x803BFBA5, bit_position=3)
  ),
  "Use Seeker": CRLocationData(
    code=20,
    ram_addr=CRRamData(0x803BFBA5, bit_position=4)
  ),
  "Use Breaker": CRLocationData(
    code=21,
    ram_addr=CRRamData(0x803BFBA5, bit_position=5)
  ),
  "Use Seal Head": CRLocationData(
    code=22,
    ram_addr=CRRamData(0x803BFBA5, bit_position=6)
  ),
  "Use Dour Head": CRLocationData(
    code=23,
    ram_addr=CRRamData(0x803BFBA5, bit_position=7)
  ),
  "Use Tank Head": CRLocationData(
    code=24,
    ram_addr=CRRamData(0x803BFBA5, bit_position=8)
  ),
  "Use Ray Legend": CRLocationData(
    code=25,
    ram_addr=CRRamData(0x803BFBA4, bit_position=1),
    illegal=True
  ),
  "Use Oil Can": CRLocationData(
    code=26,
    ram_addr=CRRamData(0x803BFBA4, bit_position=2)
  ),
  "Use Ray Warrior": CRLocationData(
    code=27,
    ram_addr=CRRamData(0x803BFBA4, bit_position=3),
    illegal=True
  ),
  "Use Rakansen": CRLocationData(
    code=28,
    ram_addr=CRRamData(0x803BFBA4, bit_position=4),
    illegal=True
  ),
  "Use Ruhiel": CRLocationData(
    code=29,
    ram_addr=CRRamData(0x803BFBA4, bit_position=5),
    illegal=True
  ),
  "Use Athena": CRLocationData(
    code=30,
    ram_addr=CRRamData(0x803BFBA4, bit_position=6),
    illegal=True
  ),
  "Use Rahu I": CRLocationData(
    code=31,
    ram_addr=CRRamData(0x803BFBA4, bit_position=7),
    illegal=True
  ),
  "Use Rahu II": CRLocationData(
    code=32,
    ram_addr=CRRamData(0x803BFBA4, bit_position=8),
    illegal=True
  ),
  "Use Rahu III": CRLocationData(
    code=33,
    ram_addr=CRRamData(0x803BFBAB, bit_position=1),
    illegal=True
  ),
  "Use Chickenheart": CRLocationData(
    code=34,
    ram_addr=CRRamData(0x803BFBAB, bit_position=2)
  ),
  "Use Basic Gun": CRLocationData(
    code=35,
    ram_addr=CRRamData(0x803BFBC7, bit_position=1)
  ),
  "Use 3-Way Gun": CRLocationData(
    code=36,
    ram_addr=CRRamData(0x803BFBC7, bit_position=2)
  ),
  "Use Gatling Gun": CRLocationData(
    code=37,
    ram_addr=CRRamData(0x803BFBC7, bit_position=3)
  ),
  "Use Vertical Gun": CRLocationData(
    code=38,
    ram_addr=CRRamData(0x803BFBC7, bit_position=4)
  ),
  "Use Sniper Gun": CRLocationData(
    code=39,
    ram_addr=CRRamData(0x803BFBC7, bit_position=5)
  ),
  "Use Stun Gun": CRLocationData(
    code=40,
    ram_addr=CRRamData(0x803BFBC7, bit_position=6)
  ),
  "Use Hornet Gun": CRLocationData(
    code=41,
    ram_addr=CRRamData(0x803BFBC7, bit_position=7)
  ),
  "Use Flame Gun": CRLocationData(
    code=42,
    ram_addr=CRRamData(0x803BFBC7, bit_position=8)
  ),
  "Use Dragon Gun": CRLocationData(
    code=43,
    ram_addr=CRRamData(0x803BFBC6, bit_position=1)
  ),
  "Use Splash Gun": CRLocationData(
    code=44,
    ram_addr=CRRamData(0x803BFBC6, bit_position=2)
  ),
  "Use Left Arc Gun": CRLocationData(
    code=45,
    ram_addr=CRRamData(0x803BFBC6, bit_position=3)
  ),
  "Use Right Arc Gun": CRLocationData(
    code=46,
    ram_addr=CRRamData(0x803BFBC6, bit_position=4)
  ),
  "Use Shotgun Gun": CRLocationData(
    code=47,
    ram_addr=CRRamData(0x803BFBC6, bit_position=5)
  ),
  "Use Rayfall Gun": CRLocationData(
    code=48,
    ram_addr=CRRamData(0x803BFBC6, bit_position=6)
  ),
  "Use Bubble Gun": CRLocationData(
    code=49,
    ram_addr=CRRamData(0x803BFBC6, bit_position=7)
  ),
  "Use Eagle Gun": CRLocationData(
    code=50,
    ram_addr=CRRamData(0x803BFBC6, bit_position=8)
  ),
  "Use V Laser Gun": CRLocationData(
    code=51,
    ram_addr=CRRamData(0x803BFBC5, bit_position=1)
  ),
  "Use Magnum Gun": CRLocationData(
    code=52,
    ram_addr=CRRamData(0x803BFBC5, bit_position=2)
  ),
  "Use Needle Gun": CRLocationData(
    code=53,
    ram_addr=CRRamData(0x803BFBC5, bit_position=3)
  ),
  "Use Starshot Gun": CRLocationData(
    code=54,
    ram_addr=CRRamData(0x803BFBC5, bit_position=4)
  ),
  "Use Glider Gun": CRLocationData(
    code=55,
    ram_addr=CRRamData(0x803BFBC5, bit_position=5)
  ),
  "Use Homing Star Gun": CRLocationData(
    code=56,
    ram_addr=CRRamData(0x803BFBC5, bit_position=6)
  ),
  "Use Trap Gun": CRLocationData(
    code=57,
    ram_addr=CRRamData(0x803BFBC5, bit_position=7)
  ),
  "Use Drill Gun": CRLocationData(
    code=58,
    ram_addr=CRRamData(0x803BFBC5, bit_position=8)
  ),
  "Use Titan Gun": CRLocationData(
    code=59,
    ram_addr=CRRamData(0x803BFBC4, bit_position=1)
  ),
  "Use Claw Gun": CRLocationData(
    code=60,
    ram_addr=CRRamData(0x803BFBC4, bit_position=2)
  ),
  "Use Knuckle Gun": CRLocationData(
    code=61,
    ram_addr=CRRamData(0x803BFBC4, bit_position=3)
  ),
  "Use Afterburner Gun": CRLocationData(
    code=62,
    ram_addr=CRRamData(0x803BFBC4, bit_position=4)
  ),
  "Use Blade Gun": CRLocationData(
    code=63,
    ram_addr=CRRamData(0x803BFBC4, bit_position=5)
  ),
  "Use Meteor Storm Gun": CRLocationData(
    code=64,
    ram_addr=CRRamData(0x803BFBC4, bit_position=6)
  ),
  "Use Twin Fang Gun": CRLocationData(
    code=65,
    ram_addr=CRRamData(0x803BFBC4, bit_position=7)
  ),
  "Use Gravity Gun": CRLocationData(
    code=66,
    ram_addr=CRRamData(0x803BFBC4, bit_position=8)
  ),
  "Use Phoenix Gun": CRLocationData(
    code=67,
    ram_addr=CRRamData(0x803BFBCB, bit_position=1)
  ),
  "Use Can Gun": CRLocationData(
    code=68,
    ram_addr=CRRamData(0x803BFBCB, bit_position=2)
  ),
  "Use Left Pulse Gun": CRLocationData(
    code=69,
    ram_addr=CRRamData(0x803BFBCB, bit_position=3)
  ),
  "Use Right Pulse Gun": CRLocationData(
    code=70,
    ram_addr=CRRamData(0x803BFBCB, bit_position=4)
  ),
  "Use Sword Storm Gun": CRLocationData(
    code=71,
    ram_addr=CRRamData(0x803BFBCB, bit_position=5)
  ),
  "Use Ion Gun": CRLocationData(
    code=72,
    ram_addr=CRRamData(0x803BFBCB, bit_position=6)
  ),
  "Use Flare Gun": CRLocationData(
    code=73,
    ram_addr=CRRamData(0x803BFBCB, bit_position=7)
  ),
  "Use Left 5-Way Gun": CRLocationData(
    code=74,
    ram_addr=CRRamData(0x803BFBCB, bit_position=8)
  ),
  "Use Right 5-Way Gun": CRLocationData(
    code=75,
    ram_addr=CRRamData(0x803BFBCA, bit_position=1)
  ),
  "Use Halo Gun": CRLocationData(
    code=76,
    ram_addr=CRRamData(0x803BFBCA, bit_position=2)
  ),
  "Use Wave Laser Gun": CRLocationData(
    code=77,
    ram_addr=CRRamData(0x803BFBCA, bit_position=3),
    illegal=True
  ),
  "Use X Laser Gun": CRLocationData(
    code=78,
    ram_addr=CRRamData(0x803BFBCA, bit_position=4),
    illegal=True
  ),
  "Use Crystal Strike Gun": CRLocationData(
    code=79,
    ram_addr=CRRamData(0x803BFBCA, bit_position=5),
    illegal=True
  ),
  "Use Wyrm Gun": CRLocationData(
    code=80,
    ram_addr=CRRamData(0x803BFBCA, bit_position=6),
    illegal=True
  ),
  "Use Raptor Gun": CRLocationData(
    code=81,
    ram_addr=CRRamData(0x803BFBCA, bit_position=7),
    illegal=True
  ),
  "Use Waxing Arc Gun": CRLocationData(
    code=82,
    ram_addr=CRRamData(0x803BFBCA, bit_position=8),
    illegal=True
  ),
  "Use Waning Arc Gun": CRLocationData(
    code=83,
    ram_addr=CRRamData(0x803BFBC9, bit_position=1),
    illegal=True
  ),
  "Use Rahu I Gun": CRLocationData(
    code=84,
    ram_addr=CRRamData(0x803BFBC9, bit_position=2),
    illegal=True
  ),
  "Use Rahu II Gun": CRLocationData(
    code=85,
    ram_addr=CRRamData(0x803BFBC9, bit_position=3),
    illegal=True
  ),
  "Use Rahu III Gun": CRLocationData(
    code=86,
    ram_addr=CRRamData(0x803BFBC9, bit_position=4),
    illegal=True
  ),
  "Use Standard Bomb": CRLocationData(
    code=87,
    ram_addr=CRRamData(0x803BFBE7, bit_position=1)
  ),
  "Use Standard F Bomb": CRLocationData(
    code=88,
    ram_addr=CRRamData(0x803BFBE7, bit_position=2)
  ),
  "Use Standard S Bomb": CRLocationData(
    code=89,
    ram_addr=CRRamData(0x803BFBE7, bit_position=3)
  ),
  "Use Wave Bomb": CRLocationData(
    code=90,
    ram_addr=CRRamData(0x803BFBE7, bit_position=4)
  ),
  "Use Straight G Bomb": CRLocationData(
    code=91,
    ram_addr=CRRamData(0x803BFBE7, bit_position=5)
  ),
  "Use Straight S Bomb": CRLocationData(
    code=92,
    ram_addr=CRRamData(0x803BFBE7, bit_position=6)
  ),
  "Use Straight T Bomb": CRLocationData(
    code=93,
    ram_addr=CRRamData(0x803BFBE7, bit_position=7)
  ),
  "Use Right Flank H Bomb": CRLocationData(
    code=94,
    ram_addr=CRRamData(0x803BFBE7, bit_position=8)
  ),
  "Use Left Flank H Bomb": CRLocationData(
    code=95,
    ram_addr=CRRamData(0x803BFBE6, bit_position=1)
  ),
  "Use Right Wave Bomb": CRLocationData(
    code=96,
    ram_addr=CRRamData(0x803BFBE6, bit_position=2)
  ),
  "Use Left Wave Bomb": CRLocationData(
    code=97,
    ram_addr=CRRamData(0x803BFBE6, bit_position=3)
  ),
  "Use Burrow D Bomb": CRLocationData(
    code=98,
    ram_addr=CRRamData(0x803BFBE6, bit_position=4)
  ),
  "Use Burrow P Bomb": CRLocationData(
    code=99,
    ram_addr=CRRamData(0x803BFBE6, bit_position=5)
  ),
  "Use Freeze Bomb": CRLocationData(
    code=100,
    ram_addr=CRRamData(0x803BFBE6, bit_position=6)
  ),
  "Use Tomahawk B Bomb": CRLocationData(
    code=101,
    ram_addr=CRRamData(0x803BFBE6, bit_position=7)
  ),
  "Use Tomahawk G Bomb": CRLocationData(
    # TODO FIX NUMBERING
    code=187,
    ram_addr=CRRamData(0x803BFBE6, bit_position=8)
  ),
  "Use Gemini B Bomb": CRLocationData(
    code=102,
    ram_addr=CRRamData(0x803BFBE5, bit_position=1)
  ),
  "Use Gemini P Bomb": CRLocationData(
    code=103,
    ram_addr=CRRamData(0x803BFBE5, bit_position=2)
  ),
  "Use Submarine D Bomb": CRLocationData(
    code=104,
    ram_addr=CRRamData(0x803BFBE5, bit_position=3)
  ),
  "Use Submarine P Bomb": CRLocationData(
    code=105,
    ram_addr=CRRamData(0x803BFBE5, bit_position=4)
  ),
  "Use Crescent P Bomb": CRLocationData(
    code=106,
    ram_addr=CRRamData(0x803BFBE5, bit_position=5)
  ),
  "Use Crescent C Bomb": CRLocationData(
    code=107,
    ram_addr=CRRamData(0x803BFBE5, bit_position=6)
  ),
  "Use Dual Bomb": CRLocationData(
    code=108,
    ram_addr=CRRamData(0x803BFBE5, bit_position=7)
  ),
  "Use Dual C Bomb": CRLocationData(
    code=109,
    ram_addr=CRRamData(0x803BFBE5, bit_position=8)
  ),
  "Use Acrobat Bomb": CRLocationData(
    code=110,
    ram_addr=CRRamData(0x803BFBE4, bit_position=1)
  ),
  "Use Delta Bomb": CRLocationData(
    code=111,
    ram_addr=CRRamData(0x803BFBE4, bit_position=2)
  ),
  "Use Wall Bomb": CRLocationData(
    code=112,
    ram_addr=CRRamData(0x803BFBE4, bit_position=3)
  ),
  "Use Smash Bomb": CRLocationData(
    code=113,
    ram_addr=CRRamData(0x803BFBE4, bit_position=4)
  ),
  "Use Double Mine Bomb": CRLocationData(
    code=114,
    ram_addr=CRRamData(0x803BFBE4, bit_position=5)
  ),
  "Use Geo Trap Bomb": CRLocationData(
    code=115,
    ram_addr=CRRamData(0x803BFBE4, bit_position=6)
  ),
  "Use Titan Bomb": CRLocationData(
    code=116,
    ram_addr=CRRamData(0x803BFBE4, bit_position=7)
  ),
  "Use Can Bomb": CRLocationData(
    code=117,
    ram_addr=CRRamData(0x803BFBE4, bit_position=8)
  ),
  "Use Standard K Bomb": CRLocationData(
    code=118,
    ram_addr=CRRamData(0x803BFBEB, bit_position=1)
  ),
  "Use Submarine K Bomb": CRLocationData(
    code=119,
    ram_addr=CRRamData(0x803BFBEB, bit_position=2)
  ),
  "Use Crescent K Bomb": CRLocationData(
    code=120,
    ram_addr=CRRamData(0x803BFBEB, bit_position=3)
  ),
  "Use Standard X Bomb": CRLocationData(
    code=121,
    ram_addr=CRRamData(0x803BFBEB, bit_position=4)
  ),
  "Use Treble Bomb": CRLocationData(
    code=122,
    ram_addr=CRRamData(0x803BFBEB, bit_position=5),
    illegal=True
  ),
  "Use Wyvern Bomb": CRLocationData(
    code=123,
    ram_addr=CRRamData(0x803BFBEB, bit_position=6),
    illegal=True
  ),
  "Use Waxing Arc Bomb": CRLocationData(
    code=124,
    ram_addr=CRRamData(0x803BFBEB, bit_position=7),
    illegal=True
  ),
  "Use Waning Arc Bomb": CRLocationData(
    code=125,
    ram_addr=CRRamData(0x803BFBEB, bit_position=8),
    illegal=True
  ),
  "Use Grand Cross Bomb": CRLocationData(
    code=126,
    ram_addr=CRRamData(0x803BFBEA, bit_position=1),
    illegal=True
  ),
  "Use Standard Pod": CRLocationData(
    code=127,
    ram_addr=CRRamData(0x803BFC07, bit_position=1)
  ),
  "Use Seeker F Pod": CRLocationData(
    code=128,
    ram_addr=CRRamData(0x803BFC07, bit_position=2)
  ),
  "Use Seeker G Pod": CRLocationData(
    code=129,
    ram_addr=CRRamData(0x803BFC07, bit_position=3)
  ),
  "Use Speed D Pod": CRLocationData(
    code=130,
    ram_addr=CRRamData(0x803BFC07, bit_position=4)
  ),
  "Use Speed P Pod": CRLocationData(
    code=131,
    ram_addr=CRRamData(0x803BFC07, bit_position=5)
  ),
  "Use Cockroach G Pod": CRLocationData(
    code=132,
    ram_addr=CRRamData(0x803BFC07, bit_position=6)
  ),
  "Use Cockroach H Pod": CRLocationData(
    code=133,
    ram_addr=CRRamData(0x803BFC07, bit_position=7)
  ),
  "Use Dolphin Pod": CRLocationData(
    code=134,
    ram_addr=CRRamData(0x803BFC07, bit_position=8)
  ),
  "Use Dolphin G Pod": CRLocationData(
    code=135,
    ram_addr=CRRamData(0x803BFC06, bit_position=1)
  ),
  "Use Spider Pod": CRLocationData(
    code=136,
    ram_addr=CRRamData(0x803BFC06, bit_position=2)
  ),
  "Use Spider G Pod": CRLocationData(
    code=137,
    ram_addr=CRRamData(0x803BFC06, bit_position=3)
  ),
  "Use Sky Freeze Pod": CRLocationData(
    code=138,
    ram_addr=CRRamData(0x803BFC06, bit_position=4)
  ),
  "Use Ground Freeze Pod": CRLocationData(
    code=139,
    ram_addr=CRRamData(0x803BFC06, bit_position=5)
  ),
  "Use Feint F Pod": CRLocationData(
    code=140,
    ram_addr=CRRamData(0x803BFC06, bit_position=6)
  ),
  "Use Feint G Pod": CRLocationData(
    code=141,
    ram_addr=CRRamData(0x803BFC06, bit_position=7)
  ),
  "Use Float F Pod": CRLocationData(
    code=142,
    ram_addr=CRRamData(0x803BFC06, bit_position=8)
  ),
  "Use Jumping B Pod": CRLocationData(
    code=143,
    ram_addr=CRRamData(0x803BFC05, bit_position=1)
  ),
  "Use Jumping G Pod": CRLocationData(
    code=144,
    ram_addr=CRRamData(0x803BFC05, bit_position=2)
  ),
  "Use Diving Pod": CRLocationData(
    code=145,
    ram_addr=CRRamData(0x803BFC05, bit_position=3)
  ),
  "Use Wave Pod": CRLocationData(
    code=146,
    ram_addr=CRRamData(0x803BFC05, bit_position=4)
  ),
  "Use Satellite Pod": CRLocationData(
    code=147,
    ram_addr=CRRamData(0x803BFC05, bit_position=5)
  ),
  "Use Satellite H Pod": CRLocationData(
    code=148,
    ram_addr=CRRamData(0x803BFC05, bit_position=6)
  ),
  "Use Beast F Pod": CRLocationData(
    code=149,
    ram_addr=CRRamData(0x803BFC05, bit_position=7)
  ),
  "Use Trio H Pod": CRLocationData(
    code=150,
    ram_addr=CRRamData(0x803BFC05, bit_position=8)
  ),
  "Use Wall Pod": CRLocationData(
    code=151,
    ram_addr=CRRamData(0x803BFC04, bit_position=1)
  ),
  "Use Reflection Pod": CRLocationData(
    code=152,
    ram_addr=CRRamData(0x803BFC04, bit_position=2)
  ),
  "Use Caboose C Pod": CRLocationData(
    code=153,
    ram_addr=CRRamData(0x803BFC04, bit_position=3)
  ),
  "Use Caboose T Pod": CRLocationData(
    code=154,
    ram_addr=CRRamData(0x803BFC04, bit_position=4)
  ),
  "Use Twin Flank F Pod": CRLocationData(
    code=155,
    ram_addr=CRRamData(0x803BFC04, bit_position=5)
  ),
  "Use Twin Flank G Pod": CRLocationData(
    code=156,
    ram_addr=CRRamData(0x803BFC04, bit_position=6)
  ),
  "Use Umbrella Pod": CRLocationData(
    code=157,
    ram_addr=CRRamData(0x803BFC04, bit_position=7)
  ),
  "Use Throwing D Pod": CRLocationData(
    code=158,
    ram_addr=CRRamData(0x803BFC04, bit_position=8)
  ),
  "Use Throwing P Pod": CRLocationData(
    code=159,
    ram_addr=CRRamData(0x803BFC0B, bit_position=1)
  ),
  "Use Double Wave Pod": CRLocationData(
    code=160,
    ram_addr=CRRamData(0x803BFC0B, bit_position=2)
  ),
  "Use Titan Pod": CRLocationData(
    code=161,
    ram_addr=CRRamData(0x803BFC0B, bit_position=3)
  ),
  "Use Can Pod": CRLocationData(
    code=162,
    ram_addr=CRRamData(0x803BFC0B, bit_position=4)
  ),
  "Use Standard F Pod": CRLocationData(
    code=163,
    ram_addr=CRRamData(0x803BFC0B, bit_position=5)
  ),
  "Use Caboose X Pod": CRLocationData(
    code=164,
    ram_addr=CRRamData(0x803BFC0B, bit_position=6)
  ),
  "Use Cheetah Pod": CRLocationData(
    code=165,
    ram_addr=CRRamData(0x803BFC0B, bit_position=7),
    illegal=True
  ),
  "Use Wolf Spider Pod": CRLocationData(
    code=166,
    ram_addr=CRRamData(0x803BFC0B, bit_position=8),
    illegal=True
  ),
  "Use Orca Pod": CRLocationData(
    code=167,
    ram_addr=CRRamData(0x803BFC0A, bit_position=1),
    illegal=True
  ),
  "Use Penumbra I Pod": CRLocationData(
    code=168,
    ram_addr=CRRamData(0x803BFC0A, bit_position=2),
    illegal=True
  ),
  "Use Penumbra II Pod": CRLocationData(
    code=169,
    ram_addr=CRRamData(0x803BFC0A, bit_position=3),
    illegal=True
  ),
  "Use Penumbra III Pod": CRLocationData(
    code=170,
    ram_addr=CRRamData(0x803BFC0A, bit_position=4),
    illegal=True
  ),
  "Use Standard Legs": CRLocationData(
    code=171,
    ram_addr=CRRamData(0x803BFC27, bit_position=1)
  ),
  "Use High Jump Legs": CRLocationData(
    code=172,
    ram_addr=CRRamData(0x803BFC27, bit_position=2)
  ),
  "Use Ground Legs": CRLocationData(
    code=173,
    ram_addr=CRRamData(0x803BFC27, bit_position=3)
  ),
  "Use Formula Legs": CRLocationData(
    code=174,
    ram_addr=CRRamData(0x803BFC27, bit_position=4)
  ),
  "Use Stabilizer Legs": CRLocationData(
    code=175,
    ram_addr=CRRamData(0x803BFC27, bit_position=5)
  ),
  "Use Short Thrust Legs": CRLocationData(
    code=176,
    ram_addr=CRRamData(0x803BFC27, bit_position=6)
  ),
  "Use Long Thrust Legs": CRLocationData(
    code=177,
    ram_addr=CRRamData(0x803BFC27, bit_position=7)
  ),
  "Use Quick Jump Legs": CRLocationData(
    code=178,
    ram_addr=CRRamData(0x803BFC27, bit_position=8)
  ),
  "Use Feather Legs": CRLocationData(
    code=179,
    ram_addr=CRRamData(0x803BFC26, bit_position=1)
  ),
  "Use Wide Jump Legs": CRLocationData(
    code=180,
    ram_addr=CRRamData(0x803BFC26, bit_position=2)
  ),
  "Use Can Legs": CRLocationData(
    code=181,
    ram_addr=CRRamData(0x803BFC26, bit_position=3)
  ),
  "Use Booster Legs": CRLocationData(
    code=182,
    ram_addr=CRRamData(0x803BFC26, bit_position=4)
  ),
  "Use Swallow Legs": CRLocationData(
    code=183,
    ram_addr=CRRamData(0x803BFC26, bit_position=5),
    illegal=True
  ),
  "Use Raven Legs": CRLocationData(
    code=184,
    ram_addr=CRRamData(0x803BFC26, bit_position=6),
    illegal=True
  ),
  "Use Eclipse Legs": CRLocationData(
    code=185,
    ram_addr=CRRamData(0x803BFC26, bit_position=7),
    illegal=True
  ),
  "Use Ultimate Legs": CRLocationData(
    code=186,
    ram_addr=CRRamData(0x803BFC26, bit_position=8),
    illegal=True
  )
}

# Each battle counts as a check
#BATTLE_COUNTER: dict[str, CRLocationData] = {
#  "Battles Won": CRLocationData(
#    code=None,
#    ram_addr=CRRamData(0x803BF9C9, bit_position=1, ram_byte_size=8)
#  )
#}

#CHAPTER_COUNTER: dict[str, CRLocationData] = {
#   "Current Chapter": CRLocationData(
#      code=None,
#      ram_addr=CRRamData(0x803BE7A7, bit_position=1, ram_byte_size=8)
#   )
#}

RAHU_DEFEATED: dict[str, CRLocationData] = {
   "Rahu III Defeated": CRLocationData(
      code=None,
      ram_addr=CRRamData(0x803BE7A7, bit_position=1, ram_byte_size=8)
   )
}

LOCATION_TABLE: dict[str, CRLocationData] = {
  **PART_USE,
#  **BATTLE_COUNTER,
#  **CHAPTER_COUNTER,
  **RAHU_DEFEATED
}

#SELF_LOCATIONS_TO_RECV: list[int] = [
#    CRLocation.get_apid(value.code) for value in LOCATION_TABLE.values() if value.remote_only]
