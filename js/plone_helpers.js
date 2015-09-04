function checkTinyMCELoaded() {
// Thanks to Luca Fabbri, a.k.a. 'keul, for kindly sharing this snippet on:
// http://stackoverflow.com/questions/32088348
    if (window.tinymce==undefined || !tinymce.editors.length) {
        setTimeout(checkTinyMCELoaded, 100)
        return
    }
    // doAfterTinyMCELoaded()
}
