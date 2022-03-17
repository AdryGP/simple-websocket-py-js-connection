// We open one websocket per variable.
var exampleASocket = new WebSocket("ws://localhost:8765/exampleA?updatespersecond=10");
var exampleBSocket = new WebSocket("ws://localhost:8765/exampleB?updatespersecond=1");
var exampleCSocket = new WebSocket("ws://localhost:8765/exampleC?updatespersecond=5");

// And we update the html view when a new message is received from the server.
exampleASocket.onmessage = function (event) {
    document.getElementById("exampleA").textContent = event.data;
}

exampleBSocket.onmessage = function (event) {
    document.getElementById("exampleB").textContent = event.data;
}

exampleCSocket.onmessage = function (event) {
    document.getElementById("exampleC").textContent = event.data;
}