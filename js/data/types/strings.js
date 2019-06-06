function removeSpaces(string) {
  string = string.trim()                // remove trailing spaces
  string = string.replace(/\n/g, '')    // remove line-breaks
  string = string.replace(/  /g, '')    // remove doubled spaces
  return string
}


function toLines(string, lineLength=60) {
  let line = ''
  let linebreakPos = null
  let lines = []

  while(string.length > 0) {

    // Add character to line:
    line += string[0]

    // Remember last occuring space:
    if(string[0] == ' ' || string[0] == '\n') {
      linebreakPos = line.length-1
    }

    // Remove character of string:
    string = string.slice(1)

    // When line breaks:
    if(line.length > lineLength) {

      // Collect line until breakpoint:
      lines.push(line.slice(0, linebreakPos))

      // Keep rest of line for next line:
      line = line.slice(linebreakPos)

    }

  }
  // Collect last line:
  lines.push(line)
  console.debug(lines)
  return lines
}
