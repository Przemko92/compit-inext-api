import aiohttp
import logging

from compit_inext_api.api import CompitAPI
from compit_inext_api.consts import CompitParameter
from compit_inext_api.device_definitions import DeviceDefinitionsLoader
from compit_inext_api.types.DeviceState import DeviceInstance, DeviceState, Param


_LOGGER: logging.Logger = logging.getLogger(__package__)


class CompitApiConnector:
    """Connector class for Compit API."""

    devices: dict[int, DeviceInstance] = {}

    def __init__(self, session: aiohttp.ClientSession) -> None:
        self.session = session

    async def init(self, email: str, password: str, lang: str = "en") -> bool:
        self.api = CompitAPI(email, password, self.session)
        self.systemInfo = await self.api.authenticate()
        if self.systemInfo is None:
            _LOGGER.error("Failed to authenticate with Compit API")
            return False
        
        for gates in self.systemInfo.gates:
            for device in gates.devices:
                try:
                    self.devices[device.id] = DeviceInstance(await DeviceDefinitionsLoader.get_device_definition(device.type, lang)) 
                    state = await self.api.get_state(device.id)
                    if state and isinstance(state, DeviceState):
                        self.devices[device.id].state = state
                    else:
                        _LOGGER.error("Failed to get state for device %s", device.id)
                except ValueError:
                    _LOGGER.warning("No definition found for device with code %d", device.type)
        return True

    async def update_state(self, device_id: int | None) -> None:
        if device_id is None:
            for device in self.devices.keys():
                await self.update_state(device)
            return

        device = self.devices.get(device_id)
        if device is None:
            _LOGGER.warning("No device found with ID %d", device_id)
            return

        state = await self.api.get_state(device_id)
        if state and isinstance(state, DeviceState):
            device.state = state
        else:
            _LOGGER.error("Failed to get state for device %s", device_id)

    def get_device_parameter(self, device_id: int, parameter: CompitParameter) -> Param | None:
         return self.devices[device_id].state.get_parameter_value(parameter.value)
    
    async def set_device_parameter(self, device_id: int, parameter: CompitParameter, value: str | float) -> bool:
        result = await self.api.update_device_parameter(device_id, parameter, value)
        if result:
            self.devices[device_id].state.set_parameter_value(parameter.value, value)
            return True
        return False