from starlette.staticfiles import StaticFiles

from .config import STATIC_DIR

static: StaticFiles = StaticFiles(directory=STATIC_DIR)
