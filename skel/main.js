function main() {
 alert('Hello!')
}

function doAfterDocReady(funcName) {
  // We do not support IE < 9 no more :-)
  document.addEventListener("DOMContentLoaded", function(event) { 
    funcName()
  });
}

doAfterDocReady(main)
