
function load(url, from, to) {
    var cached=sessionStorage[url];
    if(!from){from="body";} // default to grabbing body tag
    if(to && to.split){to=document.querySelector(to);} // a string TO turns into an element
    if(!to){to=document.querySelector(from);} // default re-using the source elm as the target elm
//    if(cached){return to.innerHTML=cached;} // cache responses for instant re-use

    var XHRt = new XMLHttpRequest; // new ajax
    XHRt.responseType='document';  // ajax2 context and onload() event
    XHRt.onload= function() { sessionStorage[url]=to.innerHTML= XHRt.response.querySelector(from).innerHTML;};
    XHRt.open("GET", url, true);
    XHRt.send();
    return XHRt;
}
function main() {
}


/*
*/
main()
setTimeout(function(){window.location.href=window.location.href},
7000)
