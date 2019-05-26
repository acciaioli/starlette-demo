import asyncio
import logging
from typing import Any

import redis
from starlette.endpoints import WebSocket, WebSocketEndpoint

logger = logging.getLogger(__name__)

redis_con_pool = redis.Redis(host="localhost", port=6379)


class BroadcastWs(WebSocketEndpoint):
    encoding = "text"
    channel_name = "asgi_broadcast"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.pub_sub = redis_con_pool.pubsub()
        super().__init__(*args, **kwargs)

    async def listen_channel(self, websocket: WebSocket) -> None:
        self.pub_sub.subscribe(self.channel_name)
        while self.pub_sub.connection:
            msg = self.pub_sub.get_message()
            if msg is not None and msg["type"] == "message":
                logger.info(msg)
                await websocket.send_text(f"broadcasting: {msg['data'].decode()}")
            await asyncio.sleep(1)
            logger.info(f"listening for new {self.channel_name} msgs..")
            await asyncio.sleep(1)

    async def on_connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        loop = asyncio.get_event_loop()
        loop.create_task(self.listen_channel(websocket))

    async def on_receive(self, websocket: WebSocket, data: Any) -> None:
        redis_con_pool.publish(self.channel_name, data)

    async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
        self.pub_sub.close()
