"""Module containing params definitions."""  # noqa: INP001

from typing import Any

from .DeviceDefinitions import Device, Parameter


class Param:
    """Class representing a parameter."""

    def __init__(
        self,
        code: str,
        hidden: bool,
        max: float | None,
        min: float | None,
        value: Any,
        value_code: str | None,
        value_label: str | None,
        write: bool,
        ext_info: dict | None = None,
    ) -> None:
        """Initialize the Param object."""
        self.code = code
        self.hidden = hidden
        self.max = max
        self.min = min
        self.value = value
        self.value_code = value_code
        self.value_label = value_label
        self.write = write
        self.ext_info = ext_info


class DeviceState:
    """Class representing the state of a device."""

    def __init__(
        self, errors: list[Any], last_connected_at: str, params: list[Param]
    ) -> None:
        """Initialize the DeviceState object."""
        self.errors = errors
        self.last_connected_at = last_connected_at
        self.params = params

    def get_parameter_value(self, param: str | Parameter) -> Param | None:
        """Get the value of a parameter by its code or parameter object.

        Args:
            param (str | Parameter): The code or parameter object.

        Returns:
            Param: The parameter object.

        """

        if isinstance(param, str):
            return next(
                (item for item in self.params if item and item.code == param), None
            )
        return next(
            (
                item
                for item in self.params
                if item and item.code == param.parameter_code
            ),
            None,
        )

    @classmethod
    def from_json(cls, data: dict):
        """Create a DeviceState object from JSON data."""
        params = [
            Param(
                code=p["code"],
                hidden=p["hidden"],
                max=p.get("max"),
                min=p.get("min"),
                value=p["value"],
                value_code=p.get("value_code"),
                value_label=p.get("value_label"),
                write=p["write"],
                ext_info=p.get("ext_info"),
            )
            for p in data["params"]
        ]
        return cls(
            errors=data["errors"],
            last_connected_at=data["last_connected_at"],
            params=params,
        )


class DeviceInstance:
    """Class representing a device instance."""

    def __init__(self, definition: Device) -> None:
        """Initialize the DeviceInstance object."""
        self.definition = definition
        self.state: DeviceState
