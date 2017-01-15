function addColorpicker() {
    // Requires jscolor.js:
    $(app + '-controls').append('<input class="color" />')
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
        addEle('value').text('27')
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
        knotUp()
        addEle('up').text('\u25B2')
        knotUp()
        addEle('upright').text('\u2197')
        knotUp()
        // Second row:
        addEle('left').text('\u25C0')
        knotUp()
        addEle('middle').text('off')
        knotUp()
        addEle('right').text('\u25B6')
        knotUp()
        // Third row:
        addEle('downleft').text('\u2199')
        knotUp()
        addEle('down').text('\u25BC')
        knotUp()
        addEle('downright').text('\u2198')
        knotUp()    
    knotUp()
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
(function ($) {
    addControlsMin() 
    addColorpicker() 
    addController() 
    addCounters()
    
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
        
        var val_ele = $(this).parent().parent().find('> :nth-child(2)')
        var val = Number(val_ele.text())
        if($(this).text()=='+') {
            val += 1
        }
        else {
            val -= 1
        }
        
        val_ele.text(val)
        updateBrush('size')
    });

    // Colorpicker:
    $(app+ ' .color').change(function () {
       updateBrushColor(this.value)
    });
    
})(jQuery);
