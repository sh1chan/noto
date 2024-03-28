import asyncio
import websockets


async def echo(websockets):
  async for message in websockets:
    print('Sending: ', message)
    await websockets.send(message)


async def main():
  async with websockets.serve(echo, "127.0.0.1", 12345):
    await asyncio.Future()


asyncio.run(main())
