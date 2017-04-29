//
// ANIME
//
function tickerText(text_ele, text, duration, doAfter=null) {
/*
Requires: 
Promises: Insert text into an element in a ticker-like manner,
          one char after the other.
Examples: var text_ele = document.getElementsByTagName('body')[0]
          var text = 'Some text to ticker'
          var duration = 10 // interval in milliseconds
          var doAfter = function() { console.debug('tickerText() ended')  }
          tickerText(text_ele, text, duration, doAfter)
*/
  var text_new = ''
  var i = 1

  text = text.trim() // remove trailing spaces

  // Show first char right ahead, don't wait for interval to start:
  if(text[0] !== undefined) { text_ele.innerHTML = text[0] }

  // Start interval:
  var interval = setInterval(function () {
    // If the text ends ...
    if(i >= text.length-1) {
      // ... end the interval ...
      clearInterval(interval)
      // and apply callback, if passed:
      if(doAfter) { doAfter() }
    }
    // Text didn't end, set new text:
    if(text[i] !== undefined) {
      text_ele.innerHTML = text_ele.innerHTML + text[i]
    }
    i += 1
  }, duration);
}
function tickerLinesSequentially(lines_ele, lines_text_list, duration) {
/*
Requires: ../commons.js: addEle(), tickerText()
Promises: Ticker one line after the other.
Examples: var lines_ele = document.getElementsByTagName('body')[0]
          var lines_text_list = ['Hello,', '', 'some info.', '', 'Bye,' 'Anynone']
          var duration = 10 // interval in milliseconds
          tickerLines(lines_ele, lines_text_list, duration)
*/
  var i = 0
  var loopLines = function() {
    if(i < lines_text_list.length){
      var text_ele = addEle(lines_ele, 'div')
      var text = lines_text_list[i]
      text = text.trim() // remove trailing spaces
      // Repeat this loop after it ended:
      var doAfter = function() { i += 1; loopLines() }
      // Make a little pause between each line-animation:
      setTimeout(
        function() {
          // Now, trigger ticker:
          tickerText(text_ele, text, duration, doAfter)
        },
        427
      );
    }
  }
  loopLines() // ini
}
function tickerLinesSimultaneouslyWithSameDuration(lines_ele, lines_text_list, duration) {
/*
Requires: ../commons.js: addEle(), tickerText()
Promises: Ticker lines, each starting at the same time,
          each consuming the same time to finish.
Examples: var lines_ele = document.getElementsByTagName('body')[0]
          var lines_text_list = ['Hello,', '', 'some info.', '', 'Bye,' 'Anynone']
          var duration = 10 // interval in milliseconds
          tickerLinesSimultaneously(lines_ele, lines_text_list, duration)
*/
  var text_ele;
  var line_text;
  var line_duration = 0
  var longest_line_length = 0
  var i = 0
  // Wait a moment, to have a blank state, do not show first chars immediately:
  setTimeout(function() {
    // First, eval longest line to make it the 100% of duration:
    while(i < lines_text_list.length) {
      line_text = lines_text_list[i]
      line_text = line_text.trim() // remove trailing spaces
      if(line_text.length > longest_line_length) {
        longest_line_length = line_text.length
      }
      i += 1
    }
    // Then, iterate again for ticking:
    i = 0
    while(i < lines_text_list.length) {
      text_ele = addEle(lines_ele, 'div')
      line_text = lines_text_list[i]
      line_text = line_text.trim() // remove trailing spaces
      if(line_text === '') { line_text = '&nbsp;' }
      // Compute duration:
      line_duration = longest_line_length/line_text.length*duration
      // Regard, if text is an empty string:
      if(line_text.length === 0) { line_duration = 0 }
      // Finally ticker:
      if(line_text !== '&nbsp;') {
        tickerText(text_ele, line_text, line_duration)
      }
      i += 1
    }
  }, 277);
}
