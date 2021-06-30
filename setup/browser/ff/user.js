// darktheme for webinspector:
user_pref("devtools.theme", "dark");
// show styles inherited from browser in webinspector:
user_pref("devtools.inspector.showUserAgentStyles", true);
// allow installation of unsecure add-ons:
user_pref("xpinstall.signatures.required", false);
// make DuckDuckGo default search engine:
user_pref("browser.urlbar.placeholderName", "DuckDuckGo");
// localhost when opening ff:
user_pref("browser.startup.homepage", "localhost:3000");
// no fluff in new tab-pages:
user_pref("browser.newtabpage.activity-stream.feeds.section.topstories", false);
user_pref("browser.newtabpage.activity-stream.feeds.topsites", false);
user_pref("browser.newtabpage.activity-stream.showSearch", false);
// dont show bookmarks beneath addressbar:
user_pref("browser.toolbars.bookmarks.visibility", "never");
// re-enable userChrome.css:
user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);
