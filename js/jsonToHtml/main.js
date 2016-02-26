(function ($) {

function toggleKnot(knot) {
  $(knot).find('.pairs').toggle()
}

function jsonToHtml(obj) {
  // Take a json-obj and return it as nested html-divs,
  // according to the given structure.
  var html = '';
  var keys = [];
  for (var key in obj) {
    if (obj.hasOwnProperty(key)) {
      if ('object' == typeof(obj[key]) && obj[key] !== null) {
        html += '<div class="knot"><a href="#" class="toggleSyslings">+</a><div class="key">' + key +
          '</div><div class="pairs">' + jsonToHtml(obj[key]) + '</div></div>';
      }
      else { // val
        html += '<div class="pair"><div class="key">' + key +
          '</div><div class="val">' + obj[key] + '</div></div>';
      }
    }
  }
  return html;
};

function applyJsonsToHtmlEventListeners(jsons_container) {
  $(jsons_container).find('a').click(function(eve) {
    var knot = $(eve.target)
    if(knot.hasClass('toggleAll')) {
      //$(jsons_container).find('.pairs').hide()
      $(jsons_container).find('.pairs').show()
    }
    else {
      knot.find('~ .pairs').toggle()
    }
//alert('I')
  });
}


function jsonsToHtml(json_urls) {
  // Exe jsonToHtml for a list of urls
  // and prepend result to body.
  var json_url;
  var json_obj;
  var jsons_container;
  var html;
  var i;
  $('body').prepend('<div class="jsons"></div>')
  jsons_container = $('.jsons')[0]
  for(i=0; i < json_urls.length; i++) {
    json_url = json_urls[i]
    json_obj = $.getJSON(json_url, function(data) {
      html = jsonToHtml(data)
      $(jsons_container).append('<div class="json"><a href="#" class="toggleAll">+</a>' + html + '</div>')
      applyJsonsToHtmlEventListeners(jsons_container)
    });
  }
}


$(document).ready(function() {

  var json_urls = [
    //'https://pypi.python.org/pypi/adi.suite/json',
    //'https://pypi.python.org/pypi/Plone/json',
    'example.json',
  ]

  jsonsToHtml(json_urls)

}); /* doc.ready */ })(jQuery);

