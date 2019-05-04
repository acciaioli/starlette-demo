from typing import List

from starlette.routing import Route, WebSocketRoute

from .endpoints import api, Ws

routes: List[Route] = [
    Route('/api', endpoint=api, methods=['GET']),
    WebSocketRoute('/ws', endpoint=Ws),
]
