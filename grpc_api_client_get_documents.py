from clients.grpc.gateway import UsersGatewayGRPCClient, AccountsGatewayGRPCClient, DocumentsGatewayGRPCClient
from clients.grpc.gateway.client_factory import GRPCClientFactory, build_gateway_grpc_client

factory = GRPCClientFactory(build_gateway_grpc_client)

users_gateway_client = factory.create(UsersGatewayGRPCClient)
accounts_gateway_client = factory.create(AccountsGatewayGRPCClient)
documents_gateway_client = factory.create(DocumentsGatewayGRPCClient)

create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

open_debit_card_account_response = accounts_gateway_client.open_credit_card_account(
    user_id=create_user_response.user.id
)
print('Open credit card account response:', open_debit_card_account_response)

get_tariff_document_response = documents_gateway_client.get_tariff_document(
    account_id=open_debit_card_account_response.account.id
)
print('Get tariff document response:', get_tariff_document_response)

get_contract_document_response = documents_gateway_client.get_contract_document(
    account_id=open_debit_card_account_response.account.id
)
print('Get contract document response:', get_contract_document_response)
