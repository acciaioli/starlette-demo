from starlette.routing import Route

from .endpoints import homepage

routes = [
    Route('/', endpoint=homepage, methods=['GET']),
]
