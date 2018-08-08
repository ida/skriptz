function getHeight(ele) {
  return getPropVal(ele, 'height')
}

function getLeft(ele) {
  return getPropVal(ele, 'left')
}

function getPropVal(ele, prop) {
  return parseFloat(window.getComputedStyle(ele).getPropertyValue(prop))
}

function getWidth(ele) {
  return getPropVal(ele, 'width')
}

function getRight(ele) {
  return getPropVal(ele, 'right')
}

function getTop(ele) {
  return getPropVal(ele, 'top')
}

