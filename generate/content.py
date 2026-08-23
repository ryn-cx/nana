# TODO: Validate
"""Rebuilds ContentModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, NANA_PATH
from generate.utils import download_if_missing
from nana import Nana

CONTENT_IDS = [
    "14de3bf28d7153ff8d938f554b76dcf5",
    "14de3bf28d7153ff8d938f554b76dcf5-2",
    "1ca4ff63d6b65ca59b6607c4fd152f3c",
    "2fa0eef93c07552da8c6f81988100b02",
]
"""A series, one of its seasons, one of its episodes and a movie."""


# TODO: Validate
def generate_content(client: Nana) -> None:
    """Rebuild ContentModel."""
    for content_id in CONTENT_IDS:
        download_if_missing(
            FILES_PATH,
            "ContentModel",
            content_id,
            lambda content_id=content_id: client.content.download(content_id),
        )
    generate_model(FILES_PATH, NANA_PATH, "ContentModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_content(Nana(build_client_automatically()))
