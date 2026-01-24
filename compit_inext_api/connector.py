import aiohttp
import logging

from compit_inext_api.api import CompitAPI
from compit_inext_api.consts import CompitParameter
from compit_inext_api.device_definitions import DeviceDefinitionsLoader
from compit_inext_api.params_dictionary import PARAMS, PARAM_VALUES, PARAMS_MAP
from compit_inext_api.types.DeviceState import DeviceInstance, GateInstance, Param


_LOGGER: logging.Logger = logging.getLogger(__package__)


class CompitApiConnector:
    """Connector class for Compit API."""

    gates: dict[int, GateInstance] = {}

    @property
    def all_devices(self) -> dict[int, DeviceInstance]:
        devices: dict[int, DeviceInstance] = {}
        for gate in self.gates.values():
            devices.update(gate.devices)
        return devices

    def __init__(self, session: aiohttp.ClientSession) -> None:
        self.session = session

    def _resolve_parameter_code(self, device_code: int, parameter: CompitParameter) -> str:
        mapping = PARAMS.get(parameter)
        if not mapping:
            return parameter.value

        if device_code in mapping:
            return mapping[device_code]

        return parameter.value

    def get_device(self, device_id: int) -> DeviceInstance | None:
        for gate in self.gates.values():
            if device_id in gate.devices:
                return gate.devices[device_id]
        return None

    async def init(self, email: str, password: str, lang: str | None = None) -> bool:
        self.api = CompitAPI(email, password, self.session)
        self.systemInfo = await self.api.authenticate()
        if self.systemInfo is None:
            _LOGGER.error("Failed to authenticate with Compit API")
            return False
        
        for gates in self.systemInfo.gates:
            self.gates[gates.id] = GateInstance(gates.id, gates.label)
            for device in gates.devices:
                try:
                    self.gates[gates.id].devices[device.id] = DeviceInstance(
                        device.label,
                        await DeviceDefinitionsLoader.get_device_definition(
                            device.type,
                            lang=lang,
                        ),
                    )
                    state = await self.api.get_state(device.id)
                    if state:
                        self.gates[gates.id].devices[device.id].state = state
                    else:
                        _LOGGER.error("Failed to get state for device %s", device.id)
                except ValueError:
                    _LOGGER.warning("No definition found for device with code %d", device.type)
        return True

    async def update_state(self, device_id: int | None) -> None:
        if device_id is None:
            for gate in self.gates.values():
                for device in gate.devices.keys():
                    await self.update_state(device)
            return

        device = self.get_device(device_id)
        if device is None:
            _LOGGER.warning("No device found with ID %d", device_id)
            return

        state = await self.api.get_state(device_id)
        if state:
            device.state = state
        else:
            _LOGGER.error("Failed to get state for device %s", device_id)

    def get_current_option(self, device_id: int, parameter: CompitParameter) -> str | None:
        device = self.get_device(device_id)
        if not device:
            return None

        code = self._resolve_parameter_code(device.definition.code, parameter)
        val = device.state.get_parameter_value(code)

        if val is None:
            return None
        
        param = PARAM_VALUES.get(parameter, None)
        if param is None:
            return None

        for key, value in param.items():
            if value == val.value:
                return key
            
        return None              

    def get_current_value(self, device_id: int, parameter: CompitParameter) -> str | float | None:
        device = self.get_device(device_id)
        if not device:
            return None
        code = self._resolve_parameter_code(device.definition.code, parameter)
        param = device.state.get_parameter_value(code)
        if param is None:
            return None
        
        if param.value_label is None:
            return param.value
        
        parameter_values = PARAM_VALUES.get(parameter, None)

        if parameter_values is None:
            return param.value

        for key, value in parameter_values.items():
            if value == param.value:
                return key

        return param.value

    def get_device_parameter(self, device_id: int, parameter: CompitParameter) -> Param | None:
        device = self.get_device(device_id)
        if not device:
            return None
        code = self._resolve_parameter_code(device.definition.code, parameter)
        param = device.state.get_parameter_value(code)

        mapped_values = PARAMS_MAP.get(parameter, None)
        if mapped_values:
            map = mapped_values.get(device.definition.code, None)
            if map is not None and param is not None:
                reverse_map = {v: k for k, v in map.items()}
                if param.value in reverse_map:
                    param.value = reverse_map[param.value]

        if param is None:
            return None

        return param

    async def select_device_option(self, device_id: int, parameter: CompitParameter, value: str) -> bool:
        device = self.get_device(device_id)
        if device is None:
                return False
                
        code = self._resolve_parameter_code(device.definition.code, parameter)
        
        val = PARAM_VALUES.get(parameter, None)
        if val is None:
                return False
        
        mapped_value = val.get(value, None)
        if mapped_value is None:
                return False
        
        result = await self.api.update_device_parameter(device_id, code, mapped_value)
        if result is None:
                return False
        device.state.set_parameter_value(code, mapped_value)
        return result

    async def set_device_parameter(self, device_id: int, parameter: CompitParameter, value: str | float) -> bool:
        device = self.get_device(device_id)
        if device is None:
                return False
        
        code = self._resolve_parameter_code(device.definition.code, parameter)

        mapped_values = PARAMS_MAP.get(parameter, None)

        if mapped_values:
            map = mapped_values.get(device.definition.code, None)
            if map is not None:
                value = map[int(value)]

        result = await self.api.update_device_parameter(device_id, code, value)
        if result:
            device.state.set_parameter_value(code, value)

        return result