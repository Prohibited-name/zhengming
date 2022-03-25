#!/usr/bin/env python

import asyncio
import json
import secrets

import websockets


class Host(object):
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 3002

    async def error(self, websocket, message):
        event = {
            "type": "error",
            "message": message,
        }
        await websocket.send(json.dumps(event))

    async def handler(self, websocket, path):
        # Receive and parse the "init" event from the UI.
        message = await websocket.recv()
        event = json.loads(message)
        assert event["type"] == "init"

        if "join" in event:
            # Second player joins an existing game.
            pass
        elif "watch" in event:
            # Spectator watches an existing game.
            pass
        else:
            # First player starts a new game.
            pass

    async def main(self):
        async with websockets.serve(self.handler, self.ip, 3002):
            await asyncio.Future()  # run forever

    def run(self):
        asyncio.run(self.main())

