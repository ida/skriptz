function doAction(app) {
  var coordActionMap = {
    0: {
      //0: 'switchColor'
      0: switchColor
    }
  }
  var coords = getCoords(app.cursor.ele, app.canvas.ele)
  var action = coordActionMap[coords[0]]
  if(action !== undefined) {
    action = action[coords[1]]
    if(action !== undefined) {
//console.debug('app is:', app)

      action(app)
    }
  }
}
