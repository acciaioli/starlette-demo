import sqlalchemy
import databases

from .config import TESTING, DATABASE_URL, TEST_DATABASE_URL


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
