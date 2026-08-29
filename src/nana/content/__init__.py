# TODO: Validate
"""Contains the Content class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from urllib.parse import quote, urlencode

from nana.base_api_endpoint import BaseEndpoint
from nana.content.constants import EXPAND, FEATURE_INCLUDE, FILTER, INCLUDE
from nana.content.models import ContentModel, model_validate_json
from nana.exceptions import ContentNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Content(BaseEndpoint):
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

    # TODO: Validate
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
        content_url = f"https://content.sr.roku.com/content/v1/roku-trc/{content_id}"
        return "api/v2/homescreen/content/" + quote(
            f"{content_url}?{query}",
            safe="",
        )

    # TODO: Validate
    def __call__(
        self,
        content_id: str,
        *,
        expand: str = EXPAND,
        include: str = INCLUDE,
        filters: str = FILTER,
        feature_include: str = FEATURE_INCLUDE,
    ) -> ContentModel:
        """Look the content up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                content_id,
                expand=expand,
                include=include,
                filters=filters,
                feature_include=feature_include,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        content_id: str,
        *,
        expand: str = EXPAND,
        include: str = INCLUDE,
        filters: str = FILTER,
        feature_include: str = FEATURE_INCLUDE,
    ) -> str:
        """Download the content file."""
        log_id = self.get_log_id(self.download, locals())
        referer = f"https://therokuchannel.roku.com/details/{content_id}"
        try:
            return self._client.download(
                endpoint=self.endpoint(
                    content_id,
                    expand=expand,
                    include=include,
                    filters=filters,
                    feature_include=feature_include,
                ),
                headers={"referer": referer},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise ContentNotFoundError(
                content_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ContentModel:
        """Read a downloaded content file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
