import websockets

class WebSocketClient:
    def __init__(self, uri):
        self.uri = uri
        self.connection = None

    async def connect(self):
        self.connection = await websockets.connect(self.uri)
        print(f"Connected to {self.uri}")

    async def send_message(self, message):
        if self.connection is None:
            await self.connect()
        await self.connection.send(message)
        response = await self.connection.recv()
        return response

    async def close(self):
        if self.connection is not None:
            await self.connection.close()
            print(f"Connection to {self.uri} closed")
