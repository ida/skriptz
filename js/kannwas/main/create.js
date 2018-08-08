function createElements() {

  viewport.ele.innerHTML = '' // destroy before possible re-creation

  canvas.ele = document.createElement('div')
  viewport.ele.appendChild(canvas.ele)

  cursor.ele = document.createElement('div')
  viewport.ele.appendChild(cursor.ele)

}

