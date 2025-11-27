from datetime import datetime
from enum import StrEnum

from pydantic import HttpUrl

from tools.camel_model import CamelModel


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
    status: OperationStatus
    amount: float
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
    category: str


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
