function onFileSelect(evt) {
  var files = evt.target.files
  for(i in files) {
    var f = files[i]
      var reader = new FileReader()
      reader.onload = function(e) {
        var contents = e.target.result
        keys = setTable(contents)
        showTable(keys)
      }
      reader.readAsText(f)
  }
}
document.addEventListener("DOMContentLoaded", function(event) {
console.debug(keys)
  var ele = document.createElement('div')
  document.body.appendChild(ele)
  var input = document.createElement('input')
	input.type = 'file'
	input.id = 'files'
  ele.appendChild(input)
  input.onchange = function(eve) {
		onFileSelect(eve)
  }
});
