from typing import Any, Dict

from requests.auth import HTTPBasicAuth
from requests.models import Response
from starlette.testclient import TestClient


def assert_json_response(response: Response, status_code: int, msg: Dict[str, Any]) -> None:
    assert response.status_code == status_code
    assert response.headers["content-type"] == "application/json"
    assert response.json() == msg


def test_protected_401(client: TestClient) -> None:
    response_no_auth = client.get("/protected")

    auth = HTTPBasicAuth(username="user", password="notmypassword")
    response_bad_auth = client.get("/protected", auth=auth)

    headers = {"Authorization": "Token ABCDEFGI123"}
    response_token_auth = client.get("/protected", headers=headers)

    for response in [response_no_auth, response_bad_auth, response_token_auth]:
        assert_json_response(response, 401, {"detail": "unauthorized"})


def test_protected_400(client: TestClient) -> None:
    headers = {"Authorization": "qwerty"}
    response = client.get("/protected", headers=headers)

    assert_json_response(response, 400, {"detail": "auth error"})


def test_portected_200(client: TestClient) -> None:
    auth = HTTPBasicAuth(username="myfriend", password="asgi>wsgi")

    response = client.get(f"/protected", auth=auth)

    assert_json_response(response, 200, {"hello": "myfriend"})
