# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from nana.exceptions import EmptySearchResultsError
from nana.search import Search
from nana.search.models import SearchModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from nana import Nana

QUERIES = [
    pytest.param("walker texas ranger", id="walker texas ranger series"),
    pytest.param("blade runner 2049", id="blade runner 2049 movie"),
]


# TODO: Validate
class SearchTest(RecordedEndpoint):
    MODEL = SearchModel
    IGNORED = (
        "SearchModel.trace_id",
        "Content.current_time",
        "TrackerOverrides.query_params",
        "TrackerOverrides1.item_server_data",
    )


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Nana, query: str) -> None:
    SearchTest.download_test(query, lambda: client.search.download(query))


# TODO: Validate
@pytest.mark.parametrize(
    ("query", "title"),
    [
        pytest.param(
            "walker texas ranger",
            "Walker, Texas Ranger",
            id="walker texas ranger series",
        ),
        pytest.param("blade runner 2049", "Blade Runner 2049", id="blade runner movie"),
    ],
)
def test_parse(client: Nana, query: str, title: str) -> None:
    matches = Search.extract_content(
        client.search.load(SearchTest.recorded_content(query)),
    )
    assert title in [match.title for match in matches]


# TODO: Validate
@pytest.mark.parametrize(
    "query",
    [pytest.param("zzzzqqqqxxxxnotathing", id="query that matches nothing")],
)
def test_download_invalid(client: Nana, query: str) -> None:
    SearchTest.error_test(
        query,
        lambda: client.search.download(query),
        EmptySearchResultsError,
    )
