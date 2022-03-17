# simple-websocket-py-js-connection
Simple example of a websocket connection between Python (server) and Javascript (client). The content served by Python is stored in files, so it can be easily modified by external means (like the data generator program included).

## How to launch the server
1. Make the file src/server/server.py executable.
2. Launch it with the command `./server.py`
3. The server is running, and waiting for client requests.

## How to launch the client
1. Open the file src/client/main.html with an Internet browser.
2. You should be able to see the responses from the server (current variable values).

## Update variable values randomly
There are three example variables stored in the files:
- src/server/data/exampleA
- src/server/data/exampleB
- src/server/data/exampleC

You can update their values randomly using the executable src/server/datagenerator.py.

## Websockets syntax
Client requests to stablish a websocket connection use the following syntax:
```
ws://<server_url>:<server_port>/<variable_name>?updatespersecond=<number>
```
