from typing import List

from starlette.routing import Route

from .endpoints import homepage

routes: List[Route] = [
    Route('/', endpoint=homepage, methods=['GET']),
]
