# TODO: Validate
"""Contains the Nana class."""

from __future__ import annotations

import re
import time
import uuid
from datetime import UTC, datetime, timedelta
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from get_around import GetAround

from nana.content import Content
from nana.exceptions import CSRFTokenError, HTTPError, ResourceNotFoundError
from nana.menu import Menu
from nana.page import Page
from nana.search import Search

if TYPE_CHECKING:
    import httpx

logger = getLogger(__name__)
logger.addHandler(NullHandler())

API_DOMAIN = "therokuchannel.roku.com"

CSRF_LIFETIME = timedelta(minutes=5)
"""How long a token is reused for. The site refreshes every five minutes."""

_CSRF_COOKIE = re.compile(r"_csrf=([^;,\s]+)")
"""Matches the `_csrf` cookie in a `set-cookie` header."""

EMPTY_LIST_BASE64 = "W10="
"""Base64 of `[]`, sent when no experiments are active."""

EMPTY_OBJECT_BASE64 = "e30="
"""Base64 of `{}`, sent when no experiment configs are active."""


# TODO: Validate
def _local_time_zone_offset() -> str:
    """Return the local UTC offset in the `-07:00` format the API expects."""
    offset = datetime.now().astimezone().strftime("%z")
    return f"{offset[:-2]}:{offset[-2:]}"


# TODO: Validate
class Nana:
    """The Roku Channel API wrapper."""

    # TODO: Validate
    def __init__(
        self,
        get_around_client: GetAround | None = None,
        culture_code: str = "en-US",
        channel_store_code: str = "us",
        time_zone_offset: str | None = None,
    ) -> None:
        """Initialize the Nana client.

        The client holds one attribute per endpoint, so `client.content(id)`
        looks a title up and `client.content.download(id)` and
        `client.content.load(data)` are the halves of it.
        """
        self.culture_code = culture_code
        self.channel_store_code = channel_store_code
        self.time_zone_offset = time_zone_offset or _local_time_zone_offset()
        self.get_around_client = get_around_client or GetAround()
        self.session_id = str(uuid.uuid4())
        self._csrf_token_value = ""
        self._csrf_cookie_value = ""
        self._csrf_expires_at = datetime.now(tz=UTC)

        self.content = Content(self)
        self.page = Page(self)
        self.menu = Menu(self)
        self.search = Search(self)

    # TODO: Validate
    @property
    def _csrf(self) -> tuple[str, str]:
        """The CSRF token and the `_csrf` cookie value that validates it."""
        if not self._csrf_token_value or self._csrf_expires_at < datetime.now(UTC):
            self._download_csrf()
        return self._csrf_token_value, self._csrf_cookie_value

    # TODO: Validate
    def _download_csrf(self) -> None:
        """Collect a CSRF token and the cookie it was issued with.

        Raises:
            HTTPError: If the request is answered with anything but a 200.
            CSRFTokenError: If either half of the pair is missing.
        """
        url = f"https://{API_DOMAIN}/api/v1/csrf"
        logger.debug("Downloading CSRF token:")
        start = time.monotonic()
        response = self.get_around_client.get(url, headers=self._csrf_headers())
        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded CSRF token (%.4f s)", time.monotonic() - start)

        # The token is only accepted alongside the cookie it was issued with, so
        # both halves have to be kept. The cookie is only reissued when the
        # request arrived without one.
        token = response.json().get("csrf")
        self._capture_csrf_cookie(response)
        if not token or not self._csrf_cookie_value:
            raise CSRFTokenError(url)

        self._csrf_token_value = token
        self._csrf_expires_at = datetime.now(tz=UTC) + CSRF_LIFETIME

    # TODO: Validate
    def _csrf_headers(self) -> dict[str, str]:
        """Headers for a request that carries the CSRF cookie, if one is held."""
        headers = self._base_headers()
        if self._csrf_cookie_value:
            headers["cookie"] = f"_csrf={self._csrf_cookie_value}"
        return headers

    # TODO: Validate
    def _capture_csrf_cookie(self, response: httpx.Response) -> None:
        """Store the `_csrf` cookie if the response set one.

        The cookie is read straight out of the headers instead of the client's
        cookie jar because requests may be relayed through another host, which
        stops the jar from matching the cookie to the Roku domain.
        """
        for header in response.headers.get_list("set-cookie"):
            if match := _CSRF_COOKIE.search(header):
                self._csrf_cookie_value = match.group(1)
                return

    # TODO: Validate
    def _base_headers(self) -> dict[str, str]:
        """Headers the site sends on every request."""
        return {
            "accept": "*/*",
            "x-roku-reserved-session-id": self.session_id,
            "x-roku-reserved-time-zone-offset": self.time_zone_offset,
            "x-roku-reserved-culture-code": self.culture_code,
            "x-roku-reserved-channel-store-code": self.channel_store_code,
            "x-roku-reserved-experiment-state": EMPTY_LIST_BASE64,
            "x-roku-reserved-experiment-configs": EMPTY_OBJECT_BASE64,
            "x-roku-reserved-amoeba-ids": "",
        }

    # TODO: Validate
    def download(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        log_id: str = "",
    ) -> str:
        """Download from the API and return the body as text.

        Raises:
            ResourceNotFoundError: If the API answered with a 404.
            HTTPError: For any other status that is not a 200.
        """
        logger.debug("Downloading: %s", log_id)
        url = f"https://{API_DOMAIN}/{endpoint}"
        start = time.monotonic()
        response = self.get_around_client.get(
            url,
            params=params,
            headers=self._base_headers() | (headers or {}),
        )
        self._capture_csrf_cookie(response)
        self._raise_for_status(response)

        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return response.text

    # TODO: Validate
    def post(
        self,
        endpoint: str,
        payload: dict[str, Any],
        headers: dict[str, str] | None = None,
        log_id: str = "",
    ) -> str:
        """Post to the API and return the body as text.

        Every non-GET request is rejected unless it carries a CSRF token and the
        cookie that token was issued with.

        Raises:
            ResourceNotFoundError: If the API answered with a 404.
            HTTPError: For any other status that is not a 200.
        """
        token, cookie = self._csrf
        request_headers = self._base_headers() | {
            "csrf-token": token,
            "cookie": f"_csrf={cookie}",
        }
        request_headers |= headers or {}

        logger.debug("Downloading: %s", log_id)
        url = f"https://{API_DOMAIN}/{endpoint}"
        start = time.monotonic()
        response = self.get_around_client.post(
            url,
            json=payload,
            headers=request_headers,
        )
        self._capture_csrf_cookie(response)
        self._raise_for_status(response)

        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return response.text

    # TODO: Validate
    @staticmethod
    def _raise_for_status(response: httpx.Response) -> None:
        """Raise if the response is not a 200.

        Raises:
            ResourceNotFoundError: If the API answered with a 404.
            HTTPError: For any other status that is not a 200.
        """
        if response.status_code == HTTPStatus.OK:
            return
        if response.status_code == HTTPStatus.NOT_FOUND:
            raise ResourceNotFoundError(response.status_code, response.text)
        raise HTTPError(response.status_code, response.text)
