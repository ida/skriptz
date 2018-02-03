function loadFileAndDoSthWithText(filePath, doSthWithText) {
  //
  // filePath is expected to be relative to the directory of
  // this file and must live within this directory.
  //
  // doSthWithText is expected to be a function or a function-name,
  // it gets the loaded text of the file passed as a parameter.
  //
  // Example usage:
  //
  //   loadFileAndDoSthWithText(
  //     'styles/waffles.css',
  //     function(text) { console.log(text) }
  //    );
  //
  var request = new XMLHttpRequest()
  request.overrideMimeType("text/plain")
  request.open('GET', filePath, true)
  request.onload = function() {
    if (request.status >= 200 && request.status < 400) {
      doSthWithText(request.responseText)
    }
    else {
      console.error("Couldn't load text of '" + filePath + "'.")
    }
  }
  request.onerror = function(error) {
    console.error("Couldn't get a connection to '" + filePath + "'.")
    console.error(error)
  }
  request.send()
}



function loadFilesAndDoSthWithTexts(filePaths, doSthWithTexts) {
  //
  // requires: loadFileAndDoSthWithText()
  //
  // filePaths is expected to be an array
  //
  // doSthWithTexts is expected to be a function or a function-name,
  // it gets the loaded text of the file passed as a parameter.
  //
  // Example usage:
  //
  //   loadFilesAndDoSthWithTexts(
  //     ['styles/waffles.css', 'miles/dav.is'],
  //     function(text) { console.log(text) }
  //    );
  //

  var texts = ''

  function addTextToTexts(text) {
    texts += text     
    texts += '\n'
    if(filePaths.length > 0) {
      loadFileAndDoSthWithText(filePaths.shift(), addTextToTexts)
    }
    else {
      doSthWithTexts(texts)
    }
  }

  loadFileAndDoSthWithText(filePaths.shift(), addTextToTexts)
}

