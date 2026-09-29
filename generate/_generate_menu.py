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

MODEL_NAME = "MenuModel"


# TODO: Validate
class MenuId(RecordingId[Nana]):
    menu_name: str

    # TODO: Validate
    def download(self, client: Nana) -> str:
        return client.menu.download()


MENU_NAMES = load_ids(GENERATOR_PATHS, MODEL_NAME, MenuId)


# TODO: Validate
def generate_menu(client: Nana) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, MENU_NAMES, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, MenuId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_menu(Nana(build_client_automatically()))
