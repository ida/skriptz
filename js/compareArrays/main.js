function genHtml(arr) {
  var html = '<div class="arr">'
  for(var key in arr) {
    html += '<div class="pair">'
    html += '<div class="key">'
    html += key
    html += '</div>'
    html += '<div class="val">'
    if(Array.isArray(arr[key])) {
      html += genHtml(arr[key])
    }
    else {
    }
    html += '</div>'
  }
  html += '</div>'
  return html
}
function parseArrayStructure(arr) {
  // Takes:
  // var arr = ['root', 'root-bro', ['root-child', 'root-child-sys'], 'root-sys']
  // Returns:
  // [0, 1, [0, 1], 3]
  var res = []
  var x = -1
  while(x < arr.length -1) {
    x += 1
    var val = arr[x]
    if(Array.isArray(val)) {
      res.push([x, parseArrayStructure(arr[x])])
    }
    else if(typeof(val) === 'object') {
console.debug('obj')
      //res.push([x, parseArrayStructure(arr[x])])
      for(var key in arr[x]) {
        res.push(key)
      }
    }
    else {
      res.push(x)
    }
  }
  return res
}
function main() {
  var arr1 = ['root', ['root-child', 'root-child-sys'], 'root-sys']
  var arr2 = ['root', 'root-bro', ['root-child', 'root-child-sys'], 'root-sys',
'root', 'root-bro', ['root-child', 'root-child-sys'], 'root-sys',
'root', 'root-bro', [{'root-child':'Edith', 'root-child-sys':'Ida'}], 'root-sys']
  var arr = parseArrayStructure(arr2)
  $('body').html(arr)
  console.debug(arr)
} /* main */ (function ($) { $(document).ready(function() { main() }); })(jQuery);
