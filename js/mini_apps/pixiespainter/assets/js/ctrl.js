var disco_intervals = []

function addColorpicker() {
  // Requires jscolor.js:
  $(app + '-controls').append('<input class="color" title="Click to choose brush-color" />')
}
function addCounters() {
  addEle('counters')
      addCounter('size')
      addCounter('step')
      addCounter('radi')
  knotUp()
}
function addCounter(counter_id) {
  addEle(counter_id)
    addEle('lable').text(counter_id)
    knotUp()
    if(counter_id == 'size') {
      addEle('value').text('27')
      knotUp()
      addEle('unit').text('px')
    } else if (counter_id == 'step') {
      addEle('value').text('100')
      knotUp()
      addEle('unit').text('%')
    } else if (counter_id == 'radi') {
      addEle('value').text('50')
      knotUp()
      addEle('unit').text('%')
    }
    knotUp()
    addEle('counter').addClass('counter').addClass('buttons')
      addEle('rise').text('+')
      knotUp()
      addEle('fall').text('-')
      knotUp()
    knotUp()
  knotUp()
}
function addController() {
  // Wrapper (3x3 children and we have a first button (open/close controls) for getting the measure for now):
  addEle('controller').width(3 * $('.button').width()).addClass('buttons')
    // First row:
    addEle('upleft').text('\u2196')
      .attr('title', 'Click to move brush one dot up and left, or use key 7.')
    knotUp()
    addEle('up').text('\u25B2')
      .attr('title', 'Click to move brush one dot up, or use key 8.')
    knotUp()
    addEle('upright').text('\u2197')
      .attr('title', 'Click to move brush one dot up and right, or use key 9.')
    knotUp()
    // Second row:
    addEle('left').text('\u25C0')
      .attr('title', 'Click to move brush one dot left, or use key 4.')
    knotUp()
    addEle('middle').text('off')
      .attr('title', 'Click to turn brush on and off, or use key 5.')
    knotUp()
    addEle('right').text('\u25B6')
      .attr('title', 'Click to move brush one dot right, or use key 6.')
    knotUp()
    // Third row:
    addEle('downleft').text('\u2199')
      .attr('title', 'Click to move brush one dot down and left, or use key 1.')
    knotUp()
    addEle('down').text('\u25BC')
      .attr('title', 'Click to move brush one dot down, or use key 3.')
    knotUp()
    addEle('downright').text('\u2198')
      .attr('title', 'Click to move brush one dot down and right, or use key 3.')
    knotUp()    
  knotUp()
}
function addControls() {
  addControlsMin() 
  addController() 
  addColorpicker() 
  addCounters()
  addUndo()
  addDisco()
}
function addControlsListeners() { 
    // Controller arrow clicked: 
    $(app + '-controls-controller').click(function (eve) {
        // direction-val is last word of ele-id (seperated by minus), where ele is eve.target:
        var direction = eve.target.id.split('-')[eve.target.id.split('-').length-1]
        moveBrush(direction)
    });

    // Toggies clicked (switch visibility):
    $(app + ' .toggle').click(function() {
        $(this).toggle()
    });
    $(app + ' .toggleChildren').click(function() {
        $(this).find('> div').toggle()
    });
    $(app + ' .toggleSiblings').click(function() {
        $(this).siblings().toggle()
    });
    $(app + ' .toggleAunties').click(function() {
        $(this).parent().siblings().toggle()
    });

    // Counters:
    $(app + ' .counter div').click(function() {
      // Assume either a '+' or a '-' button was clicked:
        var counter_ele = $(this).parent().parent()
        counter_ele.css('border','1px solid lightgreen')
        var name_ele = counter_ele.find('> *:first-child')
        var value_ele = counter_ele.find('> *:nth-child(2)')
        //name_ele.css('border','1px solid red')
        var value = Number(value_ele.text())
        if($(this).text()=='+') {
            value += 1
        } else {
            value -= 1
        }
        value_ele.text(value)
        updateBrush(name_ele.text())
    });

  // Colorpicker:
  $(app + ' .color').change(function () {
    updateBrushColor(this.value)
  });

  // Undo:
  $(app + ' .undo').click(function () {
    // Remove last div, then give new last div cursor-id:
    var brushMode = getBrushMode()
    if(brushMode == 'on') {
      if($(app + '-canvas div').length > 1) {
        $(app + '-canvas :last-child').remove()
        $(app + '-canvas :last-child')
          .attr('id', (app + '-canvas-cursor').slice(1)) // slice removes '#'
      }
    } else if (brushMode == 'off') { // Delete 2nd-last div of canvas:
      $( $(app + '-canvas div')[$(app + '-canvas div').length - 2] ).remove()
    } else {
      console.debug('Could not retrieve brush-mode!')
    }
  });

  // Disco:
  $(app + ' .disco').click(function () {
    disco($(this))
  });
}    
function addControlsMin() {
  $('#paint-container-info-text').css({'position':'absolute', 'top':'127px'})
  addEle('header').css({'width':'100%'})
    addEle('info').addClass('button').addClass('toggleChildren').text('i')
    knotUp()
    addEle('toggler').addClass('button').addClass('toggleAunties').text('\u2261')
    knotUp()
  knotUp()
}
function addDisco() {
  $(app + '-controls').append('<div class="disco" tabindex="0">discoOn</div>')
}
function addUndo() {
  $(app + '-controls').append('<div class="undo" title="Click to undo last \
painted dot or use the Backspace-key">undo</div>')
}
function disco(disco_button) {
    var disco_text = disco_button.text()
    var kolors = ['green', 'yellow', 'orange', 'red', 'purple', 'blue']
    var kolors_i = -1
    if(disco_text == 'discoOn') {
      $(app + '-canvas div').each(function(index) {
        var dot = $(this)
        if(kolors_i < kolors.length - 1) { kolors_i += 1 }
        else { kolors_i = 0 }
        var kolor_i = kolors_i - 1
        var disco_interval = setInterval(function() {
          disco_intervals.push(disco_interval)
          if(kolor_i < kolors.length - 1) { kolor_i += 1 }
          else { kolor_i = 0 }
          dot.css('background', kolors[kolor_i])//.text(index).css('font-size', 9)
        }, 555);
      });
      disco_button.text('discoOff')
    }
    else if(disco_text == 'discoOff') {
      for(var interval in disco_intervals) {
          clearInterval(interval)
      }
      disco_button.text('discoOn')
    }
    else {
      console.error('Expected text of ele with class ".disco" to be \
"discoOn" or "discoOff", instead got: "' + $(this).text() + '".')
    }
}
(function ($) {
    addControls()
    addControlsListeners()
})(jQuery);
