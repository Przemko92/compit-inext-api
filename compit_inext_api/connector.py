import aiohttp
import logging

from compit_inext_api.api import CompitAPI
from compit_inext_api.consts import CompitParameter
from compit_inext_api.device_definitions import DeviceDefinitionsLoader
from compit_inext_api.types.DeviceState import DeviceInstance, DeviceState, GateInstance, Param


_LOGGER: logging.Logger = logging.getLogger(__package__)


class CompitApiConnector:
    """Connector class for Compit API."""

    gates: dict[int, GateInstance] = {}

    @property
    def all_devices(self) -> dict[int, DeviceInstance]:
        devices = {}
        for gate in self.gates.values():
            devices.update(gate.devices)
        return devices

    def __init__(self, session: aiohttp.ClientSession) -> None:
        self.session = session

    def get_device(self, device_id: int) -> DeviceInstance | None:
        for gate in self.gates.values():
            if device_id in gate.devices:
                return gate.devices[device_id]
        return None

    async def init(self, email: str, password: str, lang: str = "en") -> bool:
        self.api = CompitAPI(email, password, self.session)
        self.systemInfo = await self.api.authenticate()
        if self.systemInfo is None:
            _LOGGER.error("Failed to authenticate with Compit API")
            return False
        
        for gates in self.systemInfo.gates:
            self.gates[gates.id] = GateInstance(gates.id, gates.label)
            for device in gates.devices:
                try:
                    self.gates[gates.id].devices[device.id] = DeviceInstance(device.label, await DeviceDefinitionsLoader.get_device_definition(device.type, lang))
                    state = await self.api.get_state(device.id)
                    if state and isinstance(state, DeviceState):
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
        if state and isinstance(state, DeviceState):
            device.state = state
        else:
            _LOGGER.error("Failed to get state for device %s", device_id)

    def get_device_parameter(self, device_id: int, parameter: str | CompitParameter) -> Param | None:
        device = self.get_device(device_id)
        if device:
            return device.state.get_parameter_value(parameter if isinstance(parameter, str) else parameter.value)
        return None

    async def set_device_parameter(self, device_id: int, parameter: str | CompitParameter, value: str | float) -> bool:
        result = await self.api.update_device_parameter(device_id, parameter, value)
        if result:
            device = self.get_device(device_id)
            if device:
                device.state.set_parameter_value(parameter if isinstance(parameter, str) else parameter.value, value)
        return result

        