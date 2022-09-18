const fs = require('fs')


var directoryPath = '/'
var fieldName = null
var fieldValue = null
var fileContent = null
var filePath = null
var genFilePath = fileName => {
  filePath = directoryPath
  if(directoryPath.endsWith('/') === false) filePath += '/'
  filePath += fileName
  return filePath
}
var html = null
var isDirectory = filePath => {
  return fs.statSync(filePath).isDirectory()
}
var isEditableFile = fileName => {
  var extensions = ['.css', '.csv', '.js', '.html', '.md', '.py', '.txt']
  for(var extension of extensions) if(fileName.endsWith(extension) === true) return true
  return false
}
module.exports = request => { directoryPath = request.url

  html = ''
//  html += request.data ? 'Sended data: ' + JSON.stringify(request.data) : ''

  // CLOSE FILE
  if(request.data && request.data['closeFile']) {
  }

  // SAVE FILE
  if(request.data && request.data['saveFile']) {
    fileContent = request.data['fileContent']
    filePath = request.data['filePath']
    fs.writeFileSync(filePath, fileContent)
  }

  // EDIT FILE
  if(request.data && request.data['filePath'] && ( ! request.data['closeFile'])) {
    filePath = request.data['filePath']
    fileContent = fs.readFileSync(filePath, 'utf-8')
fileContent=fileContent.replace(/`/g, '\`')
    console.debug('filePath',filePath)
    html = `<form action="${request.url}" method="post">
  <textarea name="fileContent" autofocus>${fileContent}</textarea>
  <input type="hidden" name="filePath" value="${filePath}" />
  <input type="submit" name="closeFile" value="Cancel" />
  <input type="submit" name="saveFile" value="Save" />
</form>`
  }

  // WALK
  if(request.data && request.data['directoryPath']) directoryPath = request.data['directoryPath']

var genFormHtml = (fileName, filePath, i) => {
    var html = `
    <form action="${request.url}" method="post">
      <input disabled style="
      width: 3em;
      text-align: right;
      margin-right: 0.27em;
      " value="${i+1}">
      <a href="${filePath}">${fileName}</a>
`

    if(isEditableFile(filePath)) {
      html += `
      <input type="hidden" name="filePath" value="${filePath}" />
      <input type="submit" value="Edit" />
`
    }

    html += `
    </form>
`
  return html
}

  html += '<p>' + directoryPath + '</p>\n'
  if(directoryPath != '/') {
    var parentPath = directoryPath.split('/'); parentPath = parentPath.slice(0, parentPath.length-1).join('/')
    if( ! parentPath ) parentPath = '/'
    html += genFormHtml('..', parentPath, -1)
  }
  var fileNames = fs.readdirSync(directoryPath)
  for(var i=0; i < fileNames.length; i++) {

    fileName = fileNames[i]
    filePath = genFilePath(fileName)
    html += genFormHtml(fileName, filePath, i)
  }
  return html
}
