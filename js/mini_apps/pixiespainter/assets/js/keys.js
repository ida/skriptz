// This file holds hotkey-bindings and tabbing-behaviour.

function makeElesTabbable() {
  var selectas = ['', // == '#[app]-container'
                  '-controls-controller-middle',
                  ' .undo',
                  ' .counter div',
                  ' .button']

  for(var i=0; i < selectas.length; i++) {
    var selecta = app + selectas[i]
    $(selecta).attr('tabindex', '0')
  }
}
function defineHotkeys() {
  // Focus is in app and a key was pressed:
  $(app).keydown(function(eve) {
      var key = eve.keyCode

      // ENTER/RETURN- or SPACE-key, simulate click focused ele:
      if(key==13 || key==32) {
          $(eve.target).click()
      }
      // '5' of numpad -> brush on/off: 
      if(key==12) {
          $(app + '-controls-controller-middle').click()
      }
      // BACKSPACE -> delete latest cursor and
      // give cursor-id to then last div: 
      if(key==8) {
          $(app + ' .undo').click()
      }

      // ARROWS, simulate click on controller-buttons:
      if(key==33) { // upright
          $(app + '-controls-controller-upright').click()
      }
      if(key==34) { // downright
          $(app + '-controls-controller-downright').click()
      }
      if(key==35) { // downleft
          $(app + '-controls-controller-downleft').click()
      }
      if(key==36) { // upleft
          $(app + '-controls-controller-upleft').click()
      }
      if(key==37) { // left
          $(app + '-controls-controller-left').click()
      }
      if(key==38) { // up
          $(app + '-controls-controller-up').click()
      }
      if(key==39) { // right
          $(app + '-controls-controller-right').click()
      }
      if(key==40) { // down
          $(app + '-controls-controller-down').click()
      }

  });
}
(function ($) {
  makeElesTabbable()
  defineHotkeys()
})(jQuery);
