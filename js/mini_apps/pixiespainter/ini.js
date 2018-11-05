var app = 'paint';
var knot = 'body';
(function ($) {

  function addAppScripts() {
    var file_path= null
    var srcs_path = 'assets/js/'
    var srcs = [
      'skel.js',
      'styl.js',
      'ctrl.js',
      'keys.js',
      'brush.js',
    ]
    for(var i=0; i < srcs.length; i++) {
      file_path = srcs_path + srcs[i]
      $('head').append('<script type="text/javascript" src="' + file_path + '"></script>')
    } 
  }
  $(document).ready(function() {
    addAppScripts()

    // Set brush-color to 'red':
    $(app + '-controls .color').val('ff0800')
    // Apply brush-color to brush:
    $(app + '-canvas-cursor').css('background', '#ff0800')
    // Set brush-mode to 'on':
    $(app + '-controls-controller-middle').click()
    // Focus app, so user can go right ahead to make key-inputs:
    $(app).focus()


    // On info-button-click:
    $('#paint-container-controls-header-info').click(function() {
      if( $(this).text() == 'i' ) {
        $(this).html(' x&nbsp;   Hi, this is pixiespainter, for more info click here:' + 
        '<a href="README.txt" title="More info about this app">README</a>.')
      }
      else {
        $(this).text('i')
      }
    });

  });//docready
})(jQuery);
