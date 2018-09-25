function moveElement(ele, distance, direction) {
  var property = 'left'
  if(direction == 'up' || direction == 'down') property = 'top'
  ele.style[property] = distance + parseFloat(ele.style[property])
}

