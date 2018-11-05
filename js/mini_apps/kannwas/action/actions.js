function switchColor(app, colors=['white', 'red']) {

  var ele = app.cursor.ele
  if(ele.style.backgroundColor == colors[1]) {
    cursor.ele.style.backgroundColor = colors[0]
  }
  else {
    ele.style.backgroundColor = colors[1]
  }
}
