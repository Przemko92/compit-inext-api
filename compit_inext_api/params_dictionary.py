from .consts import CompitParameter

PARAMS = {

    CompitParameter.ACTUAL_BUFFER_TEMP: {
        215: "__rr_t_buf",
        224: "__rr_temp_zmie_bufo",
    },

    CompitParameter.ACTUAL_HC1_TEMPERATURE: {
        224: "__rd_t_co1",
    },

    CompitParameter.ACTUAL_HC2_TEMPERATURE: {
        224: "__rd_t_co2",
    },

    CompitParameter.ACTUAL_HC3_TEMPERATURE: {
        224: "__rd_t_co3",
    },

    CompitParameter.ACTUAL_HC4_TEMPERATURE: {
        224: "__rd_t_co4",
    },

    CompitParameter.ACTUAL_DHW_TEMP: {
        215: "__rr_t_cwu",
        224: "__rr_temp_zmier_cwu",
    },

    CompitParameter.ACTUAL_UPPER_SOURCE_TEMP: {
        224: "__rr_temp_zmie_gz",
    },

    CompitParameter.AIRING: {
        223: "__rr_wietrzenie",
    },

    CompitParameter.ALARM_CODE: {
        226: "__kod_alarmu",
    },

    CompitParameter.BATTERY_CHARGE_STATUS: {
        226: "__rr_ladowanie",
    },

    CompitParameter.BATTERY_LEVEL: {
        226: "__rr_naladowanie",
    },

    CompitParameter.BOILER_TEMPERATURE: {
        36: "__t_boiler",
        75: "__t_boiler",
        91: "__ramkatkotla",
        201: "__t_boiler",
        210: "__tkotla",
        212: "__tkotla",
    },

    CompitParameter.BUFFER_RETURN_TEMPERATURE: {
        210: "__tpowrotu",
    },

    CompitParameter.BUFFER_SET_TEMPERATURE: {
        222: "__bufo_temp_zada",
    },

    CompitParameter.CALCULATED_BUFFER_TEMP: {
        224: "__rr_temp_wyli_bufo",
    },

    CompitParameter.CALCULATED_DHW_TEMP: {
        224: "__rr_temp_wyli_cwu",
    },

    CompitParameter.CALCULATED_HEATING_TEMPERATURE: {
        3: "__tcowyliczona",
        14: "__tcowyliczona",
    },

    CompitParameter.CALCULATED_TARGET_TEMPERATURE: {
        5: "__Tzadanawyliczona",
        53: "__tzadwyl",
    },

    CompitParameter.CALCULATED_UPPER_SOURCE_TEMP: {
        224: "__rr_temp_wyli_gorn_zrod",
    },

    CompitParameter.CHARGING_POWER: {
        226: "__rr_ibat",
    },

    CompitParameter.CIRCUIT_TARGET_TEMPERATURE: {
        5: "__tempzadanobiegu",
    },

    CompitParameter.CO2_ALERT: {
        78: "__flaga_co2",
    },

    CompitParameter.CO2_LEVEL: {
        12: "__rd_co2",
        27: "__rr_co2",
        78: "__rt_odczyt_co2",
        223: "__rd_co2",
        225: "__rr_co2",
    },

    CompitParameter.CO2_PERCENT: {
        78: "__rt_proc_co2",
    },

    CompitParameter.COLLECTOR_POWER: {
        44: "__mockolektora",
        45: "__mockol",
        99: "__mockol",
    },

    CompitParameter.COLLECTOR_TEMPERATURE: {
        44: "__tkolektora",
        45: "__tkol",
        99: "__tkol",
    },

    CompitParameter.CO_PUMP_OFF_DELAY: {
        17: "__opwylpco",
    },

    CompitParameter.CO_PUMP_ON_DELAY: {
        17: "__opzalpco",
    },

    CompitParameter.CURRENT_TEMPERATURE: {
        7: "__t_pokojowa",
        12: "__tpokojowa",
        223: "__tpokojowa",
    },

    CompitParameter.DHW_MEASURED_TEMPERATURE: {
        53: "__tcwumierz",
        215: "__rr_t_cwu",
    },

    CompitParameter.DHW_TEMPERATURE: {
        210: "__tcwu",
    },

    CompitParameter.DUST_ALERT: {
        78: "__flaga_pyly",
    },

    CompitParameter.ENERGY_CONSUMPTION: {
        58: "__eelmwh",
    },

    CompitParameter.ENERGY_SGREADY_YESTERDAY: {
        53: "__ensgreadywczoraj",
    },

    CompitParameter.ENERGY_TODAY: {
        45: "__edzisiaj",
        99: "__edzisiaj",
    },

    CompitParameter.ENERGY_TOTAL: {
        53: "__en_calkowita",
    },

    CompitParameter.ENERGY_YESTERDAY: {
        53: "__en_wczoraj",
    },

    CompitParameter.FAN_MODE: {
        12: "__trybaero",
        223: "__trybaero",
    },

    CompitParameter.FUEL_LEVEL: {
        36: "__fuel",
        75: "__fuel",
        91: "__poziompaliwa",
        201: "__fuel",
        212: "__poz_paliwa",
    },

    CompitParameter.HAS_BATTERY: {
        226: "__rr_jest_bat",
    },

    CompitParameter.HAS_EXTERNAL_POWER: {
        226: "__rr_jest230",
    },

    CompitParameter.HEATING1_TARGET_TEMPERATURE: {
        224: "__rd_t_zad_co1",
    },

    CompitParameter.HEATING2_TARGET_TEMPERATURE: {
        224: "__rd_t_zad_co2",
    },

    CompitParameter.HEATING3_TARGET_TEMPERATURE: {
        224: "__rd_t_zad_co3",
    },

    CompitParameter.HEATING4_TARGET_TEMPERATURE: {
        224: "__rd_t_zad_co4",
    },

    CompitParameter.HUMIDITY: {
        27: "__rr_wilgotnosc",
        78: "__hig",
        225: "__pom_hum",
    },

    CompitParameter.HVAC_MODE: {
        7: "__mode_intal",
        12: "__trybpracyinstalacji",
        223: "__trybpracyinstalacji",
    },

    CompitParameter.LOWER_SOURCE_TEMPERATURE: {
        92: "__tdz",
    },

    CompitParameter.MIXER1_TEMPERATURE: {
        91: "__ramkatempco1",
    },

    CompitParameter.MIXER2_TEMPERATURE: {
        91: "__ramkatempco2",
    },

    CompitParameter.MIXER_TEMPERATURE: {
        5: "__tmieszacza",
        221: "__rr_t_mie",
    },

    CompitParameter.OUTDOOR_TEMPERATURE: {
        3: "__tzewn",
        5: "__t_ext",
        12: "__rd_tempzewn",
        27: "__rr_temp",
        34: "__t_ext",
        36: "__t_ext",
        53: "__t_zewn",
        75: "__tempzewn",
        78: "__temp",
        91: "__tzewn",
        201: "__Tzew",
        212: "__t_zewn",
        221: "__rt_t_zew",
        223: "__rd_tempzewn",
        224: "__t_ext",
        225: "__pom_temp",
        226: "__rr_tzew",
    },

    CompitParameter.PK1_FUNCTION: {
        227: "__funkcja_pk1",
    },

    CompitParameter.PM1_LEVEL_MEASURED: {
        78: "__rr_pm1",
    },

    CompitParameter.PM4_LEVEL_MEASURED: {
        78: "__rr_pm4",
    },

    CompitParameter.PM10_LEVEL: {
        12: "__rd_pm10",        
        223: "__rd_pm10",
      
    },
    CompitParameter.PM10_MEASURED: {
        78: "__rr_pm10",
        225: "__rr_pm10",
    },
    CompitParameter.PM25_LEVEL: {
        12: "__rd_pm25",
        223: "__rd_pm25",
    },
    CompitParameter.PM25_MEASURED: {
        78: "__rr_pm2_5",
        225: "__rr_pm2_5",
    },
    CompitParameter.PRESET_MODE: {
        7: "__nano_mode",
        12: "__trybpracytermostatu",
        223: "__trybpracytermostatu",
    },

    CompitParameter.PROTECTION_TEMPERATURE: {
        221: "__rr_t_ochr",
    },

    CompitParameter.PUMP_STATUS: {
        226: "__rr_pompa",
    },

    CompitParameter.RETURN_CIRCUIT_TEMPERATURE: {
        3: "__temppowrotu",
        226: "__rr__tpow",

    },

    CompitParameter.SET_TARGET_TEMPERATURE: {
        7: "__tzadman",
        12: "__tempzadpracareczna",
        223: "__tempzadpracareczna",
    },

    CompitParameter.TANK_BOTTOM_T2_TEMPERATURE: {
        44: "__czujzasobt2",
        45: "__t2",
        99: "__t2",
    },

    CompitParameter.TANK_T4_TEMPERATURE: {
        44: "__czujnikt4",
    },

    CompitParameter.TANK_TOP_T3_TEMPERATURE: {
        44: "__czujzastopt3",
        45: "__t3",
        99: "__t3",
    },

    CompitParameter.TARGET_HEATING_TEMPERATURE: {
        3: "__tzadanaco",
        14: "__tzadanaco",
    },

    CompitParameter.TARGET_TEMPERATURE: {
        7: "__tzadman",
        12: "__tpokzadana",
        223: "__tpokzadana",
    },

    CompitParameter.TEMPERATURE_ALERT: {
        78: "__rr_fl_temp",
    },

    CompitParameter.UPPER_SOURCE_TEMPERATURE: {
        92: "__tempgz",
    },

    CompitParameter.VENTILATION_ALARM: {
        12: "__rd_alarmwent",
        223: "__rd_alarmwent",
    },

    CompitParameter.VENTILATION_GEAR: {
        223: "__rr_biegwen",
    },

    CompitParameter.WEATHER_CURVE: {
        221: "__ch_pog",
    },

}

PARAM_VALUES = {
    CompitParameter.AEROKONFBYPASS: {
        "off": 0,
        "auto": 1,
        "on": 2,
    },
    CompitParameter.LANGUAGE: {
        "polish": 0,
        "english": 1,
    },
    CompitParameter.NANO_MODE: {
        "manual_3": 0,
        "manual_2": 1,
        "manual_1": 2,
        "manual_0": 3,
        "schedule": 4,
        "christmas": 5,
        "out_of_home": 6,
    },
    CompitParameter.SOLAR_COMP_OPERATING_MODE: {
        "auto": 1,
        "de_icing": 2,
        "holiday": 3,
        "disabled": 4,
    },
    CompitParameter.BUFFER_MODE: {
        "disabled": 0,
        "schedule": 1,
        "manual": 2,
    },
    CompitParameter.OPERATING_MODE: {
        "disabled": 1,
        "auto": 2,
        "eco": 3,
    },
    CompitParameter.HEATING_SOURCE_OF_CORRECTION: {
        "no_corrections": 1,
        "schedule": 2,
        "thermostat": 3,
        "nano_nr_1": 4,
        "nano_nr_2": 5,
        "nano_nr_3": 6,
        "nano_nr_4": 7,
        "nano_nr_5": 8,
    },
    CompitParameter.DHW_CIRCULATION_MODE: {
        "disabled": 0,
        "constant": 1,
        "schedule": 2,
    },
    CompitParameter.BIOMAX_HEATING_SOURCE_OF_CORRECTION: {
        "disabled": 0,
        "no_corrections": 1,
        "schedule": 2,
        "thermostat": 3,
        "nano_nr_1": 4,
        "nano_nr_2": 5,
        "nano_nr_3": 6,
        "nano_nr_4": 7,
        "nano_nr_5": 8,
    },
    CompitParameter.BIOMAX_MIXER_MODE_ZONE_1: {
        "disabled": 0,
        "without_thermostat": 1,
        "no_corrections": 1,
        "schedule": 2,
        "thermostat": 3,
        "nano_nr_1": 4,
        "nano_nr_2": 5,
        "nano_nr_3": 6,
        "nano_nr_4": 7,
        "nano_nr_5": 8,
    },
    CompitParameter.BIOMAX_MIXER_MODE_ZONE_2: {
        "disabled": 0,
        "without_thermostat": 1,
        "no_corrections": 1,
        "schedule": 2,
        "thermostat": 3,
        "nano_nr_1": 4,
        "nano_nr_2": 5,
        "nano_nr_3": 6,
        "nano_nr_4": 7,
        "nano_nr_5": 8,
    },
    CompitParameter.CO2_LEVEL: {
        "no_sensor": 0,
        "normal": 1,
        "exceeded": 3,
    },
    CompitParameter.PM25_LEVEL:{
        "no_sensor": 0,
        "normal": 1,
        "warning": 2,
        "exceeded": 3,
    },
    CompitParameter.PM10_LEVEL:{
        "no_sensor": 0,
        "normal": 1,
        "warning": 2,
        "exceeded": 3,
    },
    CompitParameter.VENTILATION_ALARM: {
        "no_alarm": 0,
        "damaged_supply_sensor": 1,
        "damaged_exhaust_sensor": 2,
        "damaged_supply_and_exhaust_sensors": 3,
        "bot_alarm": 4,
        "damaged_preheater_sensor": 5,
        "ahu_alarm": 6,
    },
    CompitParameter.AIRING: {
        "off": 0,
        "on": 1,
    },
    CompitParameter.ALARM_CODE: {
        "no_alarm": 0,
        "damaged_outdoor_temp": 1,
        "damaged_return_temp": 2,
        "no_battery": 3,
        "discharged_battery": 4,
        "low_battery_level": 5,
        "battery_fault": 6,
        "no_pump": 7,
        "pump_fault": 8,
        "internal_af": 9,
        "no_power": 10,
    },
    CompitParameter.PUMP_STATUS: {
        "off": 0,
        "on": 1,
    },
    CompitParameter.BATTERY_CHARGE_STATUS: {
        "not_charging": 0,
        "charging": 1,
    },
    CompitParameter.HAS_EXTERNAL_POWER: {
        "no": 0,
        "yes": 1,
    },
    CompitParameter.HAS_BATTERY: {
        "no": 0,
        "yes": 1,
    },
    CompitParameter.DUST_ALERT: {
        "no_alert": 0,
        "alert": 1,
    },
    CompitParameter.TEMPERATURE_ALERT: {
        "no_alert": 0,
        "alert": 1,
    },
    CompitParameter.PK1_FUNCTION: {
        "off": 0,
        "on": 1,
        "nano_nr_1": 2,
        "nano_nr_2": 3,
        "nano_nr_3": 4,
        "nano_nr_4": 5,
        "nano_nr_5": 6,
        "winter": 7,
        "summer": 8,
        "cooling": 9,
        "holiday": 10,
    }
}
PARAMS_MAP = {
    CompitParameter.PRESET_MODE:{
         7: {
            0: 4,
            1: 5,
            2: 0,
            3: 6,
         },
    }
}