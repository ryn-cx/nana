from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from nana import Nana

MODEL_NAME = "PageModel"


# TODO: Validate
class PageId(RecordingId[Nana]):
    page_id: str

    # TODO: Validate
    def download(self, client: Nana) -> str:
        return client.page.download(self.page_id)


PAGE_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, PageId)


# TODO: Validate
def generate_page(client: Nana) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, PAGE_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, PageId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_page(Nana(build_client_automatically()))
