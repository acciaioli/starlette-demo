from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.websockets import WebSocket
from starlette.types import Scope, Receive, Send


async def api(request: Request) -> JSONResponse:
    return JSONResponse({'hello': 'asgi'})


class Ws:
    def __init__(self, scope: Scope) -> None:
        assert scope['type'] == 'websocket'
        self.scope = scope

    async def __call__(self, receive: Receive, send: Send) -> None:
        websocket = WebSocket(self.scope, receive=receive, send=send)
        await websocket.accept()
        await websocket.send_json({'hello': 'asgi'})
        await websocket.send_json({'goodbye': 'asgi'})
        await websocket.close()
