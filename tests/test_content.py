# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from nana.exceptions import ContentNotFoundError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from nana import Nana
    from nana.content import Content

SERIES_ID = "618dd78c1a275ef989b06ebd492aa136"
SEASON_ID = "618dd78c1a275ef989b06ebd492aa136-6"
EPISODE_ID = "bd5ec0f3917856c78fde2eea3de21dac"
MOVIE_ID = "1ca4ff63d6b65ca59b6607c4fd152f3c"
INVALID_ID = "deadbeefdeadbeefdeadbeefdeadbeef"

CONTENT_IDS = [SERIES_ID, SEASON_ID, EPISODE_ID, MOVIE_ID]

TYPES = {
    SERIES_ID: "series",
    SEASON_ID: "season",
    EPISODE_ID: "episode",
    MOVIE_ID: "movie",
}


@pytest.fixture(scope="session")
def client(client: Nana) -> Content:
    return client.content


@pytest.mark.parametrize("content_id", CONTENT_IDS)
def test_download(client: Content, content_id: str) -> None:
    download_and_save(client, content_id, lambda: client.download(content_id))


@pytest.mark.parametrize("content_id", CONTENT_IDS)
def test_parse(client: Content, content_id: str) -> None:
    data = parsed_json(client, content_id)
    assert data.type == TYPES[content_id]


def test_download_invalid(client: Content) -> None:
    assert_error(
        client,
        INVALID_ID,
        lambda: client.download(INVALID_ID),
        ContentNotFoundError,
    )
