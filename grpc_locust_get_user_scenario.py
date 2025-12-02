from locust import User, between, task

from clients.grpc.gateway.client_factory import GRPCClientFactory, build_gateway_locust_grpc_client
from clients.grpc.gateway.users.client import UsersGatewayGRPCClient
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class GetUserScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)
    factory: GRPCClientFactory = None

    users_gateway_client: UsersGatewayGRPCClient
    create_user_response: CreateUserResponse

    def on_start(self) -> None:
        if GetUserScenarioUser.factory is None:
            GetUserScenarioUser.factory = GRPCClientFactory(lambda: build_gateway_locust_grpc_client(self.environment))

        self.users_gateway_client = GetUserScenarioUser.factory.create(UsersGatewayGRPCClient)

        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def get_user(self):
        self.users_gateway_client.get_user(self.create_user_response.user.id)
