function knotUp() {
    knot = '#' + $(knot).parent().attr('id')
}
function addEle(ele_id) {
    $(knot).append('<div id="'+ knot.slice(1) + '-' + ele_id + '"></div>')
    knot += '-' + ele_id
    return $(knot)
}
function addMarkupSkel() {
    $(knot).append('<div id="'+ app + '-container"></div>')
    app = '#' + app + '-container'
    knot = app
    addEle('canvas')
    knotUp()
    addEle('controls')
}
addMarkupSkel()
