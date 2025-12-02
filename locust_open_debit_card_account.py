from locust import User, task, between

from clients.http.gateway import UsersGatewayHTTPClient, AccountsGatewayHTTPClient
from clients.http.gateway.client_factory import HTTPClientFactory, build_gateway_locust_http_client
from clients.http.gateway.users.schema import CreateUserResponseSchema


class OpenDebitCardAccountScenarioUser(User):
    wait_time = between(1, 3)
    host = "localhost"
    factory: HTTPClientFactory = None

    users_gateway_client: UsersGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient

    create_user_response: CreateUserResponseSchema

    def on_start(self) -> None:
        if OpenDebitCardAccountScenarioUser.factory is None:
            OpenDebitCardAccountScenarioUser.factory = HTTPClientFactory(
                lambda: build_gateway_locust_http_client(self.environment)
            )

        self.users_gateway_client = OpenDebitCardAccountScenarioUser.factory.create(UsersGatewayHTTPClient)
        self.accounts_gateway_client = self.factory.create(AccountsGatewayHTTPClient)

        self.create_user_response = self.users_gateway_client.create_user()


    @task
    def open_debit_card_account(self):
        self.accounts_gateway_client.open_debit_card_account(self.create_user_response.user.id)
