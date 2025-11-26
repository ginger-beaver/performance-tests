from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.base_client import HTTPClient


class GetOperationsQueryDict(TypedDict):
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    accountId: str


class MakeOperationRequestDict(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    pass


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    category: str


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    pass


class OperationsGatewayHTTPClient(HTTPClient):

    def get_operation_api(self, operation_id: str) -> Response:
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)
