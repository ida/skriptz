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
