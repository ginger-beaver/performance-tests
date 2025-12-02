import logging

from locust import events, TaskSet, SequentialTaskSet

from clients.grpc.gateway import UsersGatewayGRPCClient, CardsGatewayGRPCClient, AccountsGatewayGRPCClient, \
    DocumentsGatewayGRPCClient, OperationsGatewayGRPCClient
from clients.grpc.gateway.client_factory import GRPCClientFactory, build_gateway_locust_grpc_client

logger = logging.getLogger("locust")


@events.init.add_listener
def on_locust_init(environment, **kwargs):
    logger.info("Locust init hook executed")

    environment.factory = GRPCClientFactory(
        lambda: build_gateway_locust_grpc_client(environment)
    )


class GatewayGRPCTaskSet(TaskSet):
    users_gateway_client: UsersGatewayGRPCClient
    cards_gateway_client: CardsGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient
    documents_gateway_client: DocumentsGatewayGRPCClient
    operations_gateway_client: OperationsGatewayGRPCClient

    def on_start(self) -> None:
        factory = self.user.environment.factory

        self.users_gateway_client = factory.create(UsersGatewayGRPCClient)
        self.cards_gateway_client = factory.create(CardsGatewayGRPCClient)
        self.accounts_gateway_client = factory.create(AccountsGatewayGRPCClient)
        self.documents_gateway_client = factory.create(DocumentsGatewayGRPCClient)
        self.operations_gateway_client = factory.create(OperationsGatewayGRPCClient)


class GatewayGRPCSequentialTaskSet(SequentialTaskSet):
    users_gateway_client: UsersGatewayGRPCClient
    cards_gateway_client: CardsGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient
    documents_gateway_client: DocumentsGatewayGRPCClient
    operations_gateway_client: OperationsGatewayGRPCClient

    def on_start(self) -> None:
        factory = self.user.environment.factory

        self.users_gateway_client = factory.create(UsersGatewayGRPCClient)
        self.cards_gateway_client = factory.create(CardsGatewayGRPCClient)
        self.accounts_gateway_client = factory.create(AccountsGatewayGRPCClient)
        self.documents_gateway_client = factory.create(DocumentsGatewayGRPCClient)
        self.operations_gateway_client = factory.create(OperationsGatewayGRPCClient)
