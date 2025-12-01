from typing import Callable, Type

from grpc import Channel, insecure_channel

from clients.grpc.base_client import GRPCClient


class GRPCClientFactory:
    def __init__(self, factory_function: Callable[[], Channel]):
        self._channel = factory_function()

    def create(self, gateway_cls: Type[GRPCClient]):
        return gateway_cls(self._channel)


def build_gateway_grpc_client() -> Channel:
    return insecure_channel("localhost:9003")
