# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from nana.exceptions import PageNotFoundError
from nana.page import Page

if TYPE_CHECKING:
    from nana import Nana

PAGES = [
    pytest.param(
        "w.K1mlzamaPvhLKYkBrNw5f9zoDy7WkWFk601b6NR7U2WrBwNgpPIqB4LoJY26T9jaW15eM",
        "trc-us-free-eligible-tv-series-en-current",
        "TV Shows",
        id="tv shows browse page",
    ),
]

NOT_PAGE_IDS = [
    pytest.param("w.notarealpageid", id="page that does not exist"),
    pytest.param("!!!", id="page id that is not a page id"),
]


# TODO: Validate
@pytest.mark.parametrize(("page_id", "filed_id", "title"), PAGES)
def test_download(client: Nana, page_id: str, filed_id: str, title: str) -> None:
    # A page is asked for by the opaque id the menu publishes and answers with
    # the readable one it is filed under.
    page = client.page(page_id)
    assert page.meta.id == filed_id
    assert page.title == title
    assert all(content.meta.id for content in Page.extract_content(page))


# TODO: Validate
@pytest.mark.parametrize("page_id", NOT_PAGE_IDS)
def test_download_invalid(client: Nana, page_id: str) -> None:
    with pytest.raises(PageNotFoundError):
        client.page.download(page_id)
