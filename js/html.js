function walkHtml(ele) {
  var chars = ele.innerHTML
  var inClosingTag = false
  var inOpeningTag = false
  var inTag = false
  for(var i=0; i < chars.length; i++) {
    var char = chars[i]
    if(chars[i] == '<') {
      inTag = true
      if(chars.length > i && chars[i+1] == '/') {
        inClosingTag = true        
      }
      else {
        inOpeningTag = true
      }
    }
    else if(chars[i] == '>' && inTag == true) {
      inTag = false
      if(inClosingTag == true) {
        inClosingTag = false
      }
      else if(inOpeningTag == true) {
        inOpeningTag = false
      }
    }
  }
} // walkHtml
