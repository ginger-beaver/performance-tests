from dataclasses import dataclass
from typing import Any, Optional

from httpx import Client, URL, Response, QueryParams


@dataclass
class HTTPClientExtensions:
    route: Optional[str] = None


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
