function addSelectionChangedListener(selectionEle, onChangeDoWithEle) {
//
// What
// ====
// When the selected value of a selection-element has changed after a
// click or typing arrow-up/down, execute callback 'onChangeDoWithEle'
// upon the element.
//
//
// Usage
// =====
//
// Insert this script in your doc, and of one of your script define
// what you want to do after a selection changed:
//
//    function mySelectionChangedHandler(selectionEle) {
//      console.log('Selection of ' + selectionEle + ' changed.')
//    }
//
// Choose the selection-ele you want to apply the listener at:
//
//    var selectionEle = document.getElementsByTagName('selection')[0]
//
// And execute this function with those two params passed:
//
//    addSelectionChangedListener(selectionEle, mySelectionChangedHandler)
//
// You could loop all found selection-elements after doc loaded, but you
// might also just apply the listener right after creating selection-eles in
// your scripts.
//
//
// Why
// ===
//
// Problem:
// Changing selected option via the up- or down-arrow are not
// firing a change-event in most browsers.
//
// Solution:
// Define here on which events the callback 'onChangeDoWithEle'
// should happen, if the selection changed. We want the click-event
// and the keyup-event of arrow-up or -down.
//
// Next problem:
// When listening to keyup-event of arrows, we cannot know if the
// selection changed, because the browser doesn't change the selection.
//
// Solution:
// Listen also on keydown-event of arrows and store the current selection,
// so the keyup-handler has this information available when needed.
//
// Next problem:
// When listening to click-event, we cannot know if the selection changed,
// because there's no way to get the selection before the click happened.
//
// Solution:
// The native change-event covers that case, listen to it and execute the
// callback, when fired.
//
// Next problem:
// The native change-event is also fired on the blur-event. We don't want
// that because the reasons for a changed selection before a blur-event
// could only be a changement via the arrow-keys, and as that case is already
// covered here, the callback had been fired already.
//
// Solution:
// Listen only for change-events caused by by a click, which is the case if
// the triggering ele is an option-ele, unlike with the blur-event where
// the triggering ele is the selection-ele.
//
// Problem that also got solved with the last solution above:
// The native change-event is also fired of some browsers, when arrow-keys are
// the cause of the change.
//
// Solution:
// Narrow change-event-listening down to those caused by click-events, only.

  var selectedIndex = null

  selectionEle.onkeydown = function(eve) {              // a key was pressed
    selectedIndex = eve.target.selectedIndex           //  remember selection
  }

  // onImmediateChange
  //  Listen to native change-event deriving of click,
  //  and if user types anything and selection changed:

  selectionEle.onkeyup = function(eve) {             //    a key was released
    if(selectedIndex != eve.target.selectedIndex) { //     selection changed
      onChangeDoWithEle(eve.target)                //      call passed func
    }
  }
  selectionEle.onchange = function(eve) {       // an option was clicked
    if(eve.explicitOriginalTarget.tagName.toLowerCase() == 'option') {
      onChangeDoWithEle(eve.target)           //   call passed func
    }
  }
/*

  // onConfirmedChange
  //  Listen to native change-event,
  //  and if user types Enter and selection changed:

  selectionEle.onchange = function(eve) {
    onChangeDoWithEle(eve.target)
  }
  selectionEle.onkeyup = function(eve) {
    if(eve.keyCode == 13 && eve.target.selectedIndex != selectedIndex) {
      onChangeDoWithEle(eve.target)
    }
  }
*/


} // EO addSelectionChangedListener
