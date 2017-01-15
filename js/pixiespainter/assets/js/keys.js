(function ($) {

    // TAB, make these div's tabbable and let them go with the flow(val=0):
    // Empyt string is app, other selectors, if not id, need a prepending space,
    // ids need a prepending minus.
    var selectas = ['', 
                    ' .button', 
                    ' .buttons > div']
                    /* 
                    '-controls-toggler', 
                    ' .counter div'] 
                    */

    for(var i=0; i < selectas.length; i++) {
        var selecta = app + selectas[i]
        $(selecta).attr('tabindex', '0')
    }

    // Focus is in app and a key was pressed:
    $(app).keydown(function(eve) {
        var key = eve.keyCode

        // ENTER/RETURN, simulate click focused ele:
        if(key==13) {
            $(eve.target).click()
        }
        // '5' of numpad -> brush on/off: 
        if(key==12) {
            $(app + '-controls-controller-middle').click()
        }
        // BACKSPACE -> delete latest cursor: 
        if(key==8) {
            $(app + '-canvas-cursor').remove()
            $(app + '-canvas :last-child').attr('id', (app + '-canvas-cursor').slice(1))
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
})(jQuery);
