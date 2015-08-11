javascript:( function(){
var success_info = 'jQuery successfully injected, ready to go wild :-)';
var ele = document.createElement("script");
ele.src = "jquery-1-11-1.min.js";
ele.src = "file:///home/ida/repos/skriptz/browsers/injects/bookmarks/jquery-1-11-1.min.js";
ele.src = "http://euve4703.vserver.de:8080/adi/static/shared/jq/jquery-1.11.2.js";
ele.type="text/javascript";
document.getElementsByTagName("head")[0].appendChild(ele);
console.log('jQuery-injection: If everything went right, you should see the message "' + success_info + '" on top of the page. Otherwise the script was probably not found.');
$('body').prepend('<div>jQuery injected :-)</div>');
$('body :first-child').css({'border-radius':'0.27','background':'lightgreen','padding':'0.77em'}).animate({opacity:0.27}, 2777, function() { $(this).remove() });
})();

