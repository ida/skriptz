function isFloat(value){
  return isNan(Number(value)) === false && value % 1 !== 0
}
function isInt(value) {
  return Number.isInteger(value)
}
function isNr(value) {
  // Regard `Number` converts empty strings to zero.
  return value != '' && isNaN(Number(value)) === false
}
