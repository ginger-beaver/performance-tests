from datetime import datetime
from enum import StrEnum

from pydantic import HttpUrl, Field

from tools.camel_model import CamelModel
from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(CamelModel):
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str
    category: str
    created_at: datetime
    account_id: str


class OperationReceiptSchema(CamelModel):
    url: HttpUrl
    document: str


class OperationsSummarySchema(CamelModel):
    spent_amount: float
    received_amount: float
    cashback_amount: float


class GetOperationResponseSchema(CamelModel):
    operation: OperationSchema


class GetOperationsQuerySchema(CamelModel):
    account_id: str


class GetOperationsResponseSchema(CamelModel):
    operations: list[OperationSchema]


class GetOperationsSummaryQuerySchema(CamelModel):
    account_id: str


class GetOperationsSummaryResponseSchema(CamelModel):
    summary: OperationsSummarySchema


class GetOperationReceiptResponseSchema(CamelModel):
    receipt: OperationReceiptSchema


class MakeOperationRequestSchema(CamelModel):
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str
    account_id: str


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeFeeOperationResponseSchema(CamelModel):
    operation: OperationSchema


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeTopUpOperationResponseSchema(CamelModel):
    operation: OperationSchema


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeCashbackOperationResponseSchema(CamelModel):
    operation: OperationSchema


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeTransferOperationResponseSchema(CamelModel):
    operation: OperationSchema


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    category: str = Field(default_factory=fake.category)


class MakePurchaseOperationResponseSchema(CamelModel):
    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeBillPaymentOperationResponseSchema(CamelModel):
    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeCashWithdrawalOperationResponseSchema(CamelModel):
    operation: OperationSchema
