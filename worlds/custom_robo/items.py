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
