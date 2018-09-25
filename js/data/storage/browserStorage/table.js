// Show a browser-storage's key's CSV-value as an HTML-list with a table-like look.
function showTable(tableEle, key) {
console.debug(key)
  var html = ''
  var rows = localStorage.getItem(key).split(rowDeli)
  for(var i in rows) {
    html += '<' + htmlListType + '>'
    var cells = rows[i].split(cellDeli)
    for(var j in cells) {
      html += '<li>' + cells[j] + '</li>'
    }
    html += '<' + htmlListType + '>'
  }
  tableEle.innerHTML = html
}
