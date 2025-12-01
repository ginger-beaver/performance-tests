from clients.grpc.gateway import UsersGatewayGRPCClient
from clients.grpc.gateway.client_factory import GRPCClientFactory, build_gateway_grpc_client

factory = GRPCClientFactory(build_gateway_grpc_client)
users_gateway_client = factory.create(UsersGatewayGRPCClient)

create_user_response = users_gateway_client.create_user()
print('Create user data:', create_user_response)

get_user_response = users_gateway_client.get_user(create_user_response.user.id)
print('Get user data:', get_user_response)
