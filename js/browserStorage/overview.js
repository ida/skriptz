function getStorageKeys(storageType) {
// Return all available keys of a storage.
  if(isValidStorageType(storageType)) {
    var keys = []
    if(storageType == 'local') {
      for(var i=0; i < localStorage.length; i++) {
        keys.push(localStorage.key(i))
      }
    }
    else if(storageType == 'session') {
      for(var i=0; i < sessionStorage.length; i++) {
        keys.push(sessionStorage.key(i))
      }
    }
    return keys
  } // isValidStorageType
}
function showStorage(containerEle, storageType, showColumnHeaders=false, showRowNrs=false) {
// Visualize storage as an html-list, containing key- and value-pairs,
// append it into the containerEle. Optionally also show column-headers
// and row-numbering.

  if(isValidStorageType(storageType)) {

    var html = ''
    var keys = getStorageKeys(storageType)

    // Add a header:
    html += '<h2>'
      html += storageType + 'Storage'
    html += '</h2>'

    // Storage is empty:
    if(keys.length < 1) {
      html += 'Apparently nothing\'s in your ' + storageType + 'Storage.'
    }
    // Storage is not empty:
    else {
      // Add column-headers, if wished:
      if(showColumnHeaders) {
        html += '<' + htmlListType + '>'
          // Include numbering, if wished:
          if(showRowNrs) {
            html += '<li>'
              html += '<em>'
                html += 'Number' 
              html += '</em>'
            html += '</li>'
          } // showRowNrs
          html += '<li>'
            html += '<em>'
              html += 'Key'
            html += '</em>'
          html += '</li>'
          html += '<li>'
            html += '<em>'
              html += 'Value'
            html += '</em>'
          html += '</li>'
        html += '</' + htmlListType + '>'
      } // showColumnHeaders

      // For each key:
      for(var i=0; i < keys.length; i++) {

        // Start list:
        html += '<' + htmlListType + '>'

        // Include numbering, if wished:
        if(showRowNrs) {
          html += '<li>'
            html += i + 1 // Start with 1, not with 0.
          html += '</li>'
        }

        // Add key:
        html += '<li tabindex=0>'
        html += keys[i]
        html += '</li>'

        // Get and add the key's value:
        html += '<li>'
        if(storageType == 'local') {
          html += localStorage.getItem(keys[i])
        }
        else if (storageType == 'session') {
          html += sessionStorage.getItem(keys[i])
        }
        html += '</li>'

        // End list:
        html += '</' + htmlListType + '>'
      }
    } // storage is not empty
    // Insert html to container:
    containerEle.innerHTML = html
  }
}
function showStorages(storagesContainer, showColumnHeaders=true, showRowNrs=true) {

  // Add a header:
  storagesContainer.innerHTML = "<h1>Your browser's storages</h1>"

  // Create ele for localStorage and insert results:
  var localStorageContainer = document.createElement('div')
  storagesContainer.appendChild(localStorageContainer)
  showStorage(localStorageContainer, 'local', showColumnHeaders, showRowNrs)

  // Create ele for sessionStorage and insert results:
  var sessionStorageContainer = document.createElement('div')
  storagesContainer.appendChild(sessionStorageContainer, showRowNrs)
  showStorage(sessionStorageContainer, 'session', showColumnHeaders, showRowNrs)
}
function isValidStorageType(storageType, msgEle=document.body) {
// Return true, if storageType is 'local' or 'session'. Otherwise
// break with err-msg on screen and return false.
  var msg = 'Error: "' + storageType + '" is not a valid storageType. \
It should be either "local" or "session".'
  if(storageType != 'local' && storageType != 'session') {
    msgEle.innerHTML = msg; return false } else { return true }
}
