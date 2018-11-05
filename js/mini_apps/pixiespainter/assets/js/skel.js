function addEle(parentEle, id=null, tagName='div') {
  var ele = document.createElement(tagName)
  parentEle.appendChild(ele)
  if(id !== null) ele.id = id
  return ele
}
function addMarkupSkel(appEle) {
  var app = 'pixiespainter'
  var id = app + '-container'
  var ele = addEle(addEle, id)

  id  = 'canvas'
  addEle(addEle, id)

  id  = 'controls'
  addEle(addEle, id)
}
addMarkupSkel(document.body)
