from enum import StrEnum

from clients.http.gateway.cards.schema import CardSchema
from tools.camel_model import CamelModel


class AccountType(StrEnum):
    DEPOSIT = "DEPOSIT"
    SAVINGS = "SAVINGS"
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"


class AccountStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    PENDING_CLOSURE = "PENDING_CLOSURE"


class AccountSchema(CamelModel):
    id: str
    type: AccountType
    cards: list[CardSchema]
    status: AccountStatus
    balance: float


class GetAccountsQuerySchema(CamelModel):
    user_id: str


class GetAccountsResponseSchema(CamelModel):
    accounts: list[AccountSchema]


class OpenDepositAccountRequestSchema(CamelModel):
    user_id: str


class OpenDepositAccountResponseSchema(CamelModel):
    account: AccountSchema


class OpenSavingsAccountRequestSchema(CamelModel):
    user_id: str


class OpenSavingsAccountResponseSchema(CamelModel):
    account: AccountSchema


class OpenDebitCardAccountRequestSchema(CamelModel):
    user_id: str


class OpenDebitCardAccountResponseSchema(CamelModel):
    account: AccountSchema


class OpenCreditCardAccountRequestSchema(CamelModel):
    user_id: str


class OpenCreditCardAccountResponseSchema(CamelModel):
    account: AccountSchema
