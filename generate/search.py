# TODO: Validate
"""Rebuilds SearchModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, NANA_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from nana import Nana

QUERIES = load_ids("SearchModel")


# TODO: Validate
def generate_search(client: Nana) -> None:
    """Rebuild SearchModel."""
    for query in QUERIES:
        download_if_missing(
            FILES_PATH,
            "SearchModel",
            query,
            lambda query=query: client.search.download(query),
        )
    rebuild_model(FILES_PATH, NANA_PATH, "SearchModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search(Nana(build_client_automatically()))
