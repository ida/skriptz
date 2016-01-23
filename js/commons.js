//ele can be obj or id-name or tag-name
function getEle(ele) {
    if (typeof ele === 'string') {
        ele = document.getElementById(ele)
    }
    return ele
}
function getStyles(ele) {
    return window.getComputedStyle( getEle(ele) )
}
function getStyle(ele, prop) {
    return parseFloat( ( getStyles(ele) ).getPropertyValue(prop) )
}
function setStyles(ele, newstyles) {
    ele = getEle(ele)
    styles = ele.getAttribute('style')
    if (styles==undefined) { styles = '' }
    ele.setAttribute('style', styles + newstyles)
}
function getCoords(ele) {
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
    return getCoords(ele)[0]
}
function getTop(ele) {
    return getCoords(ele)[1]
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
function setBrowserUrlWithoutReload(url) {
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
    return(vals)
}
function changeUrlQuery(variable, values){
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
    setBrowserUrlWithoutReload(url + new_search)
}

function jsonToNestedHtmlDivs(obj) {
    // Takes a json-obj and returns it as
    // nested html-divs, according to the given structure.

    var txt = '';
    var keys = [];

    for (var key in obj) {
      if (key !== 'histology') { // DEV escape this for now
        if (obj.hasOwnProperty(key)) {
          if (!$scope.isInArray(key, keys)) { // prep collect keys, for next step to render columns
            keys.push(key);
          }
          if ('object' == typeof(obj[key])) {
            if ($scope.jsonToNestedHtmlDivs(obj[key]) === '') {
              txt += $scope.jsonToNestedHtmlDivs(obj[key]);
            }
            else {
              txt += '<div class="nest">' + $scope.jsonToNestedHtmlDivs(obj[key]) + '</div>';
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
function addTextCharByCharAni(ele, text, duration) {
    // Insert text into an element in a ticker-like manner.
    var i = 0
    var charbychar_interval = setInterval(function () {
        body.append(text[i])
        if(i > text.length-1) {
           clearInterval(charbychar_interval)
        }
        i += 1
    }, duration);
}

