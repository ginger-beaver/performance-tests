from typing import Callable, Type

from grpc import Channel, insecure_channel, intercept_channel
from locust.env import Environment

from clients.grpc.base_client import GRPCClient
from clients.grpc.interceptors.locust_interceptor import LocustInterceptor


class GRPCClientFactory:
    def __init__(self, factory_function: Callable[[], Channel]):
        self._channel = factory_function()

    def create(self, gateway_cls: Type[GRPCClient]):
        return gateway_cls(self._channel)


def build_gateway_grpc_client() -> Channel:
    return insecure_channel("localhost:9003")


def build_gateway_locust_grpc_client(environment: Environment) -> Channel:
    locust_interceptor = LocustInterceptor(environment=environment)

    channel = insecure_channel("localhost:9003")

    return intercept_channel(channel, locust_interceptor)
