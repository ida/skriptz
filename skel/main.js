function addEle(parentEle, eleTagName='div') {
  var ele = document.createElement(eleTagName)
  parentEle.appendChild(ele)
  return ele
}
function main() {
var appEle = document.body
var scriptEle = addEle(appEle, 'script')
//scriptEle.text = 'alert("I")'
var scriptEle = document.createElement('script')
scriptEle.innerHTML = 'alert("I")'
appEle.appendChild(scriptEle)
}

function doAfterDocReady(funcName) {
  // We do not support IE < 9 no more :-)
  document.addEventListener("DOMContentLoaded", function(event) { 
    funcName()
  });
}

doAfterDocReady(main)
