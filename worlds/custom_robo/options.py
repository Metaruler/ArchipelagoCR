from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions

class IllegalPartsEnabled(Choice):
    """Choose whether Illegal Parts are included for drops and checks (enabled by default)"""
    display_name = "Illegal Parts Enabled"
    internal_name = "illegal_parts_enabled"
    option_enabled = True
    option_disabled = False
    default = True

@dataclass
class CROptions(PerGameCommonOptions):
    illegal_parts_enabled: IllegalPartsEnabled
