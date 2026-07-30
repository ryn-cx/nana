"""Contains the Search class."""

from __future__ import annotations

from collections.abc import Sequence
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, override

from nana.base_api_endpoint import BaseEndpoint
from nana.exceptions import EmptySearchResultsError
from nana.search.models import SearchModel

if TYPE_CHECKING:
    from nana.search.models import Content

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Search(BaseEndpoint[SearchModel]):
    """Manage the search file.

    Search is the only endpoint that is not a GET, so it is the only one that
    needs a CSRF token.

    Source: https://therokuchannel.roku.com/search/{query}

    Example request:
        - POST /api/v1/search HTTP/2
        - Host: therokuchannel.roku.com
        - User-Agent: __REDACTED__
        - Accept: */*
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Content-Type: application/json
        - csrf-token: __REDACTED__
        - x-roku-reserved-session-id: __REDACTED__
        - x-roku-reserved-time-zone-offset: -07:00
        - x-roku-reserved-culture-code: en-US
        - x-roku-reserved-experiment-state: W10=
        - x-roku-reserved-amoeba-ids:
        - x-roku-reserved-experiment-configs: e30=
        - Connection: keep-alive
        - Referer: https://therokuchannel.roku.com/search/{query}
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers

        {"query": "{query}"}
    """

    _response_model = SearchModel

    @override
    def download(self, query: str) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        response = self._client.post(
            endpoint="api/v1/search",
            payload={"query": query},
            headers={"referer": "https://therokuchannel.roku.com/search"},
            log_id=log_id,
        )
        return self._validate_download(response, query)

    def _validate_download(
        self,
        response: dict[str, Any],
        query: str,
    ) -> dict[str, Any]:
        # A query that matches nothing is answered with a 200 and an empty view.
        if not response.get("view"):
            raise EmptySearchResultsError(query, response)
        return response

    @override
    def download_and_parse(self, query: str) -> SearchModel:
        return self.parse(self.download(query))

    def extract_content(
        self,
        input_data: SearchModel
        | dict[str, Any]
        | Sequence[SearchModel | dict[str, Any]],
    ) -> list[Content]:
        """Extracts the matched content from one or more files."""
        responses = input_data if isinstance(input_data, Sequence) else [input_data]

        result: list[Content] = []
        for response in responses:
            parsed = (
                response if isinstance(response, SearchModel) else self.parse(response)
            )
            result.extend(item.content for item in parsed.view)
        return result
