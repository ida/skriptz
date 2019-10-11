const https = require('https')


function request(url, doWithResponseData, dataToPost) {
/*

Example GET-request:
  let url = 'https://example.org'
  let doWithResponseData = data => console.log(data)
  request(url, doWithResponseData)

Example POST-request:
  let url = 'https://admin:password@example.org'
  let doWithResponseData = data => console.log(data)
  let dataToPost = '{ "some": "data", "to": "post" }'
  request(url, doWithResponseData, dataToPost)

*/

  // Prepare options for request:

  url = new URL(url)

  const options = {
    hostname: url.hostname,
    port: url.port,
    path: url.path,
    method: 'GET',
    headers: {
      'Content-Type': 'application/json', // send data as json
      'Accept': 'application/json' // allow receiving json-data
    },
    auth: url.username + ':' + url.password
  }

  if(dataToPost) options.method = 'POST'


  // Send request:
  const req = https.request(options, res => {
    // Response is sended in pieces of data, collect them:
    let data = ''; res.on('data', datum => data += datum.toString())
    // Response has finished, execute passed handler on collected data:
    res.on('end', () => doWithResponseData(data))
	})
  // Send data, if passed:
  if(dataToPost) req.write(dataToPost)
  // A request needs to be explicitly shut down:
  req.end()
}
