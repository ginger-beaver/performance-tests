from clients.http.gateway.client_factory import HTTPClientFactory, build_gateway_http_client
from clients.http.gateway import UsersGatewayHTTPClient

factory = HTTPClientFactory(build_gateway_http_client)

users_gateway_client = factory.create(UsersGatewayHTTPClient)

create_user_response = users_gateway_client.create_user()
print('Create user data:', create_user_response)

get_user_response = users_gateway_client.get_user(create_user_response.user.id)
print('Get user data:', get_user_response)
