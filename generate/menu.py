# TODO: Validate
"""Rebuilds MenuModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, NANA_PATH
from generate.utils import download_if_missing, rebuild_model
from nana import Nana

MENU_NAME = "menu"
"""What the menu is recorded under. There is only one menu per storefront."""


# TODO: Validate
def generate_menu(client: Nana) -> None:
    """Rebuild MenuModel."""
    download_if_missing(FILES_PATH, "MenuModel", MENU_NAME, client.menu.download)
    rebuild_model(FILES_PATH, NANA_PATH, "MenuModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_menu(Nana(build_client_automatically()))
