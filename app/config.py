from starlette.config import Config

config = Config('.env')

DEBUG: bool = config('DEBUG', cast=bool, default=False)

STATIC_DIR: str = config('STATIC_DIR', cast=str, default='static')

