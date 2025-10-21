from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Toggle

class IllegalPartsEnabled(Toggle):
    """Choose whether Illegal Parts are included for drops and checks"""
    display_name = "Illegal Parts Enabled"
    internal_name = "illegal_parts_enabled"

class StartingParts(Choice):
    """Choose what Robo Parts you start with"""
    display_name = "Starting Parts"
    internal_name = "starting_parts"
    option_standard = 0
    option_randomized = 1
    default = 0

@dataclass
class CROptions(PerGameCommonOptions):
    illegal_parts_enabled: IllegalPartsEnabled
    starting_parts: StartingParts
