function main() {
//  alert('Hello!')

  var body = document.getElementsByTagName('body')[0]
  var ele = addEle(body, 'div')
  setStyles(body, 'background: #000; color: #e2e2e2;')
  setStyles(root, 'height: 90%; width: 90%; margin: 2.7% 4.9% 0 4.9%; background: red;')

  //var styles = root.getAttribute('style')
  var styles = window.getComputedStyle(root)
var list = styles
for(var i=0;i<list.length;i++){
  var item = list[i]
  ele.innerHTML = ele.innerHTML += item += ' : '
  ele.innerHTML = ele.innerHTML += getStyle(ele, item) += '<br>'
}

/////////////////////////////////////////////////////////////////


/////////////////////////////////////////////////////////////////
}

function doAfterDocReady(funcName) {
  // We do not support IE < 9 no more :-)
  document.addEventListener("DOMContentLoaded", function(event) { 
setTimeout(funcName(), 10000);
  });
}

doAfterDocReady(main)
