//
// FUNCS
//
function getThisFuncName(argumentsCallee) {
  // Execute this func of within any function and pass
  // arguments.callee to it, like this:
  //     getThisFuncName(arguments.callee)
  // Returns empty str, if func is anonymous.
  // Not IE compatible.
  var funcName = argumentsCallee.toString()
  funcName = funcName.substr('function '.length)
  funcName = funcName.substr(0, funcName.indexOf('('))
  return funcName
}
//
// ELES
//

function addEle(parent_ele, ele_tag_name, ele_text='') {
/*
Promises: Add ele to parent, set a min-height, insert text if passed.
Requires: getStyle()
Examples: addEle(some_ele, 'div', 'blabla')
          addEle(some_ele, 'span')
*/
  var ele = document.createElement(ele_tag_name)
  ele.innerHTML = ele_text
  ele.setAttribute('style', 'min-height: ' + getStyle(parent_ele, 'line-height'))
  parent_ele.appendChild(ele)
  return ele
}
function getEle(ele) {
// Promises: Passed 'ele' can be obj or id-name or tag-name, return ele-obj.
  if (typeof ele === 'string') {
    ele = document.getElementById(ele)
  }
  return ele
}
function getFirstChild(ele) {
  var first_child = null
  if(ele.firstChild !== null) {
    first_child = ele.firstChild
    while (first_child.nodeType != 1) {
      first_child = getNextSibling(first_child)
    }
  }
  return first_child
}
function getFirstChildren(ele) {
  var eles = null
  var ele = getFirstChild(ele)
  if(ele !== null) {
    eles = [ele]
    while(getNextSibling(ele) !== null) {
      ele = getNextSibling(ele)
      eles.push(ele)
    }
  }
  return eles
}
function getNextSibling(ele) {
  var next_ele = null
  if(ele.nextSibling !== null) {
    var next_ele = ele.nextSibling
    while (next_ele.nodeType != 1) {
      next_ele=next_ele.nextSibling
    }
  }
  return next_ele
}
function hasClass(ele, klassName) {
  return (' ' + ele.className + ' ').indexOf(' ' + klassName + ' ') > -1
}
//
// STYLES
//
function getStyles(ele) {
// Requires: getEle()
  return window.getComputedStyle( getEle(ele) )
}
function getStyle(ele, prop) {
// Requires: getEle(), getStyles()
  return parseFloat( ( getStyles(ele) ).getPropertyValue(prop) )
}

function setStyles(ele, newstyles) {
// Requires: getEle()
  ele = getEle(ele)
  styles = ele.getAttribute('style')
  if (styles==undefined) { styles = '' }
  ele.setAttribute('style', styles + newstyles)
  // TODO: Instead of simply appending new styles, check if a property
  // was defined already, and replace it with the new one.
}
//
// POSITIONS
//
function getCoords(ele) {
// Requires: getEle()
  ele = getEle(ele)
  var left = ele.offsetLeft
  var topp = ele.offsetTop
  while (ele=ele.offsetParent) {
      left += ele.offsetLeft
      topp += ele.offsetTop
  }
 return [left, topp]
}
function getLeft(ele) {
  // Requires: getCoords()
  return getCoords(ele)[0]
}
function getTop(ele) {
  // Requires: getCoords()
  return getCoords(ele)[1]
}
//
// BROWSER-URL
//
function setUrlWithoutReload(url) {
  window.history.pushState(null, '', url)
}

function getUrlQueryVarVals(variable) {
  var vals = []
  var query = window.location.search.substring(1)
  var vars = query.split("&")
  for (var i=0;i<vars.length;i++) {
    var pair = vars[i].split("=")
    if(pair[0] == variable) {
      vals.push(pair[1])
    }
  }
  return vals
}
function changeUrlQuery(variable, values){
// Requires: setUrlWithoutReload()
  var new_search = '?'
  // Get current search and remove questionmark of beginning:
  var search_string = window.location.search.substring(1)
  // Remove former var and its val(s) of current search:
  if(search_string.indexOf(variable) != -1) {
    // We have multiple paras:
    if(search_string.indexOf('&') != -1) {
      var searches = search_string.split('&')
      for(var i=0;i<searches.length;i++) {
        if(searches[i].split('=')[0] != variable) {
          if(new_search != '?') {
            new_search += '&'
          }
          new_search += searches[i]
        }
      }
    }
    // Just one para:
    else {
      if(search_string.split('=')[0] != variable) {
        new_search += search_string
      }
    }
  }
  // The passed var isn't present, keep complete old search:
  else {
    new_search += search_string
  }
  // Now, add new paras, we can have a list of vals, here:
  if(Array.isArray(values)) {
    for(var j=0;j<values.length;j++) {
      if(new_search != '?') {
        new_search += '&'
      }
      new_search += variable + '=' + values[j]
    }
  }
  // Or just one val:
  else {
    if(new_search != '?') {
      new_search += '&'
    }
    new_search += variable + '=' + values
  }
  // Get current url without search-query:
  var url = String(window.location).split('?')[0]
  // Set new query:
  setUrlWithoutReload(url + new_search)
}
//
// CONVERSE
//
function decodeUrl(url) {
// http%3A%2F%2Fwebarchive.org%23content ---> http://webarchive.org#content
  return decodeURIComponent(url.replace(/\+/g,  " "))
}
function encodeUrl(url) {
// http://webarchive.org#content ---> http%3A%2F%2Fwebarchive.org%23content
  return encodeURIComponent(url).replace(/'/g,"%27").replace(/"/g,"%22")
}
function jsonToNestedHtmlDivs(obj) {
  // Take a json-obj and return it as nested html-divs,
  // according to the given structure.
  var txt = ''
  var keys = [];
  for (var key in obj) {
    if (obj.hasOwnProperty(key)) {
      if ('object' == typeof(obj[key])) {
        if (jsonToNestedHtmlDivs(obj[key]) === '') {
          txt += jsonToNestedHtmlDivs(obj[key])
        }
        else {
          txt += '<div class="nest">' + 
            jsonToNestedHtmlDivs(obj[key]) + '</div>'
        }
      }
      else {
        txt += '<div class="row"><div class="key">' + key +
          '</div><div class="val">' + obj[key] + '</div></div>'
      }
    }
  }
  return txt
}
//
// LOAD
//
function loadUrlAndInsertResponseToEle(url, ele=document.body) {
  var request = new XMLHttpRequest();
  request.open('GET', url, true);
  request.onload = function() {
    if (request.status >= 200 && request.status < 400) {
      ele.innerHTML = request.responseText
    }
    else {
      console.error("Couldn't load HTML from '" + url + "'.")
    }
  }
  request.onerror = function() {
    console.error("Cannot get a connection to '" + url + "'.")
  }
  request.send()
}
// EOF
