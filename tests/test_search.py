# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from nana.exceptions import EmptySearchResultsError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from nana import Nana
    from nana.search import Search

SERIES_QUERY = "walker texas ranger"
SERIES_TITLE = "Walker, Texas Ranger"
MOVIE_QUERY = "the terminator"
NO_RESULTS_QUERY = "zzzzqqqqxxxxnotathing"

QUERIES = [SERIES_QUERY, MOVIE_QUERY]


@pytest.fixture(scope="session")
def client(client: Nana) -> Search:
    return client.search


@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Search, query: str) -> None:
    download_and_save(client, query, lambda: client.download(query))


@pytest.mark.parametrize("query", QUERIES)
def test_parse(client: Search, query: str) -> None:
    assert parsed_json(client, query).view


def test_extract_content(client: Search) -> None:
    content = client.extract_content(parsed_json(client, SERIES_QUERY))
    # Search is fuzzy, so related titles come back alongside the match.
    assert SERIES_TITLE in [item.title for item in content]


def test_download_no_results(client: Search) -> None:
    assert_error(
        client,
        NO_RESULTS_QUERY,
        lambda: client.download(NO_RESULTS_QUERY),
        EmptySearchResultsError,
    )
