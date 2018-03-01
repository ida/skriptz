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
function removeItem(array, itemPos) {
  // 'splice' returns the item at itemPos, this would not work,
  // if we'd do this upon loop like this:
  //
  //     for(var key in array) removeItem(array, key)
  //
  // Let's fetch the return in a var, so looping works:
  var removedItem = array.splice(itemPos, 1)
}
function removeAndReturnFirstItem(array) {
  array.shift()
}
function removeAndReturnLastItem(array) {
  array.pop()
}

