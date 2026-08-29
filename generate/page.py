# TODO: Validate
"""Rebuilds PageModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, NANA_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from nana import Nana

PAGE_IDS = load_ids("PageModel")
"""The TV shows browse page."""


# TODO: Validate
def generate_page(client: Nana) -> None:
    """Rebuild PageModel."""
    for page_id in PAGE_IDS:
        download_if_missing(
            FILES_PATH,
            "PageModel",
            page_id,
            lambda page_id=page_id: client.page.download(page_id),
        )
    rebuild_model(FILES_PATH, NANA_PATH, "PageModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_page(Nana(build_client_automatically()))
