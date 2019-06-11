import asyncio
import logging
from typing import Any

from starlette import status
from starlette.endpoints import WebSocket
from starlette.types import Message, Receive, Scope, Send

from .redis import redis

logger = logging.getLogger(__name__)


class BroadcastWs:
    encoding = "text"
    channel_name = "asgi_broadcast"

    def __init__(self, scope: Scope) -> None:
        assert scope["type"] == "websocket"
        self.scope = scope
        self.pub_sub = redis.pubsub()

    async def __call__(self, receive: Receive, send: Send) -> None:
        websocket = WebSocket(self.scope, receive=receive, send=send)
        await self.on_connect(websocket)

        await asyncio.gather(self.listen_channel(websocket), self.listen_client(websocket))

    async def listen_client(self, websocket: WebSocket) -> None:
        close_code = status.WS_1000_NORMAL_CLOSURE
        try:
            while True:
                message = await websocket.receive()
                logger.info(f"message: {message}")
                if message["type"] == "websocket.receive":
                    data = await self.decode(websocket, message)
                    await self.on_receive(websocket, data)
                elif message["type"] == "websocket.disconnect":
                    close_code = int(message.get("code", status.WS_1000_NORMAL_CLOSURE))
                    break
        except Exception as exc:
            close_code = status.WS_1011_INTERNAL_ERROR
            raise exc from None
        finally:
            await self.on_disconnect(websocket, close_code)

    async def listen_channel(self, websocket: WebSocket) -> None:
        while self.pub_sub.connection:
            msg = self.pub_sub.get_message()
            if msg is not None and msg["type"] == "message":
                logger.info(msg)
                await websocket.send_text(f"broadcasting: {msg['data'].decode()}")
            logger.info(f"listening for new {self.channel_name} redis msgs..")
            await asyncio.sleep(2)

    async def decode(self, websocket: WebSocket, message: Message) -> Any:
        if "text" not in message:
            await websocket.close(code=status.WS_1003_UNSUPPORTED_DATA)
            raise RuntimeError("Expected text websocket messages, but got bytes")
        return message["text"]

    async def on_connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        self.pub_sub.subscribe(self.channel_name)

    async def on_receive(self, websocket: WebSocket, data: Any) -> None:
        redis.publish(self.channel_name, data)

    async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
        self.pub_sub.close()
