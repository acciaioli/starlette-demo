from app.config import ENV


def test_env() -> None:
    assert ENV == "test"
