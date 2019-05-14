from starlette.applications import Starlette
from starlette.middleware.authentication import AuthenticationMiddleware

from .auth import BasicAuthBackend, auth_error
from .config import ENV
from .db import shutdown_db, startup_db
from .exception_handlers import not_found
from .logging import configure_logging
from .routes import routes

app: Starlette = Starlette(debug=ENV == "dev", routes=routes)

app.exception_middleware.add_exception_handler(404, not_found)
app.add_middleware(AuthenticationMiddleware, backend=BasicAuthBackend(), on_error=auth_error)


@app.on_event("startup")
async def startup() -> None:
    await configure_logging(ENV)
    await startup_db()


@app.on_event("shutdown")
async def shutdown() -> None:
    await shutdown_db()
