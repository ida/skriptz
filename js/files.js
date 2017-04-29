// What
// ====
// Let a user select a file from their filesystem, immediately upload
// it, and do something with its content.
//
// Why
// ===
// Provide a possibility to upload a file's content into a serverless
// browser-app. For example to read csv-files and display them in a
// table-like manner as html-lists.
//
// Usage
// =====
// function doStWithContentAfterUpload () { console.debug(content) }
// var inputContainer = document.body
// provideFileUpload(inputContainer, doStWithContentAfterUpload)
//
// Docs
// ====
// https://developer.mozilla.org/en-US/docs/Web/API/File
//
function addFilesInputEle(inputContainer) {
  var input = document.createElement('input')      // create input
  input.type = 'file'                      // make it a file-input
  input.setAttribute('multiple', 'true')  // enable multiple files
  inputContainer.appendChild(input)         // insert input in DOM
  return input
}
function provideInputEle(inputContainer, reader) {
  var input = addFilesInputEle(inputContainer)        // add input
  input.onchange = function(eve) {      //  when user selects file
    var file = eve.target.files[0]                  //    get file
    reader.readAsText(file)                        //    load file
  }
}
function provideFileReader(doAfterFileUpload=null) {
  var reader = new FileReader()           //   provide file-reader
  reader.onloadend = function(eve) {     // when a file has loaded
    doAfterFileUpload(eve.target.result)// do sth with its content
  }
  return reader
}
function provideFileUpload(inputContainer, doAfterFileUpload) {
  var reader  = provideFileReader(doAfterFileUpload)
  provideInputEle(inputContainer, reader)
}
