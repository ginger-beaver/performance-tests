from locust import User, between, task

from clients.grpc.gateway import UsersGatewayGRPCClient, AccountsGatewayGRPCClient
from clients.grpc.gateway.client_factory import GRPCClientFactory, build_gateway_locust_grpc_client
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class GetUserScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)
    factory: GRPCClientFactory = None

    users_gateway_client: UsersGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient
    create_user_response: CreateUserResponse

    def on_start(self) -> None:
        if GetUserScenarioUser.factory is None:
            GetUserScenarioUser.factory = GRPCClientFactory(lambda: build_gateway_locust_grpc_client(self.environment))

        self.users_gateway_client = GetUserScenarioUser.factory.create(UsersGatewayGRPCClient)
        self.accounts_gateway_client = GetUserScenarioUser.factory.create(AccountsGatewayGRPCClient)

        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        self.accounts_gateway_client.open_debit_card_account(self.create_user_response.user.id)
