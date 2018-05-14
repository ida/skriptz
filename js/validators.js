function isFloat(value){
  return isNan(Number(value)) === false && value % 1 !== 0
}
function isInt(value) {
  return Number.isInteger(value)
}
function isNr(value) {
  return isNaN(Number(value)) === false
}
