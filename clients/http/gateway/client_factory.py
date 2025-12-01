from typing import Callable, Type

from httpx import Client

from clients.http.base_client import HTTPClient


class HTTPClientFactory:
    def __init__(self, factory_function: Callable[[], Client]):
        self._client = factory_function()

    def create(self, gateway_cls: Type[HTTPClient]):
        return gateway_cls(self._client)


def build_gateway_http_client() -> Client:
    return Client(timeout=100, base_url="http://localhost:8003")
