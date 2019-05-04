from starlette.applications import Starlette

from .config import DEBUG
from .routes import routes
from .exception_handlers import not_found


app: Starlette = Starlette(debug=DEBUG, routes=routes)

app.exception_middleware.add_exception_handler(404, not_found)
