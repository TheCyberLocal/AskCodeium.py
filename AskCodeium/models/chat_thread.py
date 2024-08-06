import websockets
from AskCodeium.utils.port_manager import PortManager

class createChat:
    def __init__(self):
        self.port_manager = PortManager()
        self.port = self.port_manager.get_free_port()
        self.base_url = "https://codeium.com/live/general"
        self.websocket = None

    async def connect(self):
        try:
            self.websocket = await websockets.connect(f"ws://localhost:{self.port}")
        except Exception as e:
            print(f"Failed to connect to WebSocket: {e}")

    async def send_message(self, message):
        if self.websocket is None:
            await self.connect()
        try:
            await self.websocket.send(message)
            response = await self.websocket.recv()
            return response
        except Exception as e:
            print(f"Error during message exchange: {e}")
            return None

    async def __call__(self, message):
        return await self.send_message(message)

    # def clear_history(self):
    #     # Simulate clearing history by sending a request to the page
    #     response = requests.post(f"{self.base_url}/clearHistory")
    #     if response.status_code == 200:
    #         print("History cleared successfully")
    #     else:
    #         print("Failed to clear history")
