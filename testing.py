import asyncio
from AskCodeium.utils.websocket_client import WebSocketClient

async def test_websocket_client():
    try:
        uri = "ws://echo.websocket.events/"  # This is a public WebSocket echo server for testing
        ws_client = WebSocketClient(uri)

        # Test sending a message and receiving a response
        message = "Hello, WebSocket!"
        response = await ws_client.send_message(message)
        print(f"Sent: {message}")
        print(f"Received: {response}")

        # Close the connection
        await ws_client.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_websocket_client())
