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

function getNextSibling(ele) {
  var next_ele=ele.nextSibling
  while (next_ele.nodeType != 1) {
    next_ele=next_ele.nextSibling
  }
  return next_ele
};

function getFirstChild(ele) {
  var first_child=ele.firstChild
  while (first_child.nodeType != 1) {
    first_child=getNextSibling(first_child)
  }
  return first_child
};


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

function tickerText(text_ele, text, duration, doAfter=null) {
  /*
  Promises: Insert text into an element in a ticker-like manner,
            one char after the other.
  Requires: addEle(), tickerText()
  Examples: var text_ele = document.getElementsByTagName('body')[0]
            var text = 'Some text to ticker'
            var duration = 10 // interval in milliseconds
            var doAfter = function() { console.debug('tickerText() ended')  }
            tickerText(text_ele, text, duration, doAfter)
  */
  var text_new = ''
  var i = 1

  text = text.trim() // remove trailing spaces

  // Show first char right ahead, don't wait for interval to start:
  if(text[0] !== undefined) { text_ele.innerHTML = text[0] }

  // Start interval:
  var interval = setInterval(function () {
    // If the text ends ...
    if(i >= text.length-1) {
      // ... end the interval ...
      clearInterval(interval)
      // and apply callback, if passed:
      if(doAfter) { doAfter() }
    }
    // Text didn't end, set new text:
    if(text[i] !== undefined) {
      text_ele.innerHTML = text_ele.innerHTML + text[i]
    }
    i += 1
  }, duration);
}

function tickerLinesSequentially(lines_ele, lines_text_list, duration) {
/*
Requires: addEle(), tickerText()
Promises: Ticker one line after the other.
Examples: var lines_ele = document.getElementsByTagName('body')[0]
          var lines_text_list = ['Hello,', '', 'some info.', '', 'Bye,' 'Anynone']
          var duration = 10 // interval in milliseconds
          tickerLines(lines_ele, lines_text_list, duration)
*/
  var i = 0
  var loopLines = function() {
    if(i < lines_text_list.length){
      var text_ele = addEle(lines_ele, 'div')
      var text = lines_text_list[i]
      text = text.trim() // remove trailing spaces
      // Repeat this loop after it ended:
      var doAfter = function() { i += 1; loopLines() }
      // Make a little pause between each line-animation:
      setTimeout(
        function() {
          // Now, trigger ticker:
          tickerText(text_ele, text, duration, doAfter)
        },
        427
      );
    }
  }
  loopLines() // ini
}

function tickerLinesSimultaneouslyWithSameDuration(lines_ele, lines_text_list, duration) {
/*
Requires: addEle(), tickerText()
Promises: Ticker lines, each starting at the same time,
          each consuming the same time to finish.
Examples: var lines_ele = document.getElementsByTagName('body')[0]
          var lines_text_list = ['Hello,', '', 'some info.', '', 'Bye,' 'Anynone']
          var duration = 10 // interval in milliseconds
          tickerLinesSimultaneously(lines_ele, lines_text_list, duration)
*/
  var text_ele;
  var line_text;
  var line_duration = 0
  var longest_line_length = 0
  var i = 0
  // Wait a moment, to have a blank state, do not show first chars immediately:
  setTimeout(function() {
    // First, eval longest line to make it the 100% of duration:
    while(i < lines_text_list.length) {
      line_text = lines_text_list[i]
      line_text = line_text.trim() // remove trailing spaces
      if(line_text.length > longest_line_length) {
        longest_line_length = line_text.length
      }
      i += 1
    }
    // Then, iterate again for ticking:
    i = 0
    while(i < lines_text_list.length) {
      text_ele = addEle(lines_ele, 'div')
      line_text = lines_text_list[i]
      line_text = line_text.trim() // remove trailing spaces
      if(line_text === '') { line_text = '&nbsp;' }
      // Compute duration:
      line_duration = longest_line_length/line_text.length*duration
      // Regard, if text is an empty string:
      if(line_text.length === 0) { line_duration = 0 }
      // Finally ticker:
      if(line_text !== '&nbsp;') {
        tickerText(text_ele, line_text, line_duration)
      }
      i += 1
    }
  }, 277);
}

// EOF
