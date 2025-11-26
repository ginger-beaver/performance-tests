from httpx import Response

from clients.http.base_client import HTTPClient


class DocumentsGatewayHTTPClient(HTTPClient):

    def get_tariff_document_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/documents/contract-document/{account_id}")
