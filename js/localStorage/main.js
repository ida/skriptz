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
// MAIN
//
document.addEventListener("DOMContentLoaded", function(event) {
  var csv = null
  var keys = null

// For testing, uncomment the following two lines:
//  csv = 'Firstname;Lastname;Passion\nIda;Ebkes;Python\nAda;Ebkes;Lion'
//  setTable(csv)
// For defining an order for the keys, uncomment following line:
//  keys = csv.split(columnDeli)[0].split(cellDeli)

   showTable(keys)


	// Requires ../files.js/provideFileUpload()
	function doSthAfterUpload (content, csv, keys) {
		csv = content
		setTable(csv)
		keys = csv.split(columnDeli)[0].split(cellDeli)
		showTable(keys)
	}
	var inputContainer = document.body
	provideFileUpload(inputContainer, doSthAfterUpload)


}); // dom loaded
