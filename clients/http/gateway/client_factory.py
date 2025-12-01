import logging
from typing import Callable, Type

from httpx import Client
from locust.env import Environment

from clients.http.base_client import HTTPClient
from clients.http.event_hooks.locust_event_hook import locust_request_event_hook, locust_response_event_hook


class HTTPClientFactory:
    def __init__(self, factory_function: Callable[[], Client]):
        self._client = factory_function()

    def create(self, gateway_cls: Type[HTTPClient]):
        return gateway_cls(self._client)


def build_gateway_http_client() -> Client:
    return Client(timeout=100, base_url="http://localhost:8003")


def build_gateway_locust_http_client(environment: Environment) -> Client:
    logging.getLogger("httpx").setLevel(logging.WARNING)

    return Client(
        timeout=100,
        base_url="http://localhost:8003",
        event_hooks={
            "request": [locust_request_event_hook],
            "response": [locust_response_event_hook(environment)]
        }
    )
