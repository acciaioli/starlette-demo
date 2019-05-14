import os

import databases
from starlette.config import Config

config = Config(os.environ.get("ENVFILE", ".env"))

# dev, test, prod
ENV: str = config("ENV", cast=str, default="prod")

STATIC_DIR: str = config("STATIC_DIR", cast=str, default="static")

DATABASE_URL = config("DATABASE_URL", cast=databases.DatabaseURL, default="sqlite:///app.db")
