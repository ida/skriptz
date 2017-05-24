var rowDeli = '\n'
var cellDeli = ';'
var htmlListType = 'ol'
function applyListeners() {
  // For all list-items:
  var list_items = document.getElementsByTagName('li')
  for(var i=0; i < list_items.length; i++) {
    // If clicked:
    list_items[i].onclick = function(eve) {
      // Show table:
      showTable(document.body, eve.target.textContent)
    }
    // If focused and key was pressed:
    list_items[i].onkeydown = function(eve) {
      // And it's the enter-key:
      if(eve.keyCode == 13) {
        // Simulate click to trigger click-event:
        eve.target.click()
      }
    }
  }
}
document.addEventListener("DOMContentLoaded", function(event) {
  showStorages(document.body)
  applyListeners()
}); // dom loaded
