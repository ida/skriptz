const http = require('http')


http.createServer((request, response) => {

  response.writeHead(200, { 'Content-Type': 'text/html; charset="utf-8"' })

  response.end('<body>Hello universe!</body>')


}).listen(3000, error => console.log('Serving http://localhost:3000'))
