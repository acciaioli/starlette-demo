from typing import List

from starlette.types import Scope, Receive, Send
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.websockets import WebSocket
from starlette.background import BackgroundTasks

from .tasks import do


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


async def tasks(request):
    data: List[str] = await request.json()
    b_tasks = BackgroundTasks()
    for key in data:
        b_tasks.add_task(do, param=key)

    return JSONResponse({'will do': f'{len(data)} tasks'}, background=b_tasks)
