// https://developer.mozilla.org/en-US/docs/Web/API/File

function addFilesInputEle(containerEle) {
  var input = document.createElement('input')      // create input
  input.type = 'file'                      // make it a file-input
  input.setAttribute('multiple', '')      // enable multiple files
  containerEle.appendChild(input)           // insert input in DOM
  return input
}
function doAfterLoadWithFileContent(content) {
document.body.innerHTML = content
}
function getSelectedFiles(inputEle) {
  return inputEle.files
}
function loadFile(file, reader, doAfterLoadWithFileContent=null) {
  if(doAfterLoadWithFileContent) {       // if function was passed
    reader.onloadend = function(eve) {      // when a file is read
        doAfterLoadWithFileContent(eve.target.result)  // exe func
    }
    // Let's use the read-method, which supports most browsers:
    reader.readAsArrayBuffer(file)                    // load file
  }
}
function main() {
  var reader = new FileReader()
  var input = addFilesInputEle(document.body)
  input.onchange = function(eve) {         // user selects file(s)
    var files = getSelectedFiles(eve.target)
    for(var i = 0; i < files.length-1; i++) {     // for each file
       var file = files[i]                // load and process file
       loadFile(file, reader, doAfterLoadWithFileContent)
    }
  }
}
document.addEventListener("DOMContentLoaded", function(event) {
  main()
});
