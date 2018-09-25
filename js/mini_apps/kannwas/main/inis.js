function initiateApp() {

  viewport.ele = document.body  // set app-ele

  createElements()              // set app-children-eles
  styleElements()
  listenElements()

  cursor.ele.tabIndex = 0       // make cursor focusable
  cursor.ele.focus()            // focus cursor

}
