function moveChildren(sourceEle, targetEle) {
  while(sourceEle.firstChild) targetEle.appendChild(sourceEle.firstChild)
}
