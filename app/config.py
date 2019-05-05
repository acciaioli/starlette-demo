from starlette.config import Config
import databases


config = Config('.env')

DEBUG: bool = config('DEBUG', cast=bool, default=False)
TESTING = config('TESTING', cast=bool, default=False)

STATIC_DIR: str = config('STATIC_DIR', cast=str, default='static')

DATABASE_URL = config('DATABASE_URL', cast=databases.DatabaseURL, default='sqlite:///app.db')
TEST_DATABASE_URL = DATABASE_URL.replace(database='test_' + DATABASE_URL.database)
