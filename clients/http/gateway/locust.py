import logging

from locust import events, TaskSet, SequentialTaskSet

from clients.http.gateway import UsersGatewayHTTPClient, CardsGatewayHTTPClient, AccountsGatewayHTTPClient, \
    DocumentsGatewayHTTPClient, OperationsGatewayHTTPClient
from clients.http.gateway.client_factory import HTTPClientFactory, build_gateway_locust_http_client

logger = logging.getLogger("locust")


@events.init.add_listener
def on_locust_init(environment, **kwargs):
    logger.info("Locust init hook executed")

    environment.factory = HTTPClientFactory(
        lambda: build_gateway_locust_http_client(environment)
    )


class GatewayHTTPTaskSet(TaskSet):
    users_gateway_client: UsersGatewayHTTPClient
    cards_gateway_client: CardsGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient
    documents_gateway_client: DocumentsGatewayHTTPClient
    operations_gateway_client: OperationsGatewayHTTPClient

    def on_start(self) -> None:
        factory = self.user.environment.factory

        self.users_gateway_client = factory.create(UsersGatewayHTTPClient)
        self.cards_gateway_client = factory.create(CardsGatewayHTTPClient)
        self.accounts_gateway_client = factory.create(AccountsGatewayHTTPClient)
        self.documents_gateway_client = factory.create(DocumentsGatewayHTTPClient)
        self.operations_gateway_client = factory.create(OperationsGatewayHTTPClient)


class GatewayHTTPSequentialTaskSet(SequentialTaskSet):
    users_gateway_client: UsersGatewayHTTPClient
    cards_gateway_client: CardsGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient
    documents_gateway_client: DocumentsGatewayHTTPClient
    operations_gateway_client: OperationsGatewayHTTPClient

    def on_start(self) -> None:
        factory = self.user.environment.factory

        self.users_gateway_client = factory.create(UsersGatewayHTTPClient)
        self.cards_gateway_client = factory.create(CardsGatewayHTTPClient)
        self.accounts_gateway_client = factory.create(AccountsGatewayHTTPClient)
        self.documents_gateway_client = factory.create(DocumentsGatewayHTTPClient)
        self.operations_gateway_client = factory.create(OperationsGatewayHTTPClient)
