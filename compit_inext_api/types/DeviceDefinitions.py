"""Module containing device definitions for compit which are deserialized from json."""  # noqa: INP001

from typing import Any


class ParameterDetails:
    """Class representing the details of a parameter."""

    def __init__(self, State: int, Description: str, Param: str) -> None:
        """Initialize the ParameterDetails class.

        Args:
            State (int): The state of the parameter.
            Description (str): The description of the parameter.
            Param (str): The parameter value.

        """
        self.state = State
        self.description = Description
        self.param = Param


class Parameter:
    """Class representing a parameter."""

    def __init__(
        self,
        ParameterCode: str,
        Label: str,
        ReadWrite: str = "R",
        Details: list[dict[str, Any]] | None = None,
        MinValue: float | None = None,
        MaxValue: float | None = None,
        Unit: str | None = None,
    ) -> None:
        """Initialize the DeviceDefinitions class."""

        self.parameter_code = ParameterCode
        self.label = Label
        self.readWrite = ReadWrite
        self.details = (
            [ParameterDetails(**detail) if Details else None for detail in Details]
            if Details
            else None
        )
        self.min_value = MinValue
        self.max_value = MaxValue
        self.unit = Unit


class Device:
    """Class representing a device."""

    def __init__(
        self,
        name: str,
        parameters: list[Parameter],
        code: int,
        device_class: int,
        id: int | None,
    ) -> None:
        """Initialize the Device class.

        Args:
            name (str): The name of the device.
            parameters (list[Parameter]): The list of parameters for the device.
            code (int): The code of the device.
            device_class (int): The class of the device.
            id (int | None): The ID of the device.

        """
        self.name = name
        self.parameters = parameters
        self.code = code
        self.device_class = device_class
        self.id = id

    @classmethod
    def from_json(cls, data: dict[str, Any]):
        """Create a DeviceDefinitions instance from JSON data.

        Args:
            data (dict[str, Any]): The JSON data representing the device definitions.

        Returns:
            DeviceDefinitions: The created DeviceDefinitions instance.

        """
        parameters = [Parameter(**param) for param in data.get("Parameters", [])]
        return cls(
            name=data["Name"],
            parameters=parameters,
            code=data["Code"],
            device_class=data["Class"],
            id=data.get("ID"),
        )


class DeviceDefinitions:
    """Class representing device definitions."""

    def __init__(self, devices: list[Device]) -> None:
        """Initialize the DeviceDefinitions class.

        Args:
            devices (list[Device]): The list of devices.

        """
        self.devices = devices

    @classmethod
    def from_json(cls, data: Any):
        """Create a DeviceDefinitions instance from JSON data.

        Args:
            data (Any): The JSON data representing the device definitions.

        Returns:
            DeviceDefinitions: The created DeviceDefinitions instance.

        """
        devices = [Device.from_json(device_data) for device_data in data]
        return cls(devices=devices)
