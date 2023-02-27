const filesystem = require('fs')


function addFolder(path) {
  if(filesystem.existsSync(path) === false) {
    filesystem.mkdirSync(path);
  }
}
function addFolders(paths) {
  let path = ''
  for(let i in paths) {
    if(i != 0) path += '/'
    path += paths[i]
    createDirectory(path)
  }
}
function addParentFolders(filePath) {
  let parentPath = filePath.split('/')
  parentPath = parentPath.slice(0, parentPath.length-1)
  addFolders(parentPath)
}
function fileExists(filePath) {
  return filesystem.existsSync(filePath)
}
function getChildrenPaths(path='./') {
  let children = filesystem.readdirSync(path)
  return children
}
function getChildrensPaths(path='.', paths=[], MAX=9999) {
  if( ! path.endsWith('/') ) path += '/'
  if(paths.length==0) paths=[path]
  let children = getChildrensPaths(path)
  children.forEach(child => {
    let childPath = path + child
		if(isDirectory(childPath)) {
      childPath += '/'
			paths = getChildrensPaths(childPath, paths, MAX) // recur self
		}
    if(paths.length>MAX) return paths
    paths.push(childPath)
	});
  return paths
}
function isFolder(path) {
  return filesystem.statSync(path).isDirectory()
}
function readFile(filePath) {
  return filesystem.readFileSync(filePath, 'utf-8')
}
function readObjectOfFile(filePath) {
  let content = filesystem.readFileSync(filePath, 'utf-8')
  let object = JSON.parse(content)
  return object

}
function removeDirectory(filePath) {
  var files = []
  if( fs.existsSync(path) ) {
    files = fs.readdirSync(path)
    files.forEach(function(file,index){
      var curPath = path + "/" + file
      if(fs.lstatSync(curPath).isDirectory()) {
        removeDirectory(curPath)
      }
      else {
        fs.unlinkSync(curPath)
      }
    });
    fs.rmdirSync(path)
  }
}
function writeFile(filePath, string) {
  createParents(filePath)
  filesystem.writeFileSync(filePath, string)
  console.log('Wrote', filePath)
}
function writeObjectToFile(filePath, object) {
  writeFile(JSON.stringify(object))
}


module.exports.fileExists = fileExists
module.exports.getChildrenPaths = getChildrenPaths
module.exports.getChildrensPaths = getChildrensPaths
module.exports.isFolder = isFolder
module.exports.readFile = readFile
module.exports.readObjectOfFile = readObjectOfFile
module.exports.writeFile = writeFile
module.exports.writeObjectToFile = writeObjectToFile
