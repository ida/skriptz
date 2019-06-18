function addOptionEles(optionsParent, options, selectedIndex=0) {
  for(var i=0; i < options.length; i++) {
    var optionEle = document.createElement('option')
    optionEle.value = options[i]
    optionEle.innerHTML = options[i]
    optionsParent.appendChild(optionEle)
  }
}
function addSelectEle(selectionParent, options=[], selectedIndex=0) {
  var selectEle = document.createElement('select')
  addOptionEles(selectEle, options)
  selectEle.selectedIndex = selectedIndex
  selectionParent.appendChild(selectEle)
  return selectEle
}
function getSelectedOptionEle(selectEle) {
  return selectEle.children[selectEle.selectedIndex]
}
function getSelectedValue(selectEle) {
  var selectedOption = getSelectedOptionEle(selectEle)
  var value = selectedOption.innerHTML
  return value
}
function getSelectionValues(selectEle) {
  var values = []
  for(var i=0; i < selectEle.children.length; i++) {
    values.push(selectEle.children[i].innerHTML)
  }
  return values
}
function setOptions(selectEle, values) {
  selectEle.innerHTML = ''
  addOptionEles(selectEle, values)
}
function selectByValue(selectEle, value) {
  var values = getValues(selectEle)
}
