from app.core.config import settings
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

url = f"{settings.API_V1_STR}/health"


def test_health_endpoint_returns_200():
    response = client.get(url)

    assert response.status_code == 200
    assert response.json() == {"status": "running"}


def test_health_endpoint_method_not_allowed():
    response = client.post(url)

    assert response.status_code == 405
    assert "detail" in response.json()


def test_health_endpoint_invalid_path():
    response = client.get(f"{url}/123")

    assert response.status_code == 404
    assert "detail" in response.json()
