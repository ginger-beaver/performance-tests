from pydantic import HttpUrl

from tools.camel_model import CamelModel


class DocumentSchema(CamelModel):
    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(CamelModel):
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(CamelModel):
    contract: DocumentSchema
