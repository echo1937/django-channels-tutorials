import json
from asyncio import sleep
from random import randint

from channels.generic.websocket import AsyncWebsocketConsumer


class WSConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await super().connect()
        for _ in range(1000):
            await self.send(json.dumps({'message': randint(1, 100)}))
            await sleep(1)
