# TODO: Validate
"""Contains the Content class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override
from urllib.parse import quote, urlencode

from nana.base_api_endpoint import BaseEndpoint
from nana.content.constants import (
    CONTENT_URL,
    EXPAND,
    FEATURE_INCLUDE,
    FILTER,
    INCLUDE,
)
from nana.content.models import ContentModel
from nana.exceptions import ContentNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Content(BaseEndpoint[ContentModel]):
    """Manage the content file.

    One endpoint covers every kind of content, the `type` field says which one
    was returned. A series includes its seasons and their episodes, so a series,
    a season and an episode are all reachable by their own id.

    Source: https://therokuchannel.roku.com/details/{content_id}/{slug}

    Example request:
        - GET /api/v2/homescreen/content/{content_url}?
            - expand={expand}&
            - include={include}&
            - filter={filter}&
            - featureInclude={feature_include}
            - HTTP/2
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
        - Referer: https://therokuchannel.roku.com/details/{content_id}/{slug}
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers
    """

    _response_model = ContentModel

    @staticmethod
    def endpoint(
        content_id: str,
        *,
        expand: str,
        include: str,
        filters: str,
        feature_include: str,
    ) -> str:
        """Build the endpoint for a content id.

        The endpoint proxies a content URL, so the whole URL, query string
        included, is escaped into a single path segment.
        """
        query = urlencode(
            {
                "expand": expand,
                "include": include,
                "filter": filters,
                "featureInclude": feature_include,
            },
        )
        return "api/v2/homescreen/content/" + quote(
            f"{CONTENT_URL}{content_id}?{query}",
            safe="",
        )

    @override
    def download(
        self,
        content_id: str,
        *,
        expand: str = EXPAND,
        include: str = INCLUDE,
        filters: str = FILTER,
        feature_include: str = FEATURE_INCLUDE,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download(
                endpoint=self.endpoint(
                    content_id,
                    expand=expand,
                    include=include,
                    filters=filters,
                    feature_include=feature_include,
                ),
                headers={
                    "referer": (
                        f"https://therokuchannel.roku.com/details/{content_id}"
                    ),
                },
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise ContentNotFoundError(
                content_id,
                err.status_code,
                err.response,
            ) from err

    @override
    def download_and_parse(
        self,
        content_id: str,
        *,
        expand: str = EXPAND,
        include: str = INCLUDE,
        filters: str = FILTER,
        feature_include: str = FEATURE_INCLUDE,
    ) -> ContentModel:
        return self.parse(
            self.download(
                content_id,
                expand=expand,
                include=include,
                filters=filters,
                feature_include=feature_include,
            ),
        )
