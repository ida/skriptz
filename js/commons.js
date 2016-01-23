//
// ELES
//
function addEle(parent_ele, ele_tag_name) {
  // Append and return an ele to the given parent.
  var ele = document.createElement(ele_tag_name)
  parent_ele.appendChild(ele)
  return ele
}
function getEle(ele) {
  // Passed ele can be obj or id-name or tag-name,
  // return ele-obj.
  if (typeof ele === 'string') {
    ele = document.getElementById(ele)
  }
  return ele
}
function getNextSibling(ele) {
  var next_ele=ele.nextSibling
  while (next_ele.nodeType!=1) {
    next_ele=next_ele.nextSibling
  }
  return next_ele
};
function getFirstChild(ele) {
  var first_child=ele.firstChild
  while (first_child.nodeType!=1) {
    first_child=getNextSibling(first_child)
  }
  return first_child
};
//
// STYLES
//
function getStyles(ele) {
  // Expects getEle().
  return window.getComputedStyle( getEle(ele) )
}
function getStyle(ele, prop) {
  // Expects getEle(), getStyles().
  return parseFloat( ( getStyles(ele) ).getPropertyValue(prop) )
}
function setStyles(ele, newstyles) {
  // Expects getEle().
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
  // Expects getEle().
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
  // Expects getCoords().
  return getCoords(ele)[0]
}
function getTop(ele) {
  // Expects getCoords().
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
  // Expects setUrlWithoutReload().
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
// CONVERSIONS
//
function jsonToNestedHtmlDivs(obj) {
  // Take a json-obj and return it as nested html-divs,
  // according to the given structure.
  var txt = '';
  var keys = [];
  for (var key in obj) {
    if (key !== 'histology') { // DEV escape this for now
      if (obj.hasOwnProperty(key)) {
        if ('object' == typeof(obj[key])) {
          if (jsonToNestedHtmlDivs(obj[key]) === '') {
            txt += jsonToNestedHtmlDivs(obj[key]);
          }
          else {
            txt += '<div class="nest">' + jsonToNestedHtmlDivs(obj[key]) + '</div>';
          }
        }
        else {
          txt += '<div class="row"><div class="key">' + key +
            '</div><div class="val">' + obj[key] + '</div></div>';
        }
      }
    }
  }
  return txt;
};
//
// ANIMATIONS
//
function addTextCharByCharAni(line_ele, line_text, interval_in_milliseconds, callbackFunction) {
/*  Insert text into an element in a ticker-like manner one char after the other
    and replace empty- or only-spaces-string with a linebreak. Example usage:
    var line_ele = document.getElementsByTagName('body')[0]
    var line_text = 'Some string to ticker.'
    var interval_in_milliseconds = 10
    tickerAllTextLinesAtOnce(ele, lines, interval_in_milliseconds) */
    var i = 0
    var charbychar_interval = setInterval(function () {
        // Remove trailing spaces:
        line_text = line_text.trim()
        // We have an empty string:
        if(line_text === '') {
            // Replace it with a linebreak,
            // so ele consumes height:
            line_ele.innerHTML = '<br>'
        }
        // If the text ends:
        if(i > line_text.length-1) {
            // End the interval:
            clearInterval(charbychar_interval)
            // Apply the callback-hook, if passed:
            if(callbackFunction) {
                callbackFunction()
            }
            // Break further executions:
            return
        }
        // Add char to line and increase iterator:
        var text_old = line_ele.innerHTML
        if(text_old === undefined) { text_old = '' }
        line_ele.innerHTML = text_old + line_text[i]
        i += 1
    }, interval_in_milliseconds);
}

function tickerAllTextLinesAtOnce(lines_ele, lines_text_list, interval_in_milliseconds) {
  /*
  Expects addEle() and addTextCharByCharAni(), example usage:
  var lines_ele = document.getElementsByTagName('body')[0]
  var lines_text_list = ['Hello,', '', 'some info.', '', 'Bye,' 'Anynone']
  var interval_in_milliseconds = 10
  tickerAllTextLinesAtOnce(lines_ele, lines_text_list, interval_in_milliseconds)
  */
  var i = 0
  while(i < lines_text_list.length) {
    var line_ele = addEle(lines_ele, 'div')
    var line_text = lines_text_list[i]
    addTextCharByCharAni(line_ele, lines_text_list[i], interval_in_milliseconds)
    i += 1
  }
}

function tickerTextLinesOneAfterTheOther(lines_ele, lines_text_list, interval_in_milliseconds) {
  /*
  Expects addEle() and addTextCharByCharAni(), example usage:
  var lines_ele = document.getElementsByTagName('body')[0]
  var lines_text_list = ['Hello,', '', 'some info.', '', 'Bye,' 'Anynone']
  var interval_in_milliseconds = 10
  tickerTextLinesOneAfterTheOther(lines_ele, lines_text_list, interval_in_milliseconds)
  */
  var i = 0
  var rekur = function() {
    if(i < lines_text_list.length){
      var line_ele = addEle(lines_ele, 'div')
      addTextCharByCharAni(line_ele, lines_text_list[i], interval_in_milliseconds, function() {
        i += 1
        rekur()
      });
    }
  }
  rekur()
}

