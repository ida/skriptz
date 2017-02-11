javascript:( function(){

    var saveToUrl = 'http://localhost:8080/Plone';

    var bookmarkId = Date.now();
    var bookmarkTitle = document.title;
    var bookmarkUrl = window.location.href;
    var bookmarkDesc = prompt('Description:');

    saveToUrl += '/portal_factory/Link/';
    saveToUrl += bookmarkId + '/edit?title=' + bookmarkTitle;
    saveToUrl += '&description=' + bookmarkDesc;
    saveToUrl += '&remoteUrl=' + bookmarkUrl + '&autosave';

    window.location.href = saveToUrl;

})();
