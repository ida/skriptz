function applyJsonsToHtmlEventListeners(jsons_container) {
  $(jsons_container).find('a').click(function(eve) {
    var knot = $(eve.target)
    if(knot.hasClass('showAllKnots')) {
        $(jsons_container).find('.pairs').show()
        $(jsons_container).find('.toggleSyslings').text('-')
        $(jsons_container).find('.toggleSyslings').attr('title', 'Hide knot')
    }
    else if(knot.hasClass('hideAllKnots')) {
        $(jsons_container).find('.pairs').hide()
        $(jsons_container).find('.toggleSyslings').text('+')
        $(jsons_container).find('.toggleSyslings').attr('title', 'Show knot')
    }
    else {
      if(knot.text() == '+') {
        knot.find('~ .pairs').show()
        knot.text('-')
        knot.attr('title', 'Hide knot')
      }
      else {
        knot.find('~ .pairs').hide()
        knot.text('+')
        knot.attr('title', 'Show knot')
      }
    }
  });
}


function jsonToHtml(obj) {
  // Take a json-obj and return it as nested html-divs,
  // according to the given structure.
  var html = '';
  for (var key in obj) {
    if (obj.hasOwnProperty(key)) {
      if ('object' == typeof(obj[key]) && obj[key] !== null) {
        html += '<div class="knot"><a title="Hide knot" class="toggleSyslings">-</a><div id="' +
          key + '" class="key">' + key +
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


function jsonsToHtml(json_urls) {
  $('body').prepend('<div class="jsons"><a title="Show all knots" class="showAllKnots">+</a><a title="Hide all knots" class="hideAllKnots">-</a></div>')
  var jsons_container = $('.jsons')[0]
  for(var i=0; i < json_urls.length; i++) {
    var json_url = json_urls[i]
    var json_obj = $.getJSON(json_url, function(data) {
      var html = jsonToHtml(data)
      $(jsons_container).append('<div class="json">' + html + '</div>')
      applyJsonsToHtmlEventListeners(jsons_container)
    });
  }
}


function getKeysOfJsonUrl(json_url) {
  var depth = 0;
  var keys = []
  var data = $.getJSON(json_url, function( data ) {
    function loop() {
      $.each( data, function( key, val ) {
        keys.push(key)
        if ('object' == typeof(val)) {
          for(var i=0; i < val.length; i++) {
          console.debug(val[i])
          }
          loop()
          depth += 1;
  console.debug(depth)
        }
      });
    }
  });

  return keys
}


function getKeysOfJsonUrls(json_urls) {
  var keys = []
  for(i=0; i < json_urls.length; i++) {
    keys = getKeysOfJsonUrl(json_urls[i])
  }
  return keys
}


function main() {
  var json_urls = [
  //'https://pypi.python.org/pypi/Plone/json',
  //'http://www.flickr.com/services/feeds/photos_public.gne?tags=soccer&format=json&jsoncallback=?',
  'example.json',
  ]
  jsonsToHtml(json_urls)
  var keys = getKeysOfJsonUrls(json_urls, keys)
//  console.debug(keys)
}


(function ($) {
  $(document).ready(function() {
    main()
  });
})(jQuery);
