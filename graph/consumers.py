import asyncio
import json
import random

from channels.generic.websocket import AsyncWebsocketConsumer


class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await super().connect()
        for _ in range(1000):
            await self.send(json.dumps({'value': random.randint(1, 20)}))
            await asyncio.sleep(0.5)
