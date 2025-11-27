from datetime import date
from enum import StrEnum

from tools.camel_model import CamelModel


class CardType(StrEnum):
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"


class CardStatus(StrEnum):
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"


class CardPaymentSystem(StrEnum):
    MASTERCARD = "MASTERCARD"
    VISA = "VISA"


class CardSchema(CamelModel):
    id: str
    pin: str
    cvv: str
    type: CardType
    status: CardStatus
    account_id: str
    card_number: str
    card_holder: str
    expiry_date: date
    payment_system: CardPaymentSystem


class IssueVirtualCardRequestSchema(CamelModel):
    user_id: str
    account_id: str


class IssueVirtualCardResponseSchema(CamelModel):
    card: CardSchema


class IssuePhysicalCardRequestSchema(CamelModel):
    user_id: str
    account_id: str


class IssuePhysicalCardResponseSchema(CamelModel):
    card: CardSchema
