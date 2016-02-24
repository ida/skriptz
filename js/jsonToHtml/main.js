(function ($) {
function jsonToNestedHtmlDivs(obj) {
  // Take a json-obj and return it as nested html-divs,
  // according to the given structure.
  var html = '';
  var keys = [];
  for (var key in obj) {
    if (obj.hasOwnProperty(key)) {
      if ('object' == typeof(obj[key])) {
        if (jsonToNestedHtmlDivs(obj[key]) === '') {
          html += jsonToNestedHtmlDivs(obj[key]);
        }
        else {
          html += '<div class="nest">' + jsonToNestedHtmlDivs(obj[key]) + '</div>';
        }
      }
      else {
        html += '<div class="row"><div class="key">' + key +
          '</div><div class="val">' + obj[key] + '</div></div>';
      }
    }
  }
  return html;
};


$(document).ready(function() {

  var json_url = 'https://pypi.python.org/pypi/Plone/json'
  var json_obj = $.getJSON(json_url, function(data) {
    var html = jsonToNestedHtmlDivs(data)
    $('body').html(html)
  });

}); /* doc.ready */ })(jQuery);

