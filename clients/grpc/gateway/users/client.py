from grpc import Channel

from clients.grpc.base_client import GRPCClient
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserRequest, GetUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from tools.fakers import fake


class UsersGatewayGRPCClient(GRPCClient):

    def __init__(self, channel: Channel):
        super().__init__(channel)

        self.stub = UsersGatewayServiceStub(channel)

    def get_user_api(self, request: GetUserRequest) -> GetUserResponse:
        return self.stub.GetUser(request)

    def create_user_api(self, request: CreateUserRequest) -> CreateUserResponse:
        return self.stub.CreateUser(request)

    def get_user(self, user_id: str) -> GetUserResponse:
        request = GetUserRequest(id=user_id)
        return self.get_user_api(request)

    def create_user(self) -> CreateUserResponse:
        request = CreateUserRequest(
            email=fake.email(),
            last_name=fake.last_name(),
            first_name=fake.first_name(),
            middle_name=fake.middle_name(),
            phone_number=fake.phone_number()
        )
        return self.create_user_api(request)
