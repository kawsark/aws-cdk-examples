# https://websockets.readthedocs.io/en/stable/
#!/usr/bin/env python

"""Echo server using the asyncio API."""

import asyncio
from websockets.asyncio.server import serve
from aiohttp import web


# Health Check Handler
async def health_check(request):
    return web.Response(text="OK")

# Websocket handler
async def echo(websocket):
    async for message in websocket:
        # Print the received message
        print(f"Received message: {message}")

        # Print metadata (e.g., client address)
        print(f"Client address: {websocket.remote_address}")
        print(f"Request ID: {websocket.id}")
        print(f"Client state: {websocket.state}")
        print(f"Client latency: {websocket.latency}")

	    # Echo the message back
        await websocket.send(message)


async def main():

    # Create HTTP server for /healthz
    app = web.Application()
    app.router.add_get("/healthz", health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
    print('HTTP server started ("/healthz")...')

    # Create WebSocket server
    websocket_server = await serve(echo, "0.0.0.0", 8765)
    print("WebSocket server started...")

    # Keep the servers running
    try:
        # This will run forever until interrupted
        await asyncio.Future()  # keep the server running
    finally:
        websocket_server.close()
        await websocket_server.wait_closed()
        await runner.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
