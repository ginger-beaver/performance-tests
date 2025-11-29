from clients.grpc.gateway.client_builder import GRPCClientBuilder

grpc_builder = GRPCClientBuilder()

users_gateway_client = grpc_builder.build_users_gateway()
accounts_gateway_client = grpc_builder.build_accounts_gateway()
cards_gateway_client = grpc_builder.build_cards_gateway()

create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(
    user_id=create_user_response.user.id
)
print('Open debit card account response:', open_debit_card_account_response)

issue_physical_card_response = cards_gateway_client.issue_physical_card(
    user_id=create_user_response.user.id,
    account_id=open_debit_card_account_response.account.id
)

print('Issue physical card response:', issue_physical_card_response)
