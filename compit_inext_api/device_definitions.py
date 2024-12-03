from importlib import resources
import json
import logging
import aiofiles

from .types.DeviceDefinitions import DeviceDefinitions

_LOGGER: logging.Logger = logging.getLogger(__package__)

class DeviceDefinitionsLoader:
    """Class to load the device definitions from file."""
    
    @staticmethod
    async def get_device_definitions(lang: str) -> DeviceDefinitions:
        """Get the device definitions from file."""
        file_name = f"devices_{lang}.json"
        config_path = resources.files('compit_inext_api.definitions').joinpath(file_name)
        try:        
            async with aiofiles.open(config_path, encoding="utf-8", mode='r') as file:
                content = await file.read()
                return DeviceDefinitions.from_json(json.loads(content))
        except FileNotFoundError:
            _LOGGER.warning("File %s not found", file_name)
            if lang != "en":
                _LOGGER.debug("Trying to load English definitions")
                return await DeviceDefinitionsLoader.get_device_definitions("en")
            raise ValueError("No definitions found") from None