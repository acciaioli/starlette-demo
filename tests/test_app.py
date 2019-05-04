from starlette.testclient import TestClient

from app import app


def test_api():
    client = TestClient(app)
    response = client.get('/api')
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
    assert response.json() == {'hello': 'asgi'}


def test_ws():
    client = TestClient(app)
    with client.websocket_connect('/ws') as websocket:
        data = websocket.receive_json()
        assert data == {'hello': 'asgi'}
        data = websocket.receive_json()
        assert data == {'goodbye': 'asgi'}

