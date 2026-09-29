# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from nana.exceptions import EmptySearchResultsError
from nana.search import Search

if TYPE_CHECKING:
    from nana import Nana

QUERIES = [
    pytest.param(
        "walker texas ranger",
        "Walker, Texas Ranger",
        id="walker texas ranger series",
    ),
    pytest.param("blade runner 2049", "Blade Runner 2049", id="blade runner movie"),
]


# TODO: Validate
@pytest.mark.parametrize(("query", "title"), QUERIES)
def test_download(client: Nana, query: str, title: str) -> None:
    matches = Search.extract_content(client.search(query))
    assert title in [match.title for match in matches]


# TODO: Validate
def test_download_invalid(client: Nana) -> None:
    with pytest.raises(EmptySearchResultsError):
        client.search.download("zzzzqqqqxxxxnotathing")
