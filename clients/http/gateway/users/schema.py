from pydantic import EmailStr, Field

from tools.camel_model import CamelModel
from tools.fakers import fake

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
    email: EmailStr = Field(default_factory=fake.email)
    last_name: str = Field(default_factory=fake.last_name)
    first_name: str = Field(default_factory=fake.first_name)
    middle_name: str = Field(default_factory=fake.middle_name)
    phone_number: str = Field(default_factory=fake.phone_number)


class CreateUserResponseSchema(CamelModel):
    user: UserSchema
