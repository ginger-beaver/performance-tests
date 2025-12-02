from typing import Any, TypedDict

from httpx import Client, URL, Response, QueryParams


class HTTPClientExtensions(TypedDict, total=False):
    route: str


class HTTPClient:
    def __init__(self, client: Client):
        self.client = client

    def get(
            self,
            url: URL | str,
            params: QueryParams | None = None,
            extensions: HTTPClientExtensions | None = None
    ) -> Response:
        return self.client.get(url, params=params, extensions=extensions)

    def post(
            self,
            url: str,
            json: Any | None = None,
            extensions: HTTPClientExtensions | None = None
    ) -> Response:
        return self.client.post(url=url, json=json, extensions=extensions)
