function computeStyles(app) {
  //
  // Compute centering canvas and cursor in viewport.
  //

  app.viewport.height = getHeight(viewport.ele)

  app.viewport.width = getWidth(viewport.ele)


  app.canvas.left = (viewport.width - canvas.width)/2

  app.canvas.top = (viewport.height - canvas.height)/2


  app.cursor.left = canvas.width/2 - cursor.width/2 + canvas.left

  app.cursor.top = canvas.height/2 - cursor.height/2 + canvas.top

}

function styleElements(app) {


  // Set dimensions, so we can measure ele:
  app.viewport.ele.style = `
    margin: 0;
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    overflow: hidden;
  `

  // Compute styles with measurable height:
  computeStyles(app)


  // Set computed styles:
  app.canvas.ele.style = `
    position: absolute;
    top: ${canvas.top}px;
    left: ${canvas.left}px;
    width: ${canvas.width}px;
    height: ${canvas.height}px;
    background: url(media/mandala.svg);
    opacity: 0.7;
  `
  app.cursor.ele.style = `
    position: absolute;
    top: ${cursor.top}px;
    left: ${cursor.left}px;
    width: ${cursor.width}px;
    height: ${cursor.height}px;
    background: white;
  `

}

