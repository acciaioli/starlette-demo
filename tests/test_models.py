from sqlalchemy.sql import select
from sqlalchemy.engine.base import Connection

from app.models import protocols


def test_protocols(conn: Connection) -> None:
    s = select([protocols.c.name])
    rows = conn.execute(s)
    assert rows.fetchall() == []

    s = protocols.insert()
    conn.execute(s, [{"name": "wsgi"}, {"name": "asgi"}])

    s = select([protocols.c.name])
    rows = conn.execute(s)
    assert rows.fetchall() == [("wsgi",), ("asgi",)]

    s = protocols.update().where(protocols.c.name == "wsgi").values(name="past")
    conn.execute(s)

    s = select([protocols.c.name])
    rows = conn.execute(s)
    assert rows.fetchall() == [("past",), ("asgi",)]

    s = protocols.delete()
    conn.execute(s)

    s = select([protocols.c.name])
    rows = conn.execute(s)
    assert rows.fetchall() == []
