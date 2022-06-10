// Switch display of topbar with F11.
// Similar to fullscreen, but window-size remains.
user_pref("full-screen-api.ignore-widgets", true);

// make DuckDuckGo default search engine: !!! this does not take effect, not event if we bam it right into profile/prefs.js !!!
user_pref("browser.urlbar.placeholderName", "DuckDuckGo");


// darktheme for webinspector:
user_pref("devtools.theme", "dark");
// show styles inherited from browser in webinspector:
user_pref("devtools.inspector.showUserAgentStyles", true);
// allow installation of unsecure add-ons:
user_pref("xpinstall.signatures.required", false);
// localhost in new window:
user_pref("browser.startup.homepage", "localhost:3000");
// no fluff in new tabs:
user_pref("browser.newtabpage.activity-stream.feeds.section.topstories", false);
user_pref("browser.newtabpage.activity-stream.feeds.topsites", false);
user_pref("browser.newtabpage.activity-stream.showSearch", false);
// dont show bookmarks beneath addressbar:
user_pref("browser.toolbars.bookmarks.visibility", "never");

// Enable styling firefox itself in profile/chrome/userChrome.css:
user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);
// Enable debugging firefox itself with Ctrl+Alt+Shift+I :
user_pref("devtools.chrome.enabled", true);
user_pref("devtools.debugger.remote-enabled", true);
