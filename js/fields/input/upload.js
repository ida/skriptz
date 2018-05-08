function addUploadButton(containerEle, doWithContentAfterUpload) {
// Append a browse-button to containerEle for selecting files to upload,
// do something with the uploaded content after selection got confirmed
// by user. Usage example:
//
//    var containerEle = document.body
//    function doSthAfterUpload (content) { console.debug(content) }
//    addUploadButton(containerEle, doSthAfterUpload)
//

  function addFilesInputEle(containerEle) {
    var input = document.createElement('input')      // create input
    input.type = 'file'                      // make it a file-input
    input.setAttribute('multiple', 'true')  // enable multiple files
    containerEle.appendChild(input)         // insert input in DOM
    return input
  }
  function provideInputEle(containerEle, reader) {
    var input = addFilesInputEle(containerEle)        // add input
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
  function provideFileUpload(containerEle, doAfterFileUpload) {
    var reader  = provideFileReader(doAfterFileUpload)
    var input = provideInputEle(containerEle, reader)
    return input
  }

  return provideFileUpload(containerEle, doWithContentAfterUpload)

} // addUploadButton
