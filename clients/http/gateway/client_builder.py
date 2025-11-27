from httpx import Client

from .accounts.client import AccountsGatewayHTTPClient
from .cards.client import CardsGatewayHTTPClient
from .documents.client import DocumentsGatewayHTTPClient
from .operations.client import OperationsGatewayHTTPClient
from .users.client import UsersGatewayHTTPClient


class HTTPClientBuilder:
    def __init__(self):
        self._base_url: str | None = "http://localhost:8003/"
        self._timeout: float | None = None
        self._headers: dict[str, str] | None = None

    def base_url(self, url: str):
        self._base_url = url
        return self

    def timeout(self, seconds: float):
        self._timeout = seconds
        return self

    def headers(self, headers: dict[str, str]):
        self._headers = headers
        return self

    def build_client(self) -> Client:
        return Client(
            base_url=self._base_url,
            timeout=self._timeout,
            headers=self._headers,
        )

    def build_users_gateway(self) -> UsersGatewayHTTPClient:
        return UsersGatewayHTTPClient(self.build_client())

    def build_cards_gateway(self) -> CardsGatewayHTTPClient:
        return CardsGatewayHTTPClient(self.build_client())

    def build_accounts_gateway(self) -> AccountsGatewayHTTPClient:
        return AccountsGatewayHTTPClient(self.build_client())

    def build_documents_gateway(self) -> DocumentsGatewayHTTPClient:
        return DocumentsGatewayHTTPClient(self.build_client())

    def build_operations_gateway(self) -> OperationsGatewayHTTPClient:
        return OperationsGatewayHTTPClient(self.build_client())
