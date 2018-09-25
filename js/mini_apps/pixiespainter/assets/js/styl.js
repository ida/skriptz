var bg = '#fff'
var fg = '#111'
var basic_styles = '\
body { margin: 0; font-family: sans; } /*DEV*/\n\
' + app + ' {\n\
    background: ' + bg + ';\n\
    color: ' + fg + ';\n\
    line-height: 1.5em;\n\
}\n\
' + app + ' input.color {\n\
    border: 1px solid transparent;\n\
    border-radius: 50%;\n\
    color: transparent!important;\n\
    width: 1.5em;\n\
    height: 1.5em;\n\
    margin: 0 0.75em;\n\
}\n\
' + app + ' div {\n\
    display: inline-block;\n\
}\n\
' + app + '-canvas {\n\
    width: 100%;\n\
    height: 100%;\n\
}\n\
' + app + '-canvas div {/*cursor*/\n\
    position: absolute;\n\
}\n\
' + app + '-controls {\n\
    background: ' + fg + ';\n\
    background: #172A46;\n\
    color: ' + bg + ';\n\
    position: absolute;\n\
    right: 0;\n\
    left: 0;\n\
    bottom: 0;\n\
}\n\
' + app + '-controls-header {\n\
    background: #333;\n\
}\n\
' + app + '-controls-header-toggler {\n\
    float: right;\n\
    vertical-align: top;\n\
}\n\
' + app + '-controls-counters > div {\n\
    margin-right: 0.75em;\n\
}\n\
' + app + ' .buttons div,\n\
' + app + ' .button {\n\
    min-width: 1.5em; /* same as lineheight */\n\
    text-align: center;\n\
}\
' + app + ' .undo {\n\
    margin-right: 0.75em;\n\
}\n\
' // Dont you – forget about me. The closing apo.

function addPermanentStyles(styles) {
    $('head').prepend('<style type="text/css">' + styles + '</style>')
}
addPermanentStyles(basic_styles)
