# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from nana.menu import Menu
from nana.menu.models import MenuModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from nana import Nana

MENU_NAMES = [
    pytest.param("menu", id="the us storefront menu"),
]


# TODO: Validate
class MenuTest(RecordedEndpoint):
    MODEL = MenuModel
    IGNORED = (
        "MenuModel.trace_id",
        "TrackerOverrides.item_server_data",
        "ViewItem.field_uuid",
    )


# TODO: Validate
@pytest.mark.parametrize("name", MENU_NAMES)
def test_download(client: Nana, name: str) -> None:
    MenuTest.download_test(name, client.menu.download)


# TODO: Validate
@pytest.mark.parametrize("name", MENU_NAMES)
def test_parse(client: Nana, name: str) -> None:
    menu = client.menu.load(MenuTest.recorded_content(name))
    assert menu.meta.id == "trc_web_us"


# TODO: Validate
@pytest.mark.parametrize("name", MENU_NAMES)
def test_extract_pages(client: Nana, name: str) -> None:
    pages = Menu.extract_pages(client.menu.load(MenuTest.recorded_content(name)))
    assert pages
    assert all(entry.meta.type == "page" for entry in pages)
