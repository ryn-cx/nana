# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from nana.exceptions import PageNotFoundError
from nana.page import Page
from nana.page.models import PageModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from nana import Nana

PAGE_IDS = [
    pytest.param(
        "w.K1mlzamaPvhLKYkBrNw5f9zoDy7WkWFk601b6NR7U2WrBwNgpPIqB4LoJY26T9jaW15eM",
        id="tv shows browse page",
    ),
]


# TODO: Validate
class PageTest(RecordedEndpoint):
    MODEL = PageModel
    # Every row is recommendations, so what is in a row comes back different
    # each time the page is fetched.
    IGNORED = (
        "PageModel.trace_id",
        "Collection.view",
        "TrackerOverrides.item_server_data",
        "TrackerOverrides1.item_server_data",
    )


# TODO: Validate
@pytest.mark.parametrize("page_id", PAGE_IDS)
def test_download(client: Nana, page_id: str) -> None:
    PageTest.download_test(page_id, lambda: client.page.download(page_id))


# TODO: Validate
@pytest.mark.parametrize("page_id", PAGE_IDS)
def test_parse(client: Nana, page_id: str) -> None:
    # A page is asked for by the opaque id the menu publishes and answers with
    # the readable one it is filed under.
    page = client.page.load(PageTest.recorded_content(page_id))
    assert page.meta.id == "trc-us-free-eligible-tv-series-en-current"
    assert page.title == "TV Shows"


# TODO: Validate
@pytest.mark.parametrize("page_id", PAGE_IDS)
def test_extract_content(client: Nana, page_id: str) -> None:
    titles = Page.extract_content(client.page.load(PageTest.recorded_content(page_id)))
    assert titles
    assert all(title.meta.id for title in titles)


# TODO: Validate
@pytest.mark.parametrize(
    "page_id",
    [
        pytest.param("w.notarealpageid", id="page that does not exist"),
        pytest.param("!!!", id="page id that is not a page id"),
    ],
)
def test_download_invalid(client: Nana, page_id: str) -> None:
    PageTest.error_test(
        page_id,
        lambda: client.page.download(page_id),
        PageNotFoundError,
    )
