function isFloat(value){
  return ! Number.isInteger(Number(value))
}
function isInt(value) {
  return Number.isInteger(Number(value))
}
function isNr(value) {
  // Regard `Number` returns zero for empty strings.
  return value != '' && isNaN(Number(value)) === false
}


function secondsToMs(seconds) {

// Return milliseconds with a length of exactly four digits.

  if(String(seconds).indexOf('.') != -1) {

    var beforeComma = String(seconds).split('.')[0]

    var afterComma = String(seconds).split('.')[1].slice(0, 3)

    seconds = beforeComma + afterComma
  }

  if(String(seconds).length < 4) {

    while(String(seconds).length < 4) {

      seconds = seconds * 10

    }

  }

  return seconds

}

