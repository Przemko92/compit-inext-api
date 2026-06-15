from __future__ import annotations

from collections.abc import Awaitable
from typing import Any, Callable

from compit_inext_api.consts import CompitParameter

type GetValueHandler = Callable[[Any, int, Any, CompitParameter, str], Any]
type SetValueHandler = Callable[[Any, int, CompitParameter, str | float], Awaitable[Any]]

CUSTOM_READ_BEHAVIORS: dict[CompitParameter, GetValueHandler] = {}
CUSTOM_WRITE_BEHAVIORS: dict[CompitParameter, SetValueHandler] = {}


def register_read_behavior(parameter: CompitParameter) -> Callable[[GetValueHandler], GetValueHandler]:
    def decorator(func: GetValueHandler) -> GetValueHandler:
        CUSTOM_READ_BEHAVIORS[parameter] = func
        return func
    return decorator


def register_write_behavior(parameter: CompitParameter) -> Callable[[SetValueHandler], SetValueHandler]:
    def decorator(func: SetValueHandler) -> SetValueHandler:
        CUSTOM_WRITE_BEHAVIORS[parameter] = func
        return func
    return decorator


@register_read_behavior(CompitParameter.PRESET_MODE)
def _preset_mode_read(
    connector: Any,
    device_id: int,
    device: Any,
    parameter: CompitParameter,
    code: str,
) -> Any:
    if device.definition.code not in (12, 223):
        return None

    out_of_home_code = connector._resolve_parameter_code(
        device.definition.code, CompitParameter.OUT_OF_HOME_MODE
    )
    out_of_home_param = device.state.get_parameter_value(out_of_home_code)
    if out_of_home_param is not None and out_of_home_param.value == 1:
        return 3
    return None


@register_write_behavior(CompitParameter.PRESET_MODE)
async def _preset_mode_write(
    connector: Any,
    device_id: int,
    parameter: CompitParameter,
    value: str | float,
) -> Any:
    device = connector.get_device(device_id)
    if device is None:
        return None

    if device.definition.code not in (12, 223):
        return None

    out_of_home_code = connector._resolve_parameter_code(
        device.definition.code, CompitParameter.OUT_OF_HOME_MODE
    )
    thermostat_code = connector._resolve_parameter_code(
        device.definition.code, CompitParameter.PRESET_MODE
    )

    if int(value) == 3:
        result = await connector.api.update_device_parameter(
            device_id, out_of_home_code, 1
        )
        if result:
            device.state.set_parameter_value(out_of_home_code, 1)
        return result

    result1 = await connector.api.update_device_parameter(
        device_id, out_of_home_code, 0
    )
    if result1:
        device.state.set_parameter_value(out_of_home_code, 0)
    result2 = await connector.api.update_device_parameter(
        device_id, thermostat_code, value
    )
    if result2:
        device.state.set_parameter_value(thermostat_code, value)
    return result2
