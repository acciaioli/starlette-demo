from starlette.applications import Starlette

from .config import DEBUG
from .routes import routes

app: Starlette = Starlette(debug=DEBUG, routes=routes)

