from typing import List

from starlette.routing import Mount, Route, WebSocketRoute

from .endpoints import Ws, api, create_protocol, list_protocols, root, tasks
from .static import static

routes: List[Route] = [
    Route("/", endpoint=root, methods=["GET"], name="root"),
    Route("/api", endpoint=api, methods=["GET"], name="api"),
    Route("/tasks", endpoint=tasks, methods=["POST"], name="tasks"),
    WebSocketRoute("/ws", endpoint=Ws, name="websocket"),
    Mount("/static", static, name="static"),
    Route("/protocols", endpoint=list_protocols, methods=["GET"], name="list_protocols"),
    Route("/protocols", endpoint=create_protocol, methods=["POST"], name="create_protocol"),
]
