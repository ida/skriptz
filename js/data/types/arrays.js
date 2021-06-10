function appendArray(array, otherArray) {
  array.push.apply(array, otherArray)
}
function appendItem(array, item) {
  array.push(item)
}
function copyArray(array) {
  var copiedArray = (...array)
  return copiedArray
}
function getItemPos(array, item) {
  return array.indexOf(item)
}
function insertItem(array, item, insertPos) {
  array.splice(insertPos, 0, item)
}
function insertItems(array, items, insertPos) {
  array.splice(insertPos, 0, ...items)
}
function prependItem(array, item) {
  array.unshift(item)
}
function mergeArrays(arrayOfArrays) {
  // Make several arrays become one, exclude duplicate items.
  var mergedArray = []
  for(var i in arrayOfArrays) {
    var array = arrayOfArrays[i]
    for(var j in array) {
      var item = array[j]
      if( ! mergedArray.includes(item)) mergedArray.push(item)
    }
  }
  return mergedArray
}
function moveItem(array, itemPos, targetPos) {
  var item = array.splice(itemPos, 1) // at itemPos remove 1 item
  array.splice(targetPos, 0, item) // at targetPos remove nothing and add item
  return array
}
function removeItem(array, itemPos) {
  // 'splice' returns the item at itemPos, this would not work,
  // if we'd do a loop like this:
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

