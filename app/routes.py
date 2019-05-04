from typing import List

from starlette.routing import Route, WebSocketRoute, Mount

from .endpoints import api, Ws, tasks
from .static import static


routes: List[Route] = [
    Route('/api', endpoint=api, methods=['GET'], name='api'),
    Route('/tasks', endpoint=tasks, methods=['POST'], name='tasks'),
    WebSocketRoute('/ws', endpoint=Ws, name='websocket'),
    Mount('/static', static, name='static'),
]
