# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from nana import Nana
    from nana.menu import Menu

NAME = "menu"


@pytest.fixture(scope="session")
def client(client: Nana) -> Menu:
    return client.menu


def test_download(client: Menu) -> None:
    download_and_save(client, NAME, client.download)


def test_parse(client: Menu) -> None:
    data = parsed_json(client, NAME)
    assert data.view


def test_extract_pages(client: Menu) -> None:
    pages = client.extract_pages(parsed_json(client, NAME))
    assert pages
    assert all(page.meta.id for page in pages)
