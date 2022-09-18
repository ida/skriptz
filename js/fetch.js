async function get(url, opts={}) {

  return await fetch(url, opts).then(res => {

    let cType = res.headers.get('content-type')

    if(cType.startsWith('application/json')) {

      return res.json()

    } else if(cType.startsWith('text')) {

      return res.text()

    }
    else {

      return res

    }
  });
}


async function post(url, entry) {

  let body = ''; for(let key in entry) {
    body += encodeURIComponent(key) + '='
    body += encodeURIComponent(entry[key]) + '&'
  } body = body.slice(0, -1)

  let headers = { 'Content-Type': 'application/x-www-form-urlencoded' }

  let opts = { method: 'POST', headers: headers, body: body }

  return await get(url, opts)

}

