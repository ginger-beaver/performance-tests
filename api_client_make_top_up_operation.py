from clients.http.gateway import UsersGatewayHTTPClient, AccountsGatewayHTTPClient, OperationsGatewayHTTPClient
from clients.http.gateway.client_factory import HTTPClientFactory, build_gateway_http_client

factory = HTTPClientFactory(build_gateway_http_client)

users_gateway_client = factory.create(UsersGatewayHTTPClient)
accounts_gateway_client = factory.create(AccountsGatewayHTTPClient)
operations_gateway_client = factory.create(OperationsGatewayHTTPClient)

create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(
    user_id=create_user_response.user.id
)
print('Open debit card account response:', open_debit_card_account_response)

make_top_up_operation_response = operations_gateway_client.make_top_up_operation(
    card_id=open_debit_card_account_response.account.cards[0].id,
    account_id=open_debit_card_account_response.account.id
)
print('Make top up operation response:', make_top_up_operation_response)
