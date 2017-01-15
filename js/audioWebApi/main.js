function playLoadedSound(buffer) {
  // Fix up prefixing
  window.AudioContext = window.AudioContext || window.webkitAudioContext;
  var context = new AudioContext();

  function playSound(buffer) {
    var source = context.createBufferSource(); // creates a sound source
    source.buffer = buffer;                    // tell the source which sound to play
    source.connect(context.destination);       // connect the source to the context's destination (the speakers)
    source.start(0);                           // play the source now
                                               // note: on older systems, may have to use deprecated noteOn(time);
  }
  playSound(buffer)
}
function loadSound(url) {
  var dogBarkingBuffer = null;
  // Fix up prefixing
  window.AudioContext = window.AudioContext || window.webkitAudioContext;
  var context = new AudioContext();

  function onError() {
    console.log('error')
  }
  function loadDogSound(url) {
    var request = new XMLHttpRequest();
    request.open('GET', url, true);
    request.responseType = 'arraybuffer';

    // Decode asynchronously
    request.onload = function() {
      context.decodeAudioData(request.response, function(buffer) {
        dogBarkingBuffer = buffer;
        playLoadedSound(dogBarkingBuffer)
      }, onError);
    }
    request.send();
  }
  loadDogSound(url)
  playLoadedSound(dogBarkingBuffer)
}
function startPlayLoop(file_url, delay_ms, start_ms=0, max_repeat=27) {
  while(max_repeat > 0) {
    setTimeout(function() {
      loadSound(file_url)
    }, start_ms)
    max_repeat -= 1
   // No increase would play all at once and boost volmune!
   start_ms += 1000 // *repeat // multiply with decreasing 'repeat', so interval between gets exponentially faster towards the end
  }
}
document.addEventListener("DOMContentLoaded", function(event) {
  var file_url = 'bark.ogg'
  var delay_ms = 1000
  startPlayLoop(file_url, delay_ms)
  var start_ms = delay_ms/2
  startPlayLoop(file_url, delay_ms, start_ms)
});
