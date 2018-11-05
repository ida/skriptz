function initiateApp(app) {

  app.viewport.ele = document.body  // set app-ele

  createElements(app)              // set app-children-eles
  styleElements(app)
  onArrowKey(app)

  app.cursor.ele.tabIndex = 0       // make cursor focusable
  app.cursor.ele.focus()            // focus cursor

}
