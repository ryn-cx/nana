# TODO: Validate
"""Rebuilds PageModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, NANA_PATH
from generate.utils import download_if_missing
from nana import Nana

PAGE_IDS = [
    "w.K1mlzamaPvhLKYkBrNw5f9zoDy7WkWFk601b6NR7U2WrBwNgpPIqB4LoJY26T9jaW15eM",
]
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
    generate_model(FILES_PATH, NANA_PATH, "PageModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_page(Nana(build_client_automatically()))
