from clients.http.gateway.client_builder import HTTPClientBuilder

builder = HTTPClientBuilder()

users_gateway_client = builder.build_users_gateway()
accounts_gateway_client = builder.build_accounts_gateway()
documents_gateway_client = builder.build_documents_gateway()

create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

open_credit_card_account_response = accounts_gateway_client.open_credit_card_account(
    user_id=create_user_response.user.id
)
print('Open credit card account response:', open_credit_card_account_response)

get_tariff_document_response = documents_gateway_client.get_tariff_document(
    account_id=open_credit_card_account_response.account.id
)
print('Get tariff document response:', get_tariff_document_response)

get_contract_document_response = documents_gateway_client.get_contract_document(
    account_id=open_credit_card_account_response.account.id
)
print('Get contract document response:', get_contract_document_response)
