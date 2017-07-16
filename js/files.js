//
// UPLOAD
// ======
//
// What
// ----
// Let a user select a file from their filesystem, immediately upload
// it, and do something with its content.
//
// Why
// ---
// Provide a possibility to upload a file's content into a serverless
// browser-app. For example to read csv-files and display them in a
// table-like manner as html-lists.
//
// Usage
// -----
// function doSthAfterUpload (content) { console.debug(content) }
// var inputContainer = document.body
// provideFileUpload(inputContainer, doSthAfterUpload)
//
// Docs
// ----
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
    reader.readAsText(file, 'ascii')               //    load file
  }
  return input
}
function provideFileReader(doAfterFileUpload) {
  var content = null
  var reader = new FileReader()           //   provide file-reader
  reader.onloadend = function(eve) {     // when a file has loaded
    content = eve.target.result         // fetch content
    // Remove last empty line that has been appended after upload:
    content = content.slice(0, content.length-1)
    doAfterFileUpload(content)       // pass content to callback
  }
  return reader
}
function provideFileUpload(inputContainer, doAfterFileUpload) {
  var reader  = provideFileReader(doAfterFileUpload)
  var input = provideInputEle(inputContainer, reader)
  return input
}
//
// DOWNLOAD
//
// Example:
//  var containerEle = document.body
//  var downloadContent = document.body.innerHTML
//  provideFileExport(containerEle, downloadContent)
//
function provideFileExport(containerEle, downloadContent) {
  var exportButton = document.createElement('a')
  exportButton.id = 'download'
  exportButton.textContent = 'Download'
  exportButton.setAttribute('download', 'tesa.csv')
  updateDownloadButton(exportButton, downloadContent)
  containerEle.appendChild(exportButton)
}
function updateDownloadButton(button, downloadContent) {
  button.href = 'data:application/csv;charset=utf-8,'
              + encodeURIComponent(downloadContent)
}
