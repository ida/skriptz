function printTable(keys=nulli, printEle=document.body) {
  var new_rows = []
  if(keys === null) { keys = getKeys() }
  var table = getTable(keys)
  var rows = table.split(columnDeli)
  for(var i=0; i < rows.length;  i++) {
    var cells = rows[i].split(cellDeli)
    for(var j=0; j < cells.length;  j++) {
    if(i == 0) {
      new_rows.push([])
    } 
      new_rows[j].push(cells[j])
    }
  }
  rows = new_rows
  var html = ''
  for(var i=0; i < rows.length;  i++) {
    var cells = rows[i]
    html += '<div>'
    for(var j=0; j < cells.length;  j++) {
      html += '<span>' + cells[j] + '</span>'
    }
    html += '</div>'
  }
  printEle.innerHTML = html
}
