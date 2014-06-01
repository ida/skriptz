//ele can be obj or id-name or tag-name
function getEle(ele) {
    if (typeof ele === 'string') {
        ele = document.getElementById(ele);
    }
    return ele;
};
function getStyles(ele) {
    return window.getComputedStyle( getEle(ele) );
};
function getStyle(ele, prop) {
    return parseFloat( ( getStyles(ele) ).getPropertyValue(prop) );
};
function setStyles(ele, newstyles) {
    ele = getEle(ele);
    styles = ele.getAttribute('style');
    if (styles==undefined) { styles = '' };
    ele.setAttribute('style', styles + newstyles);
};
function getCoords(ele) {
    ele = getEle(ele); 
    var left = ele.offsetLeft; 
    var topp = ele.offsetTop;
    while (ele=ele.offsetParent) {
        left += ele.offsetLeft;
        topp += ele.offsetTop;
    };
   return [left,topp];
};
function getLeft(ele) {
    return getCoords(ele)[0];
}
function getTop(ele) {
    return getCoords(ele)[1];
}
function getNextSibling(ele) {
    var next_ele=ele.nextSibling;
    while (next_ele.nodeType!=1) {
        next_ele=next_ele.nextSibling;
    }
    return next_ele;
};
function getFirstChild(ele) {
    var first_child=ele.firstChild;
    while (first_child.nodeType!=1) {
        first_child=getNextSibling(first_child);
    };
    return first_child;
};

