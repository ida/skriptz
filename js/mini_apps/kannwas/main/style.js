function computeStyles() {
  //
  // Center canvas and cursor in viewport.
  //

  viewport.height = getHeight(viewport.ele)

  viewport.width = getWidth(viewport.ele)


  canvas.left = (viewport.width - canvas.width)/2

  canvas.top = (viewport.height - canvas.height)/2


  cursor.left = canvas.width/2 - cursor.width/2 + canvas.left

  cursor.top = canvas.height/2 - cursor.height/2 + canvas.top

}

function styleElements() {


  // Set dimensions, so we can measure ele:
  viewport.ele.style = `
    margin: 0;
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    overflow: hidden;
  `

  // Compute styles with measurable height:
  computeStyles()


  // Set computed styles:
  canvas.ele.style = `
    position: absolute;
    top: ${canvas.top}px;
    left: ${canvas.left}px;
    width: ${canvas.width}px;
    height: ${canvas.height}px;
    background: url(media/mandala.svg);
    opacity: 0.7;
  `
  cursor.ele.style = `
    position: absolute;
    top: ${cursor.top}px;
    left: ${cursor.left}px;
    width: ${cursor.width}px;
    height: ${cursor.height}px;
    background: white;
  `

}

