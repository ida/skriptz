// Kannwas
// =======
// Single-page-application, showing a centered square in a huge square,
// movable with arrow-keys, while the cursor stays centered within the
// viewport.


// The used elements as objects with properties, assumed to be present
// globally, by the other scripts:
var viewport = {}
var canvas = {}
var cursor = {}

// Set an arbitrary length for the cursor:
cursor.width = 100
cursor.height = cursor.width

// The length of the canvas must be a multiple of the cursor's length,
// where the multiplicator must be an uneven whole number, so the edges of
// the cursor hit exactly the edge of the canvas, when trying to cross it:
canvas.width = cursor.width * 19
canvas.height = canvas.width

var tolerance = cursor.width/2
var app = {
  viewport: viewport,
  canvas: canvas,
  cursor: cursor,
}
initiateApp(app)

// EOF ////////////////////////////////////////////////////

