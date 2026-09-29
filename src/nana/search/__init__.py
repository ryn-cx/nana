# TODO: Validate
"""Contains the Search class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from nana.base_api_endpoint import BaseEndpoint
from nana.exceptions import EmptySearchResultsError
from nana.search.models import SearchModel, model_validate_json

if TYPE_CHECKING:
    from nana.search.models import Content

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Search(BaseEndpoint):
    """Contains the search.

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

    # TODO: Validate
    def __call__(self, query: str) -> SearchModel:
        """Download and parse the search file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(query), log_id)

    # TODO: Validate
    def download(self, query: str) -> str:
        """Download the search file."""
        log_id = self.get_log_id(self.download, locals())
        response = self._client.post(
            endpoint="api/v1/search",
            payload={"query": query},
            headers={"referer": "https://therokuchannel.roku.com/search"},
            log_id=log_id,
        )
        return self._validate_download(response, query)

    # TODO: Validate
    def _validate_download(self, response: str, query: str) -> str:
        # A query that matches nothing is answered with a 200 and an empty view.
        if not json.loads(response).get("view"):
            raise EmptySearchResultsError(query, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SearchModel:
        """Load a search file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

    # TODO: Validate
    @classmethod
    def extract_content(cls, data: SearchModel) -> list[Content]:
        """Extract the titles a search matched."""
        return [item.content for item in data.view]
