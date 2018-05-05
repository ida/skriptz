/* Requires './select/select_helpers.js' and './select/selection_changed.js'.

!!!
    This is a prototype for super-quick generation of depending select-eles.
    You probably want to use './dependent_field_actions.js', instead.
!!!


Dependent (select-)fields
=========================

Define field-chain-maps and generate fields of it (for now, only select-eles).
The maps define which value the next field in the chain should have, depending
on the current value of the field.


Usage
-----

// First define some values for the (select-)fields:

var field_one_value = ['dog', 'cat']
var field_two_value_for_dog = ['dependent', 'self-dirtying', 'submissive', 'attentive']
var field_two_value_for_cat = ['independent', 'self-cleaning', 'dominant', 'ignorant']
var field_three_value = ['good choice', 'bad choice']

//
// Then EITHER define maps manually:
//
var maps = [

  {
    dog: field_two_value_for_dog,
    cat: field_two_value_for_cat
  },

  {
    self-dirtying: ['bad choice'],
    self-cleaning: ['good choice'],
  }

]


// And add fields of maps to an ele (here: body-ele):
addSelectElesOfMaps(document.body, maps)


//
// OR, first auto-generate maps:
//
var fields_values = [field_one_value, field_two_value_for_dog, field_three_value]
var maps = genMaps(fields_values)

// That will set the same next-field-values for every case, meaning even if cat was
// was chosen, the next field shows 'field_two_value_for_dog'.

// Now, let's alter map of first field to show correct values in next field:
maps[0].cat = field_two_value_for_cat


// Finally add fields of maps to an ele:
addSelectElesOfMaps(document.body, maps)


*/

function addSelectEleOfMap(parentNode, map) {
  var values = getKeys(map)
  var ele = addSelectEle(parentNode, values)
  addSelectionChangedListener(ele, doAfterSelectionChanged)
  return ele
}
function addSelectElesOfMaps(parentNode, maps) {
  for(var i=0; i < maps.length; i++) {
    addSelectEleOfMap(parentNode, maps[i])
  }
}
function doAfterSelectionChanged(selectEle) {
  // Expects `maps` as glob-var.
  var pos = getPosInParent(selectEle)
  if(pos < maps.length-1) {
    var nextEle = selectEle.nextElementSibling
    var selectedIndex = 0
    var selectedValue = getSelectedValue(selectEle)
    var selectedValueNext = null
    var valuesNext = maps[pos][selectedValue]

    // Remember next selectedIndex, if next selected value exists in next values of map:
    if(nextEle !== null) {
      var selectedValueNextTemp = getSelectedValue(nextEle)
      if(valuesNext[selectedIndex] != selectedValueNextTemp && valuesNext.indexOf(selectedValueNextTemp) > 0) {
        selectedIndex = valuesNext.indexOf(selectedValueNextTemp)
      }
    }
    while(selectEle.nextElementSibling) selectEle.nextElementSibling.remove()
    selectEle = addSelectEle(parentNode, valuesNext, selectedIndex)
    addSelectionChangedListener(selectEle, doAfterSelectionChanged)
    doAfterSelectionChanged(selectEle)
  }
}
function genMaps(values){
  var maps = []
  for(var i in values) {
    var map = {}
    var options = values[i]
    for(var k in options) {
      var key = options[k]
      var optionsNext = [].concat(values[Number(i)+1])
      map[key] = optionsNext
    }
    maps.push(map)
  }
  return maps
}
function getKeys(obj) {
  var keys = []; for(var key in obj) keys.push(key); return keys
}
function getPosInParent(ele) {
  for(var i=0; i < ele.parentNode.children.length; i++) {
    if(ele.parentNode.children[i] == ele) return i
  }
  return null
}
function valuesDiffer(values1, values2) {
  for(var i=0; i < values1.length; i++) {
    if(values1[i] != values2[i]) return true
  }
  return false
}
