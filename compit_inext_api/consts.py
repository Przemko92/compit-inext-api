from enum import Enum


class CompitHVACMode(Enum):
    """Enum for available HVAC modes."""

    HEAT = 0
    OFF = 1
    COOL = 2

class CompitParameter(Enum):
    """Enum for Compit device parameters."""

    ADDITIONAL_VENTILATION_ZONE = "__trybaero2"
    AEROKONFBYPASS = "__aerokonfbypass"
    AIRING_PROGRAM_ZONE_3 = "__a3programwietrzenia"
    AIRING_PROGRAM_ZONE_4 = "__a4programwietrzenia"
    AIRING_PROGRAM_ZONE_5 = "__a5prwietrz"
    DHW_CIRCULATION_MODE = "__cwucyrkpraca"
    BIOMAX_HEATING_SOURCE_OF_CORRECTION = "__pracakotla"
    BIOMAX_MIXER_MODE_ZONE_1 = "__m1praca"
    BIOMAX_MIXER_MODE_ZONE_2 = "__m2praca"
    BUFFER_MODE = "__tr_buf"
    CURRENT_TEMPERATURE = "__tpokojowa"
    DHW_MODE = "__dhwmode"
    DHW_OPERATING_MODE = "__trybprcwu"
    DHWC_CIRCULATION = "__cyrk_cwu"
    FAN_MODE = "__trybaero"
    HEATING_SOURCE_OF_CORRECTION = "__comode"
    HVAC_MODE = "__trybpracyinstalacji"
    LANGUAGE = "_jezyk"
    MIXER_MODE = "__pracamieszacza"
    NANO_MODE = "__nano_mode"
    PRESET_MODE = "__trybpracytermostatu"
    WORK_MODE = "__sezprinst"
    R470_OPERATING_MODE = "__mode"
    R480_DHW_CIRCULATION = "__cwu_cyrkulacja"
    R480_DHW_MODE = "__tryb_cwu"
    R480_OPERATING_MODE = "__praca_pc"
    R490_OPERATING_MODE = "__trprpompyciepla"
    R770_DHW_CIRCULATION_MODE = "__trybpracycyrkcwu"
    R770_DHW_OPERATING_MODE = "__trybpracycwu"
    R770_MIXER_MODE_ZONE_1 = "__trybmieszacza"
    R770_MIXER_MODE_ZONE_2 = "__trybmie2"
    R900_OPERATING_MODE = "__tr_pracy_pc"
    SECONDARY_HEATER_ZONE_3 = "__a3konfignagwt"
    SECONDARY_HEATER_ZONE_5 = "__a5trnagrzgl"
    SET_TARGET_TEMPERATURE = "__tempzadpracareczna"
    SOLAR_COMP_OPERATING_MODE = "__trybpracy"
    TARGET_TEMPERATURE = "__tpokzadana"    
    VENTILATION_COMFORT_ZONE = "__wentkomfort"
    VENTILATION_ECO_ZONE = "__wenteko"
    VENTILATION_HOLIDAY_MODE = "__wenturlop"

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

class CompitDevice(Enum):
    """Enum for Compit devices.

    The enum value is the device `Code`, so you can look up a device by code:
    `CompitDevice(223) -> CompitDevice.NANO_COLOR_2`.

    Each member also exposes:
    - `label`: original device name
    - `device_class`: device class id
    """

    label: str
    device_class: int

    def __new__(cls, label: str, code: int, device_class: int):
        obj = object.__new__(cls)
        obj._value_ = code
        obj.label = label
        obj.device_class = device_class
        return obj

    AF_1 = ("AF-1", 226, 48)
    BIOMAX742_2 = ("BioMax742", 36, 15)
    BIOMAX742 = ("BioMax742", 212, 15)
    BIOMAX772 = ("BioMax772", 75, 15)
    BIOMAX775 = ("BioMax775", 201, 15)
    BWC310 = ("BWC310", 14, 69)
    COMBO = ("COMBO", 227, 49)
    COMBO_PRO = ("COMBO PRO", 229, 37)
    EL750 = ("EL750", 210, 29)
    L2 = ("L2", 17, 12)
    NANO_COLOR = ("Nano Color", 12, 10)
    NANO_COLOR_2 = ("Nano Color 2", 223, 10)
    NANO_ONE = ("Nano One", 7, 10)
    R_900 = ("R 900", 224, 47)
    R350CWU = ("R350.CWU", 53, 36)
    R350M = ("R350.M", 221, 14)
    R350_T3 = ("R350 T3", 5, 14)
    R470 = ("r470", 34, 16)
    R480 = ("R480", 215, 43)
    R490 = ("r490", 92, 33)
    R770RS_R771RS = ("R770RS / R771RS", 91, 25)
    R810 = ("R810", 3, 14)
    R810_1 = ("R810", 222, 34)
    CO2_SHC = ("SHC", 27, 15)
    SOLARCOMP_951 = ("SolarComp 951", 44, 18)
    SOLARCOMP971 = ("SolarComp971", 45, 18)
    SPM_NANO_COLOR = ("SPM - Nano Color", 225, 27)
    SPM_NANO_COLOR2 = ("SPM - Nano Color2", 0, 46)
    SPM_NANO_COLOR2_1 = ("SPM - Nano Color2", 78, 46)