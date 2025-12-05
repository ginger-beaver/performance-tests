from httpx import Response

from clients.http.base_client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.users.schema import (
    GetUserResponseSchema,
    CreateUserRequestSchema,
    CreateUserResponseSchema
)
from tools.routes import APIRoutes


class UsersGatewayHTTPClient(HTTPClient):

    def get_user_api(self, user_id: str) -> Response:
        return self.get(
            f"{APIRoutes.USERS}/{user_id}",
            extensions=HTTPClientExtensions(route=f"{APIRoutes.USERS}/{{user_id}}")
        )

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        return self.post(APIRoutes.USERS, json=request.model_dump(by_alias=True))

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    def create_user(self) -> CreateUserResponseSchema:
        request = CreateUserRequestSchema()
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)
