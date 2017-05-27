//
// GLOBAL-VARS
//
var cellDeli = ';'
var columnDeli = '\n'
//
// COMMONS
//
function getNextSibling(ele) {
  var next_ele = null
  if(ele.nextSibling !== null) {
    var next_ele = ele.nextSibling
    while (next_ele.nodeType != 1) {
      next_ele=next_ele.nextSibling
    }
  }
  return next_ele
}
function getFirstChild(ele) {
  var first_child = null
  if(ele.firstChild !== null) {
    first_child = ele.firstChild
    while (first_child.nodeType != 1) {
      first_child = getNextSibling(first_child)
    }
  }
  return first_child
}
function getFirstChildren(ele) {
  var eles = null
  if(ele !== undefined) {
    ele = getFirstChild(ele)
    eles = [ele]
    while(getNextSibling(ele) !== null) {
      ele = getNextSibling(ele)
      eles.push(ele)
    }
  }
  return eles
}
//
// SPECIFICA
//
function showTableAfterUpload (content) {
  var csv = content
  var rows = csv.split(columnDeli)
  var keys = rows[0].split(cellDeli)
  // Upload appends a line, remove it:
  csv = rows.join(columnDeli).slice(0, -columnDeli.length)
  setTable(csv)
  showTable(keys)
}
//
// MAIN
//
document.addEventListener("DOMContentLoaded", function(event) {
  var keys = null

// For testing, uncomment the following two lines:
//  csv = 'Firstname;Lastname;Passion\nIda;Ebkes;Python\nAda;Ebkes;Lion'
//  setTable(csv)
// For defining an order for the keys, uncomment following line:
//  keys = csv.split(columnDeli)[0].split(cellDeli)

  showTable(keys)
	provideFileUpload(document.body, showTableAfterUpload) // requires ../files.js

}); // dom loaded
