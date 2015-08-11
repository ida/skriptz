// Opens a prompt, where one can enter the URL of the script to be injected, must be served of an http(s)-prot.
// Serving locally with 'file:///', doesn't work, not relative to the watched document.
// If the html-docis watched locally ('file:///home/ida/test.html'), you can enter plain paths, relative to the doc, simply 'test.js', e.g.
javascript:(function(){
    var%20sUrl=prompt('Enter%20URL%20to%20JavaScript%20file');
    if(sUrl){
        var%20s=document.createElement('script');
        s.setAttribute('src',sUrl);
        document.getElementsByTagName('body')[0].appendChild(s);
        alert('Script%20injected!');
    }
})();
