/*

addDependentFieldAction
=======================

What
----

Do something with an ele, if another ele changes its value and
differentiate what to do with the ele, depending on the current value
of the other ele.

Why
---

Not displaying unneeded information gives a better user-experience,
because the brain does not need to filter out irrelevant input.


How
---

Adds the properties 'dependentFields' and 'changeDependentFields' to
the ruling major-field. First is a map, holding the dependent-fields
and which actions are to be done, if major-field changes, second is
executing the actions of the map and is attached to the change-event
if the major-field.


Usage
-----

After adding this script to your doc, a func named 'addDependentFieldAction'
is available at your service. No other globs are introduced.

This directory should also contain an html-file of same name than this
script, which loads this script. You can open it in a browser and uncomment
the following lines, for live-testing. */

/* [remove this line for testing]

// Wait until all eles are present:
document.addEventListener('DOMContentLoaded', function() {

  // Assume two select-eles and an input-ele are present, where the first
  // ele has the options 'Plant', 'Animal' and 'Ghost':
  var anEle      = document.getElementsByTagName('select')[0]
  var anotherEle = document.getElementsByTagName('select')[1]
  var aTextEle   = document.getElementsByTagName('input')[0]

  // Now we can tell the other ele to change its options depending
  // on the value of the first ele, like this:
  addDependentFieldAction(anEle, anotherEle, 'Animal', ['Cat', 'Cow'])
  addDependentFieldAction(anEle, anotherEle, 'Plant',  ['Avocado', 'Cocoa'])

  // We can also pass a function, the other ele will be passed to it:
  addDependentFieldAction(anEle, anotherEle, 'Ghost',
                          function(ele) { ele.style.visibility = 'hidden' })

  // Make sure the other ele is always visible, when Ghost is not selected:
  function show(ele) { ele.style.visibility = 'visible' }
  addDependentFieldAction(anEle, anotherEle, 'Plant',  show)
  addDependentFieldAction(anEle, anotherEle, 'Animal', show)

  // If the dependent-field is not a select-ele, but a text-input, simply
  // pass a string instead of an array as the value to be set:
  addDependentFieldAction(anotherEle, aTextEle, 'Cat', 'Delicious with lemons')
  addDependentFieldAction(anotherEle, aTextEle, 'Cow', 'Perfect flat-pet')
  addDependentFieldAction(anotherEle, aTextEle, 'Avocado', 'Holy guacamoly')
  addDependentFieldAction(anotherEle, aTextEle, 'Cocoa', 'Plant of the gods')


}); // doc loaded

// [remove this line for testing] */

/*

Author
------

Ida Ebkes <contact@ida-ebkes.eu>, 2018.


License
-------

MIT

*/

function addDependentFieldAction(major, minor, majorValue, action) {
// major: A field-ele.
// minor: An ele to be manipulated when value in major changes.
// majorValue: The value in major when the minor-action should be done.
// action: A function which gets minor passed, or an array for option-values
//         to be set in minor, or a string if minor is a text-field.


  var majorValueToMinorActionsMap = null

  major.changeDependentFields = function(major) {
  // Get current value of major, look up and
  // do corresponding actions of minor-maps.

    for(var [minor, value] of major.dependentFields) {

      var actions = value[major.value]

      // If actions are not found, abort:
      if(actions === undefined) { return }

      for(var i=0; i < actions.length; i++) {
        var action = actions[i]

        // Action is a function, execute it and pass minor-field to it:
        if(action instanceof Function) {
          action(minor)
        }
        // Action is an array, insert it as option-eles in minor-field:
        else if(action instanceof Array) {
          var selectedValue = minor.value // remember selection
          minor.innerHTML = ''
          for(var j=0; j < action.length; j++) {
            var option = document.createElement('option')
            option.innerHTML = action[j]
            minor.appendChild(option)
          }
          minor.value = selectedValue // reset selection
        }
        // Action is a string, insert it as value in minor-field:
        else {
          minor.value = action
        }
      }
      // If minor is also a major of another minor, update minor, too:
      if(minor.dependentFields !== undefined) {
        minor.changeDependentFields(minor)
      }
    }
  } // EO changeDependentFields


  // Initially create dependentFields-map and attach change-listener:
  if(major.dependentFields === undefined) {
    major.dependentFields = new Map()
    major.onchange = function(eve) { major.changeDependentFields(major) }
  }

  // If it's the first action for the dependent-field, add and empty
  // object, representing the majorValueToMinorActionsMap:
  if(major.dependentFields.get(minor) === undefined) {
    major.dependentFields.set(minor, {})
  }

  // Get actions-map:
  majorValueToMinorActionsMap = major.dependentFields.get(minor)

  // If the majorValueToMinorActionsMap doesn't have an action for
  // the majorValue yet, add an empty array for the actions:
  if(majorValueToMinorActionsMap[majorValue] === undefined) {
    majorValueToMinorActionsMap[majorValue] = []
  }

  // Finally add action to actions-map:
  majorValueToMinorActionsMap[majorValue].push(action)

  // Lastly after changing actions-map, do the change-func:
  major.changeDependentFields(major)

} // EO addDependentFieldAction
