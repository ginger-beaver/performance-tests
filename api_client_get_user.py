from clients.http.gateway.client_builder import HTTPClientBuilder

builder = HTTPClientBuilder()

users_gateway_client = builder.build_users_gateway()

create_user_response = users_gateway_client.create_user()
print('Create user data:', create_user_response)

get_user_response = users_gateway_client.get_user(create_user_response.user.id)
print('Get user data:', get_user_response)
