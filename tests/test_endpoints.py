# Flake8: noqa: F811
from unittest.mock import MagicMock, call, patch

from requests.models import Response
from starlette.testclient import TestClient


def assert_redirected(response: Response) -> None:
    assert len(response.history) == 1
    assert response.history[0].status_code == 302


def test_root(client: TestClient) -> None:
    response = client.get("/")
    assert_redirected(response)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"hello": "asgi"}


def test_api(client: TestClient) -> None:
    response = client.get("/api")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"hello": "asgi"}


def test_ws(client: TestClient) -> None:
    with client.websocket_connect("/ws") as websocket:
        data = websocket.receive_json()
        assert data == {"hello": "asgi"}
        data = websocket.receive_json()
        assert data == {"goodbye": "asgi"}


def test_echo(client: TestClient) -> None:
    with client.websocket_connect("/echo") as websocket:
        websocket.send_text("goodbye")
        data = websocket.receive_text()
        assert data == "echo: goodbye"
        websocket.send_text("wsgi")
        data = websocket.receive_text()
        assert data == "echo: wsgi"


def test_404_handler(client: TestClient) -> None:
    response = client.get("/not_found")
    assert response.status_code == 404
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"detail": "not found"}


def test_static(client: TestClient) -> None:
    response = client.get("/static/asgi.html")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert response.content == b"<div>hello html</div>\n"


def test_favicon(client: TestClient) -> None:
    response = client.get("/favicon.ico")
    assert_redirected(response)
    assert response.status_code == 200
    assert "image/vnd.microsoft.icon" in response.headers["content-type"]


@patch("app.endpoints.do")
def test_tasks(do: MagicMock, client: TestClient) -> None:
    keys = ["a", "b", "c"]
    response = client.post("/tasks", json=keys)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"will do": "3 tasks"}

    expected_calls = [call(param="a"), call(param="b"), call(param="c")]
    do.assert_has_calls(expected_calls, any_order=True)


def test_list_protocols(client: TestClient) -> None:
    response = client.get("/protocols")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == []


def test_create_protocols(client: TestClient) -> None:
    response = client.post("/protocols", json={"name": "wsgi"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"name": "wsgi", "is_cool": False}


def test_protocols(client: TestClient) -> None:
    client.post("/protocols", json={"name": "asgi", "is_cool": True})
    client.post("/protocols", json={"name": "wsgi", "is_cool": False})
    response = client.get("/protocols")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == [{"id": 1, "name": "asgi", "is_cool": True}, {"id": 2, "name": "wsgi", "is_cool": False}]
