# TODO: Validate
import pytest
from get_around import build_client_automatically

from nana import Nana


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> Nana:
    return Nana(build_client_automatically())
