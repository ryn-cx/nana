# TODO: Validate
"""Contains the Menu class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from nana.base_api_endpoint import BaseEndpoint
from nana.menu.models import MenuModel, model_validate_json

if TYPE_CHECKING:
    from nana.menu.models import ViewItem2

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PAGE_TYPE = "page"
"""Menu entries of this type point at a browse page instead of a site path."""


# TODO: Validate
class Menu(BaseEndpoint):
    """Contains the menu.

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

    # TODO: Validate
    def __call__(self) -> MenuModel:
        """Download and parse the menu file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(), log_id)

    # TODO: Validate
    def download(self) -> str:
        """Download the menu file."""
        log_id = self.get_log_id(self.download, locals())
        return self._client.download(
            endpoint="api/v1/navigation/menu",
            headers={"referer": "https://therokuchannel.roku.com/"},
            log_id=log_id,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> MenuModel:
        """Load a menu file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

    # TODO: Validate
    @classmethod
    def extract_pages(cls, data: MenuModel) -> list[ViewItem2]:
        """Extract the browse page entries from a menu.

        Pages sit two levels down, under the menu section ("Featured", "Genres",
        ...) that groups them.
        """
        return [
            entry
            for item in data.view
            for section in item.view or []
            for entry in section.view
            if entry.meta.type == PAGE_TYPE
        ]
