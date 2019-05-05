from starlette.applications import Starlette

from .config import DEBUG
from .routes import routes
from .exception_handlers import not_found
from .db import startup_db, shutdown_db

app: Starlette = Starlette(debug=DEBUG, routes=routes)

app.exception_middleware.add_exception_handler(404, not_found)


@app.on_event("startup")
async def startup() -> None:
    await startup_db()


@app.on_event("shutdown")
async def shutdown() -> None:
    await shutdown_db()
