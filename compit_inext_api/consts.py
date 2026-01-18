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
    BIOMAX_CIRCULATION_MODE = "__trybcyrkulacji"
    BIOMAX_DHW_CIRCULATION_MODE = "__cwucyrkpraca"
    BIOMAX_DHW_MODE = "__cwupraca"
    BIOMAX_HEATING_SOURCE_OF_CORRECTION = "__pracakotla"
    BIOMAX_MIXER_MODE_ZONE_1 = "__m1praca"
    BIOMAX_MIXER_MODE_ZONE_2 = "__m2praca"
    BUFFER_MODE = "__trprbufora"
    CIRCUIT_MODE_HEATING_ZONE_1 = "__typ_obwo_co1"
    CIRCUIT_MODE_HEATING_ZONE_2 = "__typ_obwo_co2"
    CIRCUIT_MODE_HEATING_ZONE_3 = "__typ_obwo_co3"
    CIRCUIT_MODE_HEATING_ZONE_4 = "__typ_obwo_co4"
    CURRENT_TEMPERATURE = "__tpokojowa"
    DHW_CIRCULATION_MODE = "__dhwcircmode"
    DHW_MODE = "__dhwmode"
    DHW_OPERATING_MODE = "__trybprcwu"
    DHWC_CIRCULATION = "__cyrk_cwu"
    FAN_MODE = "__trybaero"
    HEATING_MODE_ZONE_1 = "__tr_pr_co1"
    HEATING_MODE_ZONE_2 = "__tr_pr_co2"
    HEATING_MODE_ZONE_3 = "__tr_pr_co3"
    HEATING_MODE_ZONE_4 = "__tr_pr_co4"
    HEATING_OPERATING_MODE_ZONE_1 = "__trprco1"
    HEATING_OPERATING_MODE_ZONE_2 = "__trprco2"
    HEATING_OPERATING_MODE_ZONE_3 = "__trprco3"
    HEATING_OPERATING_MODE_ZONE_4 = "__trprco4"
    HEATING_SOURCE_OF_CORRECTION = "__comode"
    HEATING_SOURCE_OF_CORRECTION_ZONE_1 = "__co1zrodlokorekty"
    HEATING_SOURCE_OF_CORRECTION_ZONE_2 = "_co2zrodlokorekty"
    HEATING_SOURCE_OF_CORRECTION_ZONE_3 = "__co3zrodlokorekty"
    HEATING_SOURCE_OF_CORRECTION_ZONE_4 = "__co4zrkorekty"
    HVAC_MODE = "__trybpracyinstalacji"
    LANGUAGE = "_jezyk"
    MIXER_MODE = "__pracamieszacza"
    MIXERMODE_ZONE_1 = "__mixer1mode"
    NANO_MODE = "__nano_mode"
    OPERATING_MODE = "__tr_pracy_pc"
    PRE_HEATER_ZONE_3 = "__a3konfignagwst"
    PRE_HEATER_ZONE_5 = "__a5trybnagrzwst"
    PRESET_MODE = "__trybpracytermostatu"
    R350_HEATING_SOURCE_OF_CORRECTION = "__tr_pr"
    R470_OPERATING_MODE = "__mode"
    R480_BUFFER_MODE = "__tr_buf"
    R480_DHW_CIRCULATION = "__cwu_cyrkulacja"
    R480_DHW_MODE = "__tryb_cwu"
    R480_OPERATING_MODE = "__praca_pc"
    R490_OPERATING_MODE = "__sezprinst"
    R770_DHW_CIRCULATION_MODE = "__trybpracycyrkcwu"
    R770_DHW_OPERATING_MODE = "__trybpracycwu"
    R770_MIXER_MODE_ZONE_1 = "__trybmieszacza"
    R770_MIXER_MODE_ZONE_2 = "__trybmie2"
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