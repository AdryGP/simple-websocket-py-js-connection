#!/usr/bin/env python

import asyncio
import websockets
import time

# Función de respuesta a peticiones al servidor websocket
# Resource es el contenido de la URL tras la dirección del servidor
async def echo(websocket, resource):
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
    async with websockets.serve(echo, host="localhost", port=8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
