// Most basal server-side-event example.

let clientId = 0
let clients = {}

function sendToClient(client, data) {
	client.write('id: ' + (new Date()).toLocaleTimeString() + '\n')
	client.write('data: ' + data + '\n\n')
}

function sendToClients(data) {
	for(clientId in clients) {
		sendToClient(clients[clientId], data)
	}
}

function collectClient(req, res) {

  (function (clientId) {
    clients[clientId] = res       // collect new client
    req.on('close', function () { // client disconnected
      delete clients[clientId]    // remove client
    })
  })(++clientId)

  sendToClient(res, 'Welcome client, you are connected!')

  sendToClients('We got a new member joining!')

}


let html = `

<body>

  <script>

	var stream = new EventSource('/serverstream')

	stream.onmessage = msgEvent => {

		console.log('Got a message from server:', msgEvent.data)

	}

  </script>

</body>`


require('http').createServer((request, response) => {

  if(request.url == '/serverstream') {
			
    response.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive'
    });

		collectClient(request, response)

  }

  else {
    
    response.writeHead(200, {
      'Content-Type': 'text/html; charset="utf-8"',
      'Content-Length': html.length
    });

    response.end(html)

  }

}).listen(3000, e => console.log('Serving http://localhost:3000'))
