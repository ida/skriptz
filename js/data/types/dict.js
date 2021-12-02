// Contains prettifyDict() and helper-funcs for it.

// But first a basic to remember:
function copyDict(dict) {
  return { ...dict }
}


/**
Evaluate longest key and prepend missing spaces to other keys
for better readability.<p>
For example this dict:</p><pre>
{ "a": 1, "bb": 2, "ccc": 3 }</pre><p>
Becomes:</p></pre>
{ "&nbsp; a": 1, " bb": 2, "ccc": 3 }</pre>
@param   {object} dict - Any object with key-value-pairs.
@returns {object} dict - The passed dict with longified keys.
*/
function longifyKeys(dict, space='&nbsp;') {
  let newDict = {}
  let longestKey = ''
  for(let key in dict) {
    if(key.length > longestKey.length) {
      longestKey = key
    }
  }
  for(let key in dict) {
    let newKey = space.repeat(longestKey.length - key.length + space.length)
               + key
    newDict[newKey] = dict[key]
  }
  return newDict
}

/**<p>Turn dict-like object into a human-readable string.</p>
For example passing this dict:<pre>{ "aKey": "aValue", "anotherKey": "anotherValue" }</pre>
Would return:<pre>"
        aKey: aValue
      
  anotherKey: anotherValue

"</pre>
  @param {object}       dict  - Any object with key-value-pairs.
  @param {string} [space=' '] - The string used to longify keys and indenting lines with two of them.
  @returns {string}
*/
function prettifyDict(dict, space=' ') {
  dict = longifyKeys(dict, space)
  dict = unclutterifyDict(dict)
  return dict
}
/** Return lines of dict-entries without separators
    but one colon between key and value.</p><pre>
For example passing this dict:<pre>
{ "aKey": "aValue", "anotherKey": "anotherValue" }</pre>
Returns this array:<pre>
["aKey: aValue", "anotherKey: anotherValue"]</pre>
*/
function unclutterifyDict(dict) {
  dict = JSON.stringify(dict).slice(1).split(',')
  let str = ''
  for(let i in dict) {
    let entry = dict[i]
    entry = entry.split('"')
    entry = entry[1] + ': ' + entry[3]
    entry = '\n' + entry + '\n'
    str += entry
  }
  return str
}
module.exports = {
  longifyKeys: longifyKeys,
  prettifyDict: prettifyDict,
  unclutterifyDict: unclutterifyDict
}
