// Reload page when Alt+q is pressed.
var altIsPressed = false
window.onkeydown = eve => {
  if(eve.keyCode == 18) altIsPressed = true
  if(altIsPressed && eve.keyCode == 81) {
    window.location.href=window.location.href
  }
}
window.onkeyup = eve => {
  if(eve.keyCode == 18) altIsPressed = false
}
