const express = require('express')
const fs = require('fs')
const app = express()
const rootDirectoryPath = '.'//home/ida/Serve/Statica/adi/public'

var audioExtensions = ['wav', 'ogg']
var pictureExtensions = ['jpg', 'jpeg', 'png']
var textExtensions = ['txt', 'md']
var fileExtensions = audioExtensions.concat(textExtensions).concat(pictureExtensions)
function genAudioHtml(audioPath) {
  return '<audio autobuffer="" controls=""><source src="' + audioPath + '"></audio>'
}
function genContentHtml(filePath, childRelUrl, childAbsUrl) {
  var html = ''
  if(isFile(filePath)) {
    html += '<div class="content">'
    if(isAudioFile(filePath) === true) {
      html += genAudioHtml(childRelUrl)
    }
    else if(isPictureFile(filePath) === true) {
      html += genPicureHtml(childRelUrl)
    }
    else {
      html += fs.readFileSync(childAbsUrl)
    }
    html += '</div>'
  }
  return html
}
function genPicureHtml(url) {
  var str =
  '<div style="height: 100px; width: 100px; overflow: hidden;">' +
  '<img src="' + url + '">' +
  '</div">'
  return str
}
function genRootLink() {
  return '<div><a href="/">Back to overview</a></div>'
}
function genTitleHtml(filePath, childRelUrl) {
  var html = '<div class="title">'
  if( ! isFile(filePath) ) html += '<a href="' + childRelUrl + '">'
  html += filePath
  if( ! isFile(filePath) ) html += '</a>'
  html += '<div>'
  return html
}
function isFile(filePath) {
  var extensions = fileExtensions
  for(var i in extensions) {
    if(filePath.endsWith('.' + extensions[i])) {
      return true
    }
  }
  return false
}
function isAudioFile(filePath) {
  for(var i in audioExtensions) {
    if(filePath.endsWith('.' + audioExtensions[i])) {
      return true
    }
  }
  return false
}
function isPictureFile(filePath) {
  for(var i in pictureExtensions) {
    if(filePath.endsWith('.' + pictureExtensions[i])) {
      return true
    }
  }
  return false
}
app.use(express.static(rootDirectoryPath))
app.get("/*", (request, response) => {
  var childAbsUrl = null
  var childRelUrl = null
  var html = ''
  var title = request.url.slice(1)
  var url = rootDirectoryPath + request.url
  if(request.url != '/') {
    html += genRootLink()
  }
  else {
    title = 'public'
  }
  html += '<h2>' + title + '</h2>'
  fs.readdirSync(url).forEach(filePath => {
    childRelUrl = encodeURI(filePath)
    childAbsUrl = url + childRelUrl
    html += '<div class="child">'
    html += genTitleHtml(filePath, childRelUrl)
    html += genContentHtml(filePath, childRelUrl, childAbsUrl)
    html += '</div>'
  });
  response.send(html)
});
app.listen(port=3000, (err) => {
  console.log('Listening to', port)
});

