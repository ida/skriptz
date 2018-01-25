function removeSpaces(string) {
  string = string.trim()                // remove trailing spaces
  string = string.replace(/\n/g, '')    // remove line-breaks
  string = string.replace(/  /g, '')    // remove doubled spaces
  return string
}
