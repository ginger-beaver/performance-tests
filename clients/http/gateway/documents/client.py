from httpx import Response

from clients.http.base_client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.documents.schema import (
    GetTariffDocumentResponseSchema,
    GetContractDocumentResponseSchema
)
from tools.routes import APIRoutes


class DocumentsGatewayHTTPClient(HTTPClient):

    def get_tariff_document_api(self, account_id: str) -> Response:
        return self.get(
            f"{APIRoutes.DOCUMENTS}/tariff-document/{account_id}",
            extensions=HTTPClientExtensions(route=f"{APIRoutes.DOCUMENTS}/tariff-document/{{account_id}}")
        )

    def get_contract_document_api(self, account_id: str) -> Response:
        return self.get(
            f"{APIRoutes.DOCUMENTS}/contract-document/{account_id}",
            extensions=HTTPClientExtensions(route=f"{APIRoutes.DOCUMENTS}/contract-document/{{account_id}}")
        )

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseSchema:
        response = self.get_tariff_document_api(account_id)
        return GetTariffDocumentResponseSchema.model_validate_json(response.text)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseSchema:
        response = self.get_contract_document_api(account_id)
        return GetContractDocumentResponseSchema.model_validate_json(response.text)
