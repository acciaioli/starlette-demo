from starlette.testclient import TestClient


def test_logs(client: TestClient) -> None:
    response = client.get("/log")
    assert response.status_code == 204
    assert response.headers["content-type"] == "application/json"
