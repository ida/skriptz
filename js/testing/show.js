/*

All function-names starting with 'show' are div-wrappers 
around the showHtml-function, with certain classes
for styling.

*/

function show(html) {
  showHtml(html)
}

function showHtml(html) {
  document.body.innerHTML += html
}

function showAndExecuteCode(codeAsString) {
  var script = document.createElement('script')
  showCode(codeAsString)
  script.innerHTML = '\n' + codeAsString
  document.getElementsByTagName('head')[0].appendChild(script)
}


function showCode(text) {
  showHtml('<pre class="showCode">' + htmlToText(text) + '</pre>')
}

function showError(text) {
  showHtml('<div class="showError">' + text + '</div>')
}

function showWarning(text) {
  showHtml('<div class="showWarning">' + text + '</div>')
}

function showLinkOfCalledFile(fileName) {
  showHtml( '<div class="showLinkOfCalledFile"><a href="' + fileName + '">'
           + fileName + '</a></div>')
}

function showHtmlOutput(html) {
  showHtml('<div class="htmlOutput">' + html + '</div>')
}

function showObject(obj) {
  showHtml(objToHtml(obj))
}

function showReturn(text) {
  showHtml('<div class="showReturn">' + text + '</div>')
}

function showTag(tag, literal=false) {
  showReturn(tagToHtml(tag, literal))
}


/*
    Conversion-helpers:
*/


function htmlToText(text) {
  text = text.replace(/</g,"&lt;")
  return text
}


function objToHtml(obj, literal=false) {
  var html = ''
  html += '<div>'
  for(var key in obj) {
    var val = obj[key]
    /*
console.log('key is:')
console.log(key)
console.log('obj is:')
console.log(obj)
    */
    html += '<div>'
      html += '<div>'
      html += key
      html += '</div>'
      html += '<div>'
      if(typeof(val) == 'object' && val !== null) {
        html += objToHtml(val, literal)
      }
      else if(Array.isArray(val)) {
        for(var i in val) {
          html += '<div>'
          html += val[i]
          html += '</div>'
        }
      }
      else {
          html += String(val)
      }
      html += '</div>'
    html += '</div>'
  }
  html += '</div>'
  return html
}


function tagToHtml(tag, literal=false) {
  var html = ''
  if(literal === true) html += '&lt;'
  else html += '<'
  html += tag.name
  html += '>'

  
  if(Array.isArray(tag.content)) {
    for(var i in tag.content) {
      html += tagToHtml(tag.content[i], literal)
    }
  }
  else if(tag.content === null) {
    html += '<i>[tag is empty]</i>'
  }
  else {
    html += tag.content
  }
 
  if(literal === true) html += '&lt;'
  else html += '<'
  html += '/'
  html += tag.name
  html += '>'
  return html
}

function textToHtml(text) {
  text = text.replace(/(?:\r\n|\r|\n)/g, '<br>')
  text = text.replace(/ /g,"&nbsp;")
  return text
}

