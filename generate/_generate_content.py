from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import GAPICustomizer, generate_model
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    drop_redundant_recordings,
    load_ids,
)

from generate.constants import GENERATOR_PATHS
from nana import Nana

MODEL_NAME = "ContentModel"


# TODO: Validate
class ContentId(RecordingId[Nana]):
    content_id: str

    # TODO: Validate
    def download(self, client: Nana) -> str:
        return client.content.download(self.content_id)


CONTENT_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, ContentId)


# TODO: Validate
def generate_content(client: Nana) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, CONTENT_IDS, client)

    customizer = GAPICustomizer()
    for class_name in ("Media", "BottomLeftItem", "BottomLeftItem1"):
        for field_name in ("validity_start_time", "validity_end_time"):
            customizer.add_replacement_type(class_name, field_name, "datetime")
    customizer.add_additional_import("from datetime import datetime")

    generate_model(
        GENERATOR_PATHS.files_path,
        GENERATOR_PATHS.package_path,
        MODEL_NAME,
        customizer=customizer,
    )
    drop_redundant_recordings(GENERATOR_PATHS, MODEL_NAME, ContentId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_content(Nana(build_client_automatically()))
