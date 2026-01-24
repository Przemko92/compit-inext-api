"""Module HTTP communication with the Inext Compit api."""

from .device_definitions import DeviceDefinitionsLoader
from .api import CompitAPI, CannotConnect, InvalidAuth
from .types.DeviceState import DeviceState, Param, DeviceInstance
from .types.DeviceDefinitions import DeviceDefinitions, Parameter, ParameterDetails
from .types.SystemInfo import SystemInfo, Gate, Device
from .consts import CompitHVACMode, CompitParameter, CompitFanMode, CompitPresetMode, CompitDevice
from .connector import CompitApiConnector
from .params_dictionary import PARAMS, PARAM_VALUES

__all__ = [
    "DeviceDefinitionsLoader", 
    "CompitAPI", 
    "DeviceState", 
    "Param", 
    "DeviceInstance", 
    "DeviceDefinitions", 
    "Parameter", 
    "ParameterDetails", 
    "SystemInfo", 
    "Gate", 
    "Device",
    "InvalidAuth",
    "CannotConnect",
    "CompitDevice",
    "CompitHVACMode",
    "CompitParameter", 
    "CompitFanMode",
    "CompitPresetMode",
    "CompitApiConnector",
    "PARAMS",
    "PARAM_VALUES",
]
