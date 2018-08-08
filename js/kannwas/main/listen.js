function isArrowKey(keyCode) {
  var isArrowKey = false
  var arrowKeyCodes = [37, 38, 39, 40]
  for(var i=0; i < arrowKeyCodes.length; i++) {
    if(keyCode == arrowKeyCodes[i]) isArrowKey = true
  }
  return isArrowKey
}
function listenElements() {
  window.onkeydown = function(eve) {
    if(isArrowKey(eve.keyCode) === true) {
      var direction = null
      var distance = null
      if(eve.keyCode == 37) {
        direction = 'left'
        distance = cursor.width * -1
      }
      else if(eve.keyCode == 38) {
        direction = 'up'
        distance = cursor.height * -1
      }
      else if(eve.keyCode == 39) {
        direction = 'right'
        distance = cursor.width
      }
      else if(eve.keyCode == 40) {
        direction = 'down'
        distance = cursor.height
      }

      // Move canvas in contrary direction of pressed arrow-key:
      moveElement(canvas.ele, distance * -1, direction)
      // If canvas is not visible, move back to former position:
      //if(canvasIsInsideOfViewport() === false) {
      if(cursorIsInsideOfCanvas() === false) {
        moveElement(canvas.ele, distance, direction)
      }
      // Test a position-action:
      if(cursorIsInUpperLeftCornerOfCanvas()) {
        if(cursor.ele.style.backgroundColor == 'red') cursor.ele.style.backgroundColor = 'white'
        else cursor.ele.style.backgroundColor = 'red'
      }
    }
  }
  window.onresize = function() {
    styleElements()
  }
}

