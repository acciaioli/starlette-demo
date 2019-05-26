from typing import List

from starlette.routing import Mount, Route, WebSocketRoute

from .broadcast import BroadcastWs
from .endpoints import EchoWs, Ws, api, create_protocol, favicon, list_protocols, log, protected, root, tasks
from .static import static

routes: List[Route] = [
    Route("/", endpoint=root, methods=["GET"], name="root"),
    Route("/api", endpoint=api, methods=["GET"], name="api"),
    Route("/tasks", endpoint=tasks, methods=["POST"], name="tasks"),
    WebSocketRoute("/ws", endpoint=Ws, name="websocket"),
    WebSocketRoute("/echo", endpoint=EchoWs, name="websocket"),
    Mount("/static", static, name="static"),
    Route("/favicon.ico", favicon, name="favicon"),
    Route("/protocols", endpoint=list_protocols, methods=["GET"], name="list_protocols"),
    Route("/protocols", endpoint=create_protocol, methods=["POST"], name="create_protocol"),
    Route("/log", endpoint=log, methods=["GET"], name="log"),
    Route("/protected", endpoint=protected, methods=["GET"], name="protected"),
    WebSocketRoute("/broadcast", endpoint=BroadcastWs, name="broadcast"),
]
