function validateNumberInput(ele) {
  // If val is below min or beyond max of ele, set val to min or max.
  // Allow only numberish input, including minus-sign and some special
  // keys: Arrow-keys, first-pos-, last-pos-, backspace-, minus-
  // remove-, tab-, shift-, F5-, return- and enter-key.
  // Allow anything while Strg-key is pressed.
  var allowedKeys = [8,9,13,16,17,35,36,37,38,39,40,46,48,49,50,
  51,52,53,54,55,56,57,96,97,98,99,100,101,102,103,104,105,116,173]

  var altIsPressed = false
  var strgIsPressed = false

  ele.onkeydown = eve => {

    if(eve.keyCode == 16)  altIsPressed = true
    if(eve.keyCode == 17) strgIsPressed = true

    if( ! strgIsPressed && ! allowedKeys.includes(eve.keyCode) ) {
      eve.preventDefault()
    }

  }

  ele.onkeyup = eve => {

    if(eve.keyCode == 16)  altIsPressed = false
    if(eve.keyCode == 17) strgIsPressed = false

    if( eve.target.max != '' && eve.target.value > Number(eve.target.max) ) {
      eve.target.value = Number(eve.target.max)
    }
    if( eve.target.min != '' && eve.target.value < Number(eve.target.min) ) {
      eve.target.value = Number(eve.target.min)
    }

    /* TODO: validate pasted value
    if(strgIsPressed && eve.keyCode == 86
    || altIsPressed && eve.keyCode == 45) {
    }*/

  }

}

