import databases
import sqlalchemy

from .config import DATABASE_URL, TEST_DATABASE_URL, TESTING

metadata = sqlalchemy.MetaData()

if TESTING:
    db_url = str(TEST_DATABASE_URL)
    database = databases.Database(TEST_DATABASE_URL, force_rollback=True)
else:
    db_url = str(DATABASE_URL)  # pragma: no cover
    database = databases.Database(DATABASE_URL)  # pragma: no cover


async def startup_db() -> None:
    await database.connect()


async def shutdown_db() -> None:
    await database.disconnect()
