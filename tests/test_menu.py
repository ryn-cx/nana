# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from nana.menu import Menu

if TYPE_CHECKING:
    from nana import Nana

STOREFRONT_ID = "trc_web_us"
"""The storefront the menu is served for."""


# TODO: Validate
def test_download(client: Nana) -> None:
    menu = client.menu()
    assert menu.meta.id == STOREFRONT_ID
    pages = Menu.extract_pages(menu)
    assert pages
    assert all(entry.meta.type == "page" for entry in pages)
