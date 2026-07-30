"""Contains the Page class."""

from __future__ import annotations

from collections.abc import Sequence
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, override
from urllib.parse import quote

from nana.base_api_endpoint import BaseEndpoint
from nana.exceptions import HTTPError, PageNotFoundError
from nana.page.models import PageModel

if TYPE_CHECKING:
    from nana.page.models import Content

logger = getLogger(__name__)
logger.addHandler(NullHandler())

NOT_FOUND_STATUS_CODES = (404, 500)
"""Status codes an unknown page id answers with. The API reports a missing page
as a server error rather than a 404."""


class Page(BaseEndpoint[PageModel]):
    """Manage the page file.

    A page is a browse screen, it holds the collections ("Recently Added",
    "Popular", ...) that the screen is built out of. Page ids come from
    `nana.menu`.

    Source: https://therokuchannel.roku.com/browse/{slug}

    Example request:
        - GET /api/v2/homescreen/pages/{page_id}/rendered HTTP/2
        - Host: therokuchannel.roku.com
        - User-Agent: __REDACTED__
        - Accept: */*
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - x-roku-reserved-session-id: __REDACTED__
        - x-roku-reserved-time-zone-offset: -07:00
        - x-roku-reserved-culture-code: en-US
        - x-roku-reserved-experiment-state: W10=
        - x-roku-reserved-amoeba-ids:
        - x-roku-reserved-experiment-configs: e30=
        - Connection: keep-alive
        - Referer: https://therokuchannel.roku.com/browse/{slug}
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers
    """

    _response_model = PageModel

    @override
    def download(self, page_id: str) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        endpoint = f"api/v2/homescreen/pages/{quote(page_id, safe='')}/rendered"
        try:
            return self._client.download(endpoint=endpoint, log_id=log_id)
        except HTTPError as err:
            if err.status_code in NOT_FOUND_STATUS_CODES:
                raise PageNotFoundError(
                    page_id,
                    err.status_code,
                    err.response,
                ) from err
            raise

    @override
    def download_and_parse(self, page_id: str) -> PageModel:
        return self.parse(self.download(page_id))

    def extract_content(
        self,
        input_data: PageModel
        | dict[str, Any]
        | Sequence[PageModel | dict[str, Any]],
    ) -> list[Content]:
        """Extracts the content of every collection from one or more files.

        A title that appears in more than one collection is returned more than
        once, the collections it came from are not deduplicated.
        """
        responses = input_data if isinstance(input_data, Sequence) else [input_data]

        result: list[Content] = []
        for response in responses:
            parsed = response if isinstance(response, PageModel) else self.parse(response)
            for collection in parsed.collections:
                result.extend(item.content for item in collection.view)
        return result
