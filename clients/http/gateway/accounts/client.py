from httpx import Response, QueryParams

from clients.http.base_client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.accounts.schema import (
    GetAccountsQuerySchema,
    GetAccountsResponseSchema,
    OpenDepositAccountRequestSchema,
    OpenDepositAccountResponseSchema,
    OpenSavingsAccountRequestSchema,
    OpenSavingsAccountResponseSchema,
    OpenDebitCardAccountRequestSchema,
    OpenDebitCardAccountResponseSchema,
    OpenCreditCardAccountRequestSchema,
    OpenCreditCardAccountResponseSchema
)
from tools.routes import APIRoutes


class AccountsGatewayHTTPClient(HTTPClient):

    def get_accounts_api(self, query: GetAccountsQuerySchema):
        return self.get(
            APIRoutes.ACCOUNTS,
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route=APIRoutes.ACCOUNTS)
        )

    def open_deposit_account_api(self, request: OpenDepositAccountRequestSchema) -> Response:
        return self.post(
            f"{APIRoutes.ACCOUNTS}/open-deposit-account",
            json=request.model_dump(by_alias=True)
        )

    def open_savings_account_api(self, request: OpenSavingsAccountRequestSchema) -> Response:
        return self.post(
            f"{APIRoutes.ACCOUNTS}/open-savings-account",
            json=request.model_dump(by_alias=True)
        )

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestSchema) -> Response:
        return self.post(
            f"{APIRoutes.ACCOUNTS}/open-debit-card-account",
            json=request.model_dump(by_alias=True)
        )

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestSchema) -> Response:
        return self.post(
            f"{APIRoutes.ACCOUNTS}/open-credit-card-account",
            json=request.model_dump(by_alias=True)
        )

    def get_accounts(self, user_id: str) -> GetAccountsResponseSchema:
        query = GetAccountsQuerySchema(user_id=user_id)
        response = self.get_accounts_api(query)
        return GetAccountsResponseSchema.model_validate_json(response.text)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseSchema:
        request = OpenDepositAccountRequestSchema(user_id=user_id)
        response = self.open_deposit_account_api(request)
        return OpenDepositAccountResponseSchema.model_validate_json(response.text)

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseSchema:
        request = OpenSavingsAccountRequestSchema(user_id=user_id)
        response = self.open_savings_account_api(request)
        return OpenSavingsAccountResponseSchema.model_validate_json(response.text)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseSchema:
        request = OpenDebitCardAccountRequestSchema(user_id=user_id)
        response = self.open_debit_card_account_api(request)
        return OpenDebitCardAccountResponseSchema.model_validate_json(response.text)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseSchema:
        request = OpenCreditCardAccountRequestSchema(user_id=user_id)
        response = self.open_credit_card_account_api(request)
        return OpenCreditCardAccountResponseSchema.model_validate_json(response.text)
