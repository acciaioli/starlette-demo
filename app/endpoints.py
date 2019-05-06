import typing

from starlette.background import BackgroundTasks
from starlette.endpoints import WebSocketEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, RedirectResponse
from starlette.types import Receive, Scope, Send
from starlette.websockets import WebSocket

from .db import database
from .models import protocols
from .tasks import do


async def root(request: Request) -> RedirectResponse:
    return RedirectResponse(url="/api")


async def api(request: Request) -> JSONResponse:
    return JSONResponse({"hello": "asgi"})


class Ws:
    def __init__(self, scope: Scope) -> None:
        assert scope["type"] == "websocket"
        self.scope = scope

    async def __call__(self, receive: Receive, send: Send) -> None:
        websocket = WebSocket(self.scope, receive=receive, send=send)
        await websocket.accept()
        await websocket.send_json({"hello": "asgi"})
        await websocket.send_json({"goodbye": "asgi"})
        await websocket.close()


class EchoWs(WebSocketEndpoint):
    encoding = "text"

    async def on_receive(self, websocket: WebSocket, data: typing.Any) -> None:
        await websocket.send_text(f"echo: {data}")


async def tasks(request: Request) -> JSONResponse:
    data: typing.List[str] = await request.json()
    b_tasks = BackgroundTasks()
    for key in data:
        b_tasks.add_task(do, param=key)

    return JSONResponse({"will do": f"{len(data)} tasks"}, background=b_tasks)


async def list_protocols(request: Request) -> JSONResponse:
    query = protocols.select()
    results = await database.fetch_all(query)
    content = [{"id": result["id"], "name": result["name"]} for result in results]

    return JSONResponse(content)


async def create_protocol(request: Request) -> JSONResponse:
    data = await request.json()
    query = protocols.insert().values(name=data["name"])
    await database.execute(query)

    return JSONResponse({"name": data["name"]})


async def favicon(request: Request) -> RedirectResponse:
    return RedirectResponse("/static/favicon.ico")
