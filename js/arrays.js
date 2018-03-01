function appendArray(array, otherArray) {
  array.push.apply(array, otherArray)
}
function appendItem(array, item) {
  array.push(item)
}
function getItemPos(array, item) {
  return array.indexOf(item)
}
function prependItem(array, item) {
  array.unshift(item)
}
function moveItem(array, itemPos, targetPos) {
  var item = array.splice(itemPos, 1) // at itemPos remove 1 item
  array.splice(targetPos, 0, item) // at targetPos remove nothing and add item
  return array
}
function removeAndReturnFirstItem(array) {
  array.shift()
}
function removeAndReturnLastItem(array) {
  array.pop()
}

