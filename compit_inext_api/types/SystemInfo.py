"""Module contains classes for system information."""  # noqa: INP001

class Device:
    """Class representing a device in the system."""

    def __init__(self, device_class: int, id: int, label: str, type: int) -> None:
        """Initialize a Device instance."""
        self.device_class = device_class
        self.id = id
        self.label = label
        self.type = type


class Gate:
    """Class representing a gate in the system."""

    def __init__(self, code: str, devices: list[Device], id: int, label: str) -> None:
        """Initialize a instance of Gate."""
        self.code = code
        self.devices = devices
        self.id = id
        self.label = label


class SystemInfo:
    """Class representing system information."""

    def __init__(self, gates: list[Gate]) -> None:
        """Initialize a SystemInfo instance."""
        self.gates = gates

    @classmethod
    def from_json(cls, data: dict):
        """Create a SystemInfo instance from JSON data."""
        gates = [
            Gate(
                code=g["code"],
                devices=[
                    Device(
                        device_class=d["class"],
                        id=d["id"],
                        label=d["label"],
                        type=d["type"],
                    )
                    for d in g["devices"]
                ],
                id=g["id"],
                label=g["label"],
            )
            for g in data["gates"]
        ]
        return cls(gates=gates)
