from importlib import resources
import json
import logging
import aiofiles

from .types.DeviceDefinitions import DeviceDefinitions, Device

_LOGGER: logging.Logger = logging.getLogger(__package__)

class DeviceDefinitionsLoader:
    """Class to load the device definitions from file."""
    
    cache: dict[str, DeviceDefinitions] = {}

    @staticmethod
    async def get_device_definitions(lang: str) -> DeviceDefinitions:
        """Get the device definitions from file."""
        file_name = f"devices_{lang}.json"

        if lang in DeviceDefinitionsLoader.cache:
            return DeviceDefinitionsLoader.cache[lang]

        config_path = resources.files('compit_inext_api.definitions').joinpath(file_name)
        try:        
            async with aiofiles.open(config_path, encoding="utf-8", mode='r') as file:
                content = await file.read()
                definitions = DeviceDefinitions.from_json(json.loads(content))
                DeviceDefinitionsLoader.cache[lang] = definitions
                return definitions
        except FileNotFoundError:
            _LOGGER.warning("File %s not found", file_name)
            if lang != "en":
                _LOGGER.debug("Trying to load English definitions")
                return await DeviceDefinitionsLoader.get_device_definitions("en")
            raise ValueError("No definitions found") from None
        
    @staticmethod
    async def get_device_definition(code: int, lang: str = "en") -> Device:
        """Get the device definition for a specific device type."""
        definitions = await DeviceDefinitionsLoader.get_device_definitions(lang)
        for device in definitions.devices:
            if device.code == code:
                return device            
        raise ValueError(f"No definition found for device with code {code}")