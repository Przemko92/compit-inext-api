from enum import Enum


class CompitHVACMode(Enum):
    """Enum for available HVAC modes."""

    HEAT = 0
    OFF = 1
    COOL = 2

class CompitParameter(Enum):
    """Enum for Compit device parameters."""
    
    PRESET_MODE = "__trybpracytermostatu"
    FAN_MODE = "__trybaero"
    HVAC_MODE = "__trybpracyinstalacji"
    CURRENT_TEMPERATURE = "__tpokojowa"
    TARGET_TEMPERATURE = "__tpokzadana"
    SET_TARGET_TEMPERATURE = "__tempzadpracareczna"

class CompitFanMode(Enum):
    """Enum for available fan modes."""

    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    HOLIDAY = 4
    AUTO = 5

class CompitPresetMode(Enum):
    """Enum for available preset modes."""
    
    AUTO = 0
    HOLIDAY = 1
    MANUAL = 2
    AWAY = 3