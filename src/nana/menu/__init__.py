"""Contains the Menu class."""

from __future__ import annotations

from collections.abc import Sequence
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, override

from nana.base_api_endpoint import BaseEndpoint
from nana.menu.models import MenuModel

if TYPE_CHECKING:
    from nana.menu.models import ViewItem2

PAGE_TYPE = "page"
"""Menu entries of this type point at a browse page instead of a site path."""

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Menu(BaseEndpoint[MenuModel]):
    """Manage the menu file.

    The menu is the site navigation, it is the only place the ids of the browse
    pages are published.

    Source: https://therokuchannel.roku.com

    Example request:
        - GET /api/v1/navigation/menu HTTP/2
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
        - Referer: https://therokuchannel.roku.com/
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers
    """

    _response_model = MenuModel

    @override
    def download(self) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        return self._client.download(
            endpoint="api/v1/navigation/menu",
            headers={"referer": "https://therokuchannel.roku.com/"},
            log_id=log_id,
        )

    @override
    def download_and_parse(self) -> MenuModel:
        return self.parse(self.download())

    def extract_pages(
        self,
        input_data: MenuModel
        | dict[str, Any]
        | Sequence[MenuModel | dict[str, Any]],
    ) -> list[ViewItem2]:
        """Extracts the browse pages from one or more files.

        Pages sit two levels down, under the menu section ("Featured", "Genres",
        ...) that groups them. Entries that link to a site path rather than a
        page are skipped.
        """
        responses = input_data if isinstance(input_data, Sequence) else [input_data]

        result: list[ViewItem2] = []
        for response in responses:
            parsed = (
                response if isinstance(response, MenuModel) else self.parse(response)
            )
            for item in parsed.view:
                for section in item.view or []:
                    result.extend(
                        entry
                        for entry in section.view
                        if entry.meta.type == PAGE_TYPE
                    )
        return result
