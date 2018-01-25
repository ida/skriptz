function forEachEle(ele, doSth=null, eles=[]) {
  for(var j=0; j < ele.children.length; j++) {
    var child = ele.children[j]
    if(doSth !== null) doSth(child)
    eles.push(child)
    if(child.children.length > 0) {
      forEachEle(child, doSth, eles)
    }
  }
  return eles
}

function forEachNode(ele, doSth=null, nodes=[]) {
  for(var i=0; i < ele.childNodes.length; i++) {
    var child = ele.childNodes[i]
    if(doSth !== null) doSth(child)
    nodes.push(child)
    if(child.childNodes.length > 0) {
      forEachNode(child, doSth, nodes)
    }
  }
  return nodes
}

function forEachTextNode(ele, doSth=null, nodes=[]) {
  // Return all text-nodes of an ele, if `doSth` is passed
  // execute it upon each text-node.
  for(var i=0; i < ele.childNodes.length; i++) {
    var child = ele.childNodes[i]
    if(child instanceof Text) {
      if(doSth !== null) doSth(child)
      nodes.push(child)
    }
    if(child.childNodes.length > 0) {
      forEachTextNode(child, doSth, nodes)
    }
  }
  return nodes
}

function getPreviousNode(node) {
// Return previous sibling, or previous uncle, or null.
  if(node.previousSibling !== null) {
    node = node.previousSibling
  }
  else if(node.parentNode.previousSibling !== null) {
    node = node.parentNode.previousSibling
    while(node.childNodes.length > 0) {
      node = node.lastChild
    }
  }
  return node
}

function getPreviousTextNode(node) {
  node = getPreviousNode(node)
  while(node instanceof Element || node instanceof Comment) {
    node = getPreviousNode(node)
  }
  return node
}

function getNextNode(node) {
// Return next sibling, or next uncle, or null.

  // If node is an element and has children:
  if(node instanceof Element && node.childNodes.length > 0) {
    // The first child is our next node:
    node = node.firstChild
  }
  // If node is not an element or doesn't have children:
  else {
    // If node doesn't have a next sibling:
    if(node.nextSibling === null) {
      // Switch context to parent:
      node = node.parentNode
    }
    // Get next sibling:
    node = node.nextSibling
  }
  return node
}

function getNextTextNode(node) {
  var node = getNextNode(node)
  while(node instanceof Element || node instanceof Comment) {
    node = getNextNode(node)
  }
  return node
}

function walkNodes(node) {
  for(var i=0; i < node.childNodes.length; i++) {
    var child = node.childNodes[i]
    if(child instanceof Element) {    
    }
    else if(child instanceof Text) {
    }
    else {
      console.log('Neither text-, nor element-node, but:')
		  console.log(child.constructor.name)
    }
  }
}

