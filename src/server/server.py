#!/usr/bin/env python

# server.py: Main server process. Opens a websocket 
# server on port 8765. Serves the value of the variables
# stored under the data folder repeatedly, as fast as the 
# client wants.
# Websocket URL format: 
# ws://localhost:8765/<variable_name>?updatespersecond=<number>

import asyncio
import websockets

async def echo_var_value(websocket, resource):
    global connections

    variable = resource.split('?')[0]
    rate = int(resource.split('=')[1])

    print(f"Serving {variable} variable")

    while True:
        with open(f"data/{variable}", 'r') as reader:
            reading = reader.read()
            if reading != '':
                 await websocket.send(reading)
        await asyncio.sleep(1/rate)


async def main():
    async with websockets.serve(echo_var_value, host="localhost", port=8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
