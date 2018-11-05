function createElements(app) {

  app.viewport.ele.innerHTML = '' // destroy before possible re-creation

  app.canvas.ele = document.createElement('div')
  app.viewport.ele.appendChild(canvas.ele)

  app.cursor.ele = document.createElement('div')
  app.viewport.ele.appendChild(cursor.ele)

}

