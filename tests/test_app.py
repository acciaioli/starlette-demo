from starlette.testclient import TestClient

from app import app


def test_app():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
    assert response.json() == {'hello': 'asgi'}
