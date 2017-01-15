var bg = 'lightblue'
var fg = 'darkblue'
var hilite = 'darkblue'
var basic_styles = '\
body { margin: 0; font-family: sans; } /*DEV*/\n\
' + app + ' {\n\
    font-size: 27px;\n\
    line-height: 1.5em;\n\
}\n\
' + app + ' input {\n\
    border: 1px solid transparent;\n\
    border-radius: 50%;\n\
    color: transparent!important;\n\
    width: 1.5em;\n\
    height: 1.5em;\n\
}\n\
' + app + ' div {\n\
    display: inline-block;\n\
}\n\
' + app + ' div:focus {\n\
/*\
    outline: none;\n\
    background: ' + hilite + ';\n\
*/\
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
' + app + '-controls-controller > div:after {\n\
    position: absolute;\n\
    margin-left: -.75em;\n\
    display: none;\n\
    color: red;\n\
    background: yellow;\n\
}\n\
' + app + '-controls-controller > div:nth-child(1):after {\n\
    content: "7";\n\
}\n\
' + app + '-controls-controller > div:nth-child(2):after {\n\
    content: "8";\n\
}\n\
' + app + '-controls-controller > div:nth-child(3):after {\n\
    content: "9";\n\
}\n\
' + app + '-controls-controller > div:nth-child(4):after {\n\
    content: "4";\n\
}\n\
' + app + '-controls-controller > div:nth-child(5):after {\n\
    content: "5";\n\
}\n\
' + app + '-controls-controller > div:nth-child(6):after {\n\
    content: "6";\n\
}\n\
' + app + '-controls-controller > div:nth-child(7):after {\n\
    content: "1";\n\
}\n\
' + app + '-controls-controller > div:nth-child(8):after {\n\
    content: "2";\n\
}\n\
' + app + '-controls-controller > div:nth-child(9):after {\n\
    content: "3";\n\
}\n\
' + app + '-controls-controller-middle {\n\
    border-radius: 50%;\n\
}\n\
' + app + '-controls-controller:hover > div:after {\n\
    display: inline-block;\n\
}\n\
' + app + ' .buttons div,\n\
' + app + ' .button {\n\
    min-width: 1.5em; /* same as lineheight */\n\
    text-align: center;\n\
}\
' // Dont you – forget about me. 

function addPermanentStyles(styles) {
    $('head').prepend('<style type="text/css">' + styles + '</style>')
}
addPermanentStyles(basic_styles)
