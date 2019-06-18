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

  return lines

}


function getQuotations(string) {
//
// Parse string for quotations and return them.
//
// Example:
// Everything "quoted" in 'quotation marks' is
// regarded as a `quoted string` and collected.
//
// Returns:
// ['quoted', 'quotation marks', 'quoted string']
//
// A quotation must not contain quotation-marks of
// same kind than the surrounding quotation-marks.
//
// Otherwise it can contain anything, also multiple
// lines.
//
  const strings = []

  const quotationMarks = ['"', "'", '\`']

  let quotationMark = null

  let keyStartPos = null

  // For each character in string:
  for(var i=0; i < string.length; i++) {

    var chara = string[i]

    // Found quotation-mark:
    if(quotationMarks.includes(chara)) {

      // In case we have not remembered type of quotationMark, yet:
      if( ! quotationMark) {

        // Remember it:
        quotationMark = chara

        // Also remember current pos in string for collecting next quotation:
        keyStartPos = i
      }

      // In case we have already found a quotationMark before this one ...
      else {

        // ... and currently found quotationMark equals remembered quotationMark ...
        if(chara == quotationMark) {

          // ... collect string between starting quotationMark and ending quotationMark ...
          strings.push(string.slice(keyStartPos + 1, i)) // +1 is for omitting the quotationMark

          // ... and reset quotationMark for collecting the next quotation.
          quotationMark = null

        }
      }
    }
  }

  return strings

} // getQuotedStrings


function iniFileStringToObject(string) {
//
// Parse content of an INI-file and return
// an object of key-value-pairs.
//
// Our sufficient definition of an ini-file is:
//
// 1. A key always starts at the beginning of a line and
// ends with an equal-sign '=', thus a key must neither
// contain equal-signs nor line-breaks '\n'.
// Trailing spaces at the beginning of the line are
// tolerated and stripped of the extracted key-name.
//
// 2. A value always starts after the equal-sign which ends
// the key. It can contain equal-signs. It ends with the
// next linebreak, unless it starts with a quotation-mark
// ( '  or " or  ` ), then it ends with the next quotation-
// mark of same kind, and can spread over multiple lines.
// If the value is not quoted, trailing spaces are removed.
//
// Sections (lines in square-brackets) are not regarded.
// References: https://en.wikipedia.org/wiki/INI_file

  const iniObj = {}

  const quotationMarks = ['"', "'", '\`']

  let keyStartPos = 0

  let key, value = null

  string = String.raw`${string}`

  for(let pos=keyStartPos; pos < string.length; pos++) {

    // Found an equal-sign:
    if(string[pos] == '=') {

      // Extract key:
      key = string.slice(keyStartPos, pos)

      // Move behind equal-sign:
      pos += 1

      // If next character is a quote:
      if(quotationMarks.includes(string[pos])) {

        // Extract first found quotation:
        value = getQuotations(string.slice(pos))[0]

        // Regard quotationMarks for next char-position:
        pos += 2
      }

      // Otherwise extract rest of line:
      else {
        value = string.slice(pos).split('\n')[0]
      }

      // In both cases move behind value plus linebreak:
      pos += value.length + 1

      // Remember keyStartPos for next value:
      keyStartPos = pos

      // Finally collect extracted key and value:
      iniObj[key] = value

    } // found equal-sign

  } // each character

  return iniObj

} // iniFileStringToObject()

