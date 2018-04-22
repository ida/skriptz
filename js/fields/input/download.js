function addDownloadButton(containerEle, downloadContent, fileName='test.txt') {
// Append download-button to containerEle and download passed
// content when user clicks it. Example usage:
//    var containerEle = document.body
//    var downloadContent = document.body.innerHTML
//    addDownloadButton(containerEle, downloadContent)

  function provideFileExport(containerEle, downloadContent) {
    var exportButton = document.createElement('a')
    exportButton.id = 'download'
    exportButton.textContent = 'Download' + downloadFileName
    exportButton.setAttribute('download', downloadFileName)
    setContentToDownload(exportButton, downloadContent)
    containerEle.appendChild(exportButton)
  }
  function setContentToDownload(button, downloadContent) {
    button.href = 'data:application/octet-stream;charset=utf-8,'
                + encodeURIComponent(downloadContent)
  }
}
