# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


# TODO: Validate
class NanaError(Exception):
    """Base exception for Nana."""

    response: str | dict[str, Any] | None = None


# TODO: Validate
class HTTPError(NanaError):
    """Raised when HTTP request fails with unexpected status code."""

    # TODO: Validate
    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


# TODO: Validate
class ResourceNotFoundError(HTTPError):
    """Raised when the API reports that the requested resource does not exist."""


# TODO: Validate
class ContentNotFoundError(ResourceNotFoundError):
    """Raised when the requested content does not exist."""

    # TODO: Validate
    def __init__(
        self,
        content_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the content id and the originating response."""
        self.content_id = content_id
        super().__init__(status_code, response)


# TODO: Validate
class PageNotFoundError(ResourceNotFoundError):
    """Raised when the requested page does not exist.

    The API answers an unknown page id with a 500, so this is raised for both 404
    and 500 responses from the pages endpoint.
    """

    # TODO: Validate
    def __init__(
        self,
        page_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the page id and the originating response."""
        self.page_id = page_id
        super().__init__(status_code, response)


# TODO: Validate
class CSRFTokenError(NanaError):
    """Raised when a CSRF token and its matching cookie could not be collected."""

    # TODO: Validate
    def __init__(self, url: str) -> None:
        """Initialize with the url that was expected to hand out a token."""
        self.url = url
        super().__init__(f"No CSRF token found in the response from {url}")


# TODO: Validate
class EmptySearchResultsError(NanaError, ValueError):
    """Raised when a search matches nothing."""

    # TODO: Validate
    def __init__(
        self,
        query: str,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the query and the original response."""
        self.query = query
        self.response = response
        super().__init__(f"No search results for {query!r}")
