from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.base_client import HTTPClient


class GetAccountsQueryDict(TypedDict):
    userId: str


class OpenDepositAccountRequestDict(TypedDict):
    userId: str


class OpenSavingsAccountRequestDict(TypedDict):
    userId: str


class OpenDebitCardAccountRequestDict(TypedDict):
    userId: str


class OpenCreditCardAccountRequestDict(TypedDict):
    userId: str


class AccountsGatewayHTTPClient(HTTPClient):

    def get_accounts_api(self, query: GetAccountsQueryDict) -> Response:
        return self.get("/api/v1/accounts", params=QueryParams(**query))

    def open_deposit_account_api(self, request: OpenDepositAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-deposit-account", json=request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-savings-account", json=request)

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-debit-card-account", json=request)

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-credit-card-account", json=request)
