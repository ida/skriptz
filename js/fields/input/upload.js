function addUploadButton(parentEle, doWithContentAfterUpload) {
// Requires: ./addUploadInput()
// Add an input-ele for uploading files and hide it behind another ele
// that says 'Upload', instead of 'Browse...' – or whatever the browser
// decides to display – to have full control over the button's appearance.

  // Insert 'Upload'-wrapper:
  var ele = addEle(parentEle, '', 'span')
  var wrapper = ele
  ele.style = 'position: relative; top: 0; left: 0; display: none;'
  // Insert 'Upload'-button:
  addEle(ele, 'Upload', 'span')
  // Insert 'Browse'-button:
  ele = addUploadInput(ele, doWithContentAfterUpload)
  // Hide 'Browse', leave 'Upload' visible:
  ele.style = '\
    position: absolute;\
    top: 0;\
    left: 0;\
    height: 1.5em;\
    width: 5em;\
    margin: 0;\
    padding: 0;\
    font-size: 20px;\
    cursor: pointer;\
    opacity: 0;\
    filter: alpha(opacity=0);'

  return wrapper
}


function addUploadInput(containerEle, doWithContentAfterUpload) {
// Append a browse-button to containerEle for selecting files to upload,
// do something with the uploaded content after selection got confirmed
// by user. Usage example:
//
//    var containerEle = document.body
//    function doSthAfterUpload (content) { console.debug(content) }
//    addUploadButton(containerEle, doSthAfterUpload)
//

  function addFilesInputEle(containerEle) {
    var input = document.createElement('input') // create input
    input.type = 'file'                        //  make it a file-input
    input.setAttribute('multiple', 'true')    //   enable multiple files
    containerEle.appendChild(input)          //    insert input in DOM
    return input
  }
  function provideInputEle(containerEle, reader) {
    var input = addFilesInputEle(containerEle)          // add input
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

}
