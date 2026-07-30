import pytest
from get_around import build_client_automatically

from nana import Nana


@pytest.fixture(scope="session")
def client() -> Nana:
    return Nana(build_client_automatically())
