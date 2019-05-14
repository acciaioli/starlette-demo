import databases
import sqlalchemy

from .config import DATABASE_URL, ENV

metadata = sqlalchemy.MetaData()
force_rollback = False

if ENV == "test":
    DATABASE_URL = DATABASE_URL.replace(database="test_" + DATABASE_URL.database)
    force_rollback = True

db_url = str(DATABASE_URL)
database = databases.Database(db_url, force_rollback=force_rollback)


async def startup_db() -> None:
    await database.connect()


async def shutdown_db() -> None:
    await database.disconnect()
