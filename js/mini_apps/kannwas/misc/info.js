function addInfo(msg='') {
  var infoEleId = ' info'
  var infoEle = document.getElementById(infoEleId)
  if(infoEle === null) {
    infoEle = document.createElement('div')
    document.body.insertBefore(infoEle, document.body.firstChild)
    infoEle.id = infoEleId
  }
  infoEle.innerHTML = msg + '<br>' + infoEle.innerHTML
}
