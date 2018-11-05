function getCoords(cursor, canvas) {
  // Cursor is always in middle of screen.
  // If canvas-coords are the middle of screen,
  // cursor-coords are 0 and 0.
  // A coord-unit equals one cursor-height for top-pos,
  // and one cursor-width for left-pos.
  var canvasPosis = getPosis(canvas)
  var cursorPosis = getPosis(cursor)
  var leftDiff    = canvasPosis[0] - cursorPosis[0]
  var topDiff     = canvasPosis[1] - cursorPosis[1]
  var leftCoord   = ( leftDiff / getWidth(cursor) ) * -1
  var topCoord    = ( topDiff / getHeight(cursor) ) * -1
  if(leftCoord == -0) leftCoord = 0
  if(topCoord  == -0) topCoord  = 0
  return [leftCoord, topCoord]
}
