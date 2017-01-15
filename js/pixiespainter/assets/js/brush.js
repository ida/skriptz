function updateBrushColor(color) {
    $(app + '-canvas-cursor').css('background', '#' + color)
}
function updateBrush(para) {
    var val_ele
    if(para=='size') {
        val_ele = $(app + '-controls-counters-size-value')
    }
    var val = Number(val_ele.text())
    $(app + '-canvas-cursor').width(val).height(val)
}
function moveBrush(direction) {

    // Get some vals:
    var cursor = $(app + '-canvas-cursor')
    var step = parseInt(cursor.width())
    var left = parseInt(cursor.css('left'))
    var topp = parseInt(cursor.css('top'))
    // Calc new position:
    if(direction=='left' || direction=='upleft' || direction=='downleft') {
        left -= step
    }
    if(direction=='right' || direction=='upright' || direction=='downright') {
        left += step
    }
    if(direction=='up' || direction=='upright' || direction=='upleft') {
        topp -= step
    }
    if(direction=='down' || direction=='downright' || direction=='downleft') {
        topp += step
    }
    // Put brush on/off:
    if(direction=='middle') {
        if($(app + '-controls-controller-middle').text() == 'off') {
        //alert($(app + '-controls-controller-middle').text())
            $(app + '-controls-controller-middle').text('on')
        }
        else {
            $(app + '-controls-controller-middle').text('off')
        }
    }

    if($(app + '-controls-controller-middle').text() == 'on') {
        addBrush()
    }
    // Move it:
    $(app + '-canvas-cursor').css({'left':left, 'top':topp}) 
}
function addBrush () {
    // Get:
    var colo = $(app + '-canvas-cursor').css('background-color')
    var size = Number($(app + '-controls-counters-size-value').text())
    // Remove id of current cursor:
    $(app + '-canvas-cursor').removeAttr('id')    
    // Add new cursor:
    knot = app + '-canvas'
    // Set:
    cursor = addEle('cursor').height(size).width(size).css('background', colo)
}
addBrush()
