import pytest
from starlette.testclient import TestClient
from api.main import app

@pytest.fixture
def app_client():
    with TestClient(app) as test_client:
        yield test_client