from grpc import Channel, insecure_channel

from clients.grpc.gateway.accounts.client import AccountsGatewayGRPCClient
from clients.grpc.gateway.cards.client import CardsGatewayGRPCClient
from clients.grpc.gateway.documents.client import DocumentsGatewayGRPCClient
from clients.grpc.gateway.operations.client import OperationsGatewayGRPCClient
from clients.grpc.gateway.users.client import UsersGatewayGRPCClient


class GRPCClientBuilder:
    def __init__(self):
        self._channel: str | None = "localhost:9003"

    def base_url(self, url: str):
        self._channel = url
        return self

    def _build_client(self) -> Channel:
        return insecure_channel(target=self._channel)

    def build_users_gateway(self) -> UsersGatewayGRPCClient:
        return UsersGatewayGRPCClient(self._build_client())

    def build_cards_gateway(self) -> CardsGatewayGRPCClient:
        return CardsGatewayGRPCClient(self._build_client())

    def build_accounts_gateway(self) -> AccountsGatewayGRPCClient:
        return AccountsGatewayGRPCClient(self._build_client())

    def build_documents_gateway(self) -> DocumentsGatewayGRPCClient:
        return DocumentsGatewayGRPCClient(self._build_client())

    def build_operations_gateway(self) -> OperationsGatewayGRPCClient:
        return OperationsGatewayGRPCClient(self._build_client())
