// canvas and cursor are assumed to be siblings and absolute positioned
// canvas is assumed to move, while cursor stays positioned in viewport-center

function canvasIsInsideOfViewport() {
  var isInside = true 
  if(canvasIsAboveViewport() === true) {
      isInside = false
  }
  if(canvasIsBelowViewport() === true) {
      isInside = false
  }
  if(canvasIsLeftOfViewport() === true) {
      isInside = false
  }
  if(canvasIsRightOfViewport() === true) {
      isInside = false
  }
  return isInside
}

function canvasIsAboveViewport() {
  return getTop(canvas.ele) * -1 > canvas.height - tolerance
}

function canvasIsBelowViewport() {
  return getTop(canvas.ele) > viewport.height - tolerance
}

function canvasIsLeftOfViewport() {
  return getLeft(canvas.ele) * -1 > canvas.width - tolerance
}

function canvasIsRightOfViewport() {
  return getLeft(canvas.ele) > viewport.width - tolerance
}


function cursorIsInsideOfCanvas() {
  if(
  cursorIsRightOfCanvas()
  ||
  cursorIsLeftOfCanvas()
  ||
  cursorIsAboveCanvas()
  ||
  cursorIsBelowCanvas()
  ) {
    return false
  }
  return true
}

function cursorIsAboveCanvas() {
  return getTop(canvas.ele) > getTop(cursor.ele) 
}

function cursorIsBelowCanvas() {
  return getTop(canvas.ele) + canvas.width <
         getTop(cursor.ele) + cursor.height
}

function cursorIsLeftOfCanvas() {
  return getLeft(canvas.ele) > getLeft(cursor.ele) 
}

function cursorIsRightOfCanvas() {
  return getLeft(canvas.ele) + canvas.width <=
         getLeft(cursor.ele)
}

function cursorIsInUpperLeftCornerOfCanvas(top, left) {
  // == canvas-pos is middle of viewport
  if(
    parseInt(getTop(canvas.ele)) == parseInt(viewport.height/2 - cursor.height/2)
    &&
    parseInt(getLeft(canvas.ele)) == parseInt(viewport.width/2 - cursor.width/2)
    ) {
      return true
  }
  return false
}

