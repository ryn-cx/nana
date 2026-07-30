# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from nana.exceptions import PageNotFoundError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from nana import Nana
    from nana.page import Page

# Page ids are published by the menu endpoint, this one is "TV Shows".
PAGE_ID = "w.K1mlzamaPvhLKYkBrNw5f9zoDy7WkWFk601b6NR7U2WrBwNgpPIqB4LoJY26T9jaW15eM"
INVALID_PAGE_ID = "w.notarealpageid"


@pytest.fixture(scope="session")
def client(client: Nana) -> Page:
    return client.page


def test_download(client: Page) -> None:
    download_and_save(client, PAGE_ID, lambda: client.download(PAGE_ID))


def test_parse(client: Page) -> None:
    data = parsed_json(client, PAGE_ID)
    assert data.collections


def test_extract_content(client: Page) -> None:
    content = client.extract_content(parsed_json(client, PAGE_ID))
    assert content
    assert all(item.meta.id for item in content)


def test_download_invalid(client: Page) -> None:
    assert_error(
        client,
        INVALID_PAGE_ID,
        lambda: client.download(INVALID_PAGE_ID),
        PageNotFoundError,
    )
