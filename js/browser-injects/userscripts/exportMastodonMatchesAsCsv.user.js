// ==UserScript==
// @id             exportMastodonMatchesAsCsv
// @name           Export mastodon-matches as CSV
// @version        1.0
// @namespace      adi
// @author         Ida Ebkes
// @description    Appends a download-button to "bridge.join.mastodon" for exporting matching mastodon-users as a CSV-file.
// @include        https://bridge.joinmastodon.org/friends
// @run-at         document-end
// ==/UserScript==

// Collect user-urls:
var userUrls = []
var userEles = document.getElementsByClassName('mastodon')
for(var i=0; i < userEles.length; i++) {
  var userUrl = userEles[i].getElementsByTagName('a')[0]
  if(userUrl !== undefined) userUrls.push(userUrl.innerHTML)
}

// Convert to csv:
var csv = userUrls.join('\n') 

// Add button:
var downloadButton = document.createElement('a')
downloadButton.innerHTML = 'Download all matching Mastodon-users as CSV-file.'
downloadButton.setAttribute('download', 'mastodon_users.csv')
downloadButton.href = 'data:application/csv; charset=utf-8,'
                     + encodeURIComponent(csv)
document.body.appendChild(downloadButton)

