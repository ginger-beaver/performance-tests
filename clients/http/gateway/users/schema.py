from pydantic import EmailStr

from tools.camel_model import CamelModel


class UserSchema(CamelModel):
    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class GetUserResponseSchema(CamelModel):
    user: UserSchema


class CreateUserRequestSchema(CamelModel):
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class CreateUserResponseSchema(CamelModel):
    user: UserSchema
