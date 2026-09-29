# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from nana.exceptions import ContentNotFoundError

if TYPE_CHECKING:
    from nana import Nana

CONTENT = [
    pytest.param(
        "1ca4ff63d6b65ca59b6607c4fd152f3c",
        "movie",
        "The Terminator",
        id="the terminator movie",
    ),
    pytest.param(
        "14de3bf28d7153ff8d938f554b76dcf5",
        "series",
        "Die Hart",
        id="die hart series",
    ),
    pytest.param(
        "14de3bf28d7153ff8d938f554b76dcf5-2",
        "season",
        "Season 2",
        id="die hart season 2",
    ),
    pytest.param(
        "2fa0eef93c07552da8c6f81988100b02",
        "episode",
        "Hart Broken",
        id="die hart episode",
    ),
    pytest.param(
        "e04fbb4fc17c5dcc8c96023ac42e31df",
        "movie",
        "Rocky",
        id="movie whose licensing window carries no timezone",
    ),
]


# TODO: Validate
@pytest.mark.parametrize(("content_id", "media_type", "title"), CONTENT)
def test_download(client: Nana, content_id: str, media_type: str, title: str) -> None:
    content = client.content(content_id)
    assert content.meta.media_type == media_type
    assert content.title == title


# TODO: Validate
def test_download_invalid(client: Nana) -> None:
    with pytest.raises(ContentNotFoundError):
        client.content.download("deadbeefdeadbeefdeadbeefdeadbeef")
