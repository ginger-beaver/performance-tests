from locust import User, between, task

from clients.http.gateway import UsersGatewayHTTPClient
from clients.http.gateway.client_factory import HTTPClientFactory, build_gateway_locust_http_client
from clients.http.gateway.users.schema import CreateUserResponseSchema


class GetUserScenarioUser(User):
    wait_time = between(1, 3)
    host = "localhost"
    factory: HTTPClientFactory = None

    users_gateway_client: UsersGatewayHTTPClient
    create_user_response: CreateUserResponseSchema

    def on_start(self) -> None:
        if GetUserScenarioUser.factory is None:
            GetUserScenarioUser.factory = HTTPClientFactory(lambda: build_gateway_locust_http_client(self.environment))

        self.users_gateway_client = GetUserScenarioUser.factory.create(UsersGatewayHTTPClient)

        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def get_user(self):
        self.users_gateway_client.get_user(self.create_user_response.user.id)
