"""The Compit api connector."""

import asyncio
import logging
from typing import Any

import aiohttp

from compit_inext_api.consts import CompitParameter

from .types.DeviceState import DeviceState
from .types.SystemInfo import SystemInfo

TIMEOUT = 10
_LOGGER: logging.Logger = logging.getLogger(__package__)
HEADERS = {"Content-type": "application/json; charset=UTF-8"}
API_URL = "https://inext.compit.pl/mobile/v2/compit"

class CompitAPI:
    """API client for Compit."""

    def __init__(self, email, password, session: aiohttp.ClientSession) -> None:
        """Initialize the CompitAPI class."""
        self.email = email
        self.password = password
        self.token = None
        self._api_wrapper = ApiWrapper(session)

    async def authenticate(self) -> SystemInfo | None:
        """Authenticate the user."""
        try:
            response = await self._api_wrapper.post(
                f"{API_URL}/authorize",
                {
                    "email": self.email,
                    "password": self.password,
                    "uid": "HomeAssistant",
                    "label": "HomeAssistant",
                },
            )

            if response.status == 401:
                raise InvalidAuth()

            if response.status == 422:
                result = await self.get_result(response, ignore_response_code=True)
                self.token = result["token"]
                response = await self._api_wrapper.post(
                    f"{API_URL}/clients",
                    {
                        "fcm_token": None,
                        "uid": "HomeAssistant",
                        "label": "HomeAssistant",
                    },
                    auth=self.token,
                )

                result = await self.get_result(response)
                return await self.authenticate()
            elif response.status > 400:
                return None

            result = await self.get_result(response)
            self.token = result["token"]
            return SystemInfo.from_json(result)
        except aiohttp.ClientError as e:
            _LOGGER.error(e)
            raise CannotConnect()

    async def get_gates(self) -> SystemInfo | None:
        """Get the gates from the Compit API."""
        try:
            response = await self._api_wrapper.get(f"{API_URL}/gates", {}, self.token)

            return SystemInfo.from_json(await self.get_result(response))
        except aiohttp.ClientError as e:
            _LOGGER.error(e)
            return None

    async def get_state(self, device_id: int) -> DeviceState | None:
        """Get the state of a device."""
        try:
            response = await self._api_wrapper.get(
                f"{API_URL}/devices/{device_id}/state", {}, self.token
            )

            return DeviceState.from_json(await self.get_result(response))

        except aiohttp.ClientError as e:
            _LOGGER.error(e)
            return None

    async def update_device_parameter(
        self, device_id: int, parameter: CompitParameter, value: str | float
    ) -> Any:
        """Update the parameter of a device.

        Args:
            device_id (int): The ID of the device.
            parameter (CompitParameter): The parameter to update.
            value (str | float): The new value of the parameter.

        Returns:
            Any: The result of the update operation.

        """
        try:
            _LOGGER.info("Set %s to %s for device %s", parameter, value, device_id)

            data = {"values": [{"code": parameter, "value": value}]}

            response = await self._api_wrapper.put(
                f"{API_URL}/devices/{device_id}/params", data=data, auth=self.token
            )
            return await self.get_result(response)

        except aiohttp.ClientError as e:
            _LOGGER.error(e)
            return None

    async def get_result(
        self,
        response: aiohttp.ClientResponse | None,
        ignore_response_code: bool = False,
    ) -> Any:
        """Get the result from the response.

        Args:
            response (aiohttp.ClientResponse): The response object.
            ignore_response_code (bool, optional): Whether to ignore the response code. Defaults to False.

        Returns:
            Any: The result from the response.

        Raises:
            Exception: If the server returns an error response.

        """
        if response is None:
            raise ValueError("Server empty response")
        if response.ok or ignore_response_code:
            return await response.json()

        raise ValueError(f"Server returned: {response.status}, {response.reason}")


class ApiWrapper:
    """Helper wrapper class."""

    def __init__(self, session: aiohttp.ClientSession) -> None:
        """Initialize the Helper class.

        Args:
            session (aiohttp.ClientSession): The aiohttp client session.

        """
        self._session = session

    async def get(
        self, url: str, headers: dict | None = None, auth: Any = None
    ) -> aiohttp.ClientResponse:
        """Run http GET method."""
        if headers is None:
            headers = {}

        if auth:
            headers["Authorization"] = auth

        return await self.api_wrapper("get", url, headers=headers, auth=None)

    async def post(
        self,
        url: str,
        data: dict | None = None,
        headers: dict | None = None,
        auth: Any = None,
    ) -> aiohttp.ClientResponse:
        """Run http POST method."""
        if headers is None:
            headers = {}

        if auth:
            headers["Authorization"] = auth

        return await self.api_wrapper(
            "post", url, data=data, headers=headers, auth=None
        )

    async def put(
        self,
        url: str,
        data: dict | None = None,
        headers: dict | None = None,
        auth: Any = None,
    ) -> aiohttp.ClientResponse:
        """Run http PUT method."""
        if headers is None:
            headers = {}

        if auth:
            headers["Authorization"] = auth

        return await self.api_wrapper("put", url, data=data, headers=headers, auth=None)

    async def api_wrapper(
        self,
        method: str,
        url: str,
        data: dict | None = None,
        headers: dict | None = None,
        auth: Any = None,
    ) -> Any:
        """Get information from the API."""
        try:
            async with asyncio.timeout(TIMEOUT):
                if method == "get":
                    return await self._session.get(url, headers=headers, auth=auth)

                if method == "post":
                    return await self._session.post(
                        url, headers=headers, data=data, auth=auth
                    )
                if method == "put":
                    return await self._session.put(
                        url, headers=headers, json=data, auth=auth
                    )

        except TimeoutError as exception:
            _LOGGER.error(
                "Timeout error fetching information from %s - %s",
                url,
                exception,
            )

class CannotConnect(Exception):
    """Error to indicate we cannot connect."""


class InvalidAuth(Exception):
    """Error to indicate there is invalid auth."""