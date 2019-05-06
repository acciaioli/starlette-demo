from typing import Generator

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Connection
from sqlalchemy_utils import create_database, database_exists, drop_database
from starlette.config import environ
from starlette.testclient import TestClient

environ["TESTING"] = "True"

from app.db import db_url, metadata  # noqa: E402 # isort:skip
from app import app  # noqa: E402 # isort:skip


@pytest.fixture(scope="session", autouse=True)
def setup_db() -> Generator[None, None, None]:
    engine = create_engine(db_url)
    assert not database_exists(db_url), "Test database already exists. Aborting tests."
    create_database(db_url)  # Create the test database.
    config = Config("alembic.ini")  # Run the migrations.
    command.upgrade(config, "head")
    metadata.create_all(engine)  # Create the tables.
    yield
    drop_database(db_url)  # Drop the test database.


@pytest.fixture()
def conn() -> Generator[Connection, None, None]:
    engine = create_engine(db_url)
    yield engine.connect()


@pytest.fixture()
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client
