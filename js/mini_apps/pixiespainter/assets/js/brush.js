function addBrush () {
    // Get:
    var colo = $(app + '-canvas-cursor').css('background-color')
    var size = Number($(app + '-controls-counters-size-value').text())
    var radi = Number($(app + '-controls-counters-radi-value').text())
    // Remove id of current cursor:
    $(app + '-canvas-cursor').removeAttr('id')    
    // Add new cursor:
    knot = app + '-canvas'
    // Set:
    //cursor = addEle('cursor').height(size).width(size).css('background', colo)
    cursor = addEle('cursor').css({
      'width': size,
      'height': size,
      'background': colo,
      'border-radius': radi + '%',
    });
}
function getBrushMode() {
  return $(app + '-controls-controller-middle').text()
}
function getBrushLength() {
  return Number($(app + '-controls-counters-size-value').text())
}
function getBrushStepLength() {
  var size = getBrushLength()
  var length = 0
  return getBrushLength() * getBrushStepVal() / 100
}
function getBrushStepVal() {
  return Number($(app + '-controls-counters-step-value').text())
}
function updateBrushColor(color) {
    $(app + '-canvas-cursor').css('background', '#' + color)
}
function updateBrush(para) {
  var cursor = $(app + '-canvas-cursor')
  var val_ele = $(app + '-controls-counters-' + para + '-value')
  var val = Number(val_ele.text())
  if(para == 'size') {
    cursor.width(val).height(val)
  }
  else if (para == 'step') {
  }
  else if (para == 'radi') {
    cursor.css('border-radius', val + '%')
  }
}
function moveBrush(direction) {
  var cursor = $(app + '-canvas-cursor')
  var step = getBrushStepLength()
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
addBrush()
