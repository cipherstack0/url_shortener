import pytest
from functions import start_db


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    start_db()