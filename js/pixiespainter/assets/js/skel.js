function knotUp() {
    knot = '#' + $(knot).parent().attr('id')
}
function addEle(ele_id) {
    $(knot).append('<div id="'+ knot.slice(1) + '-' + ele_id + '"></div>')
    knot += '-' + ele_id
    return $(knot)
}
function addMarkupSkel() {
    var fg = 999
    var bg = fg/9
    $(knot).append('<div id="'+ app + '-container" style="background: #' + bg + '; color: #' + fg + ';"></div>')
    app = '#' + app + '-container'
    knot = app
    addEle('canvas')
    knotUp()
    addEle('controls')
}
addMarkupSkel()
