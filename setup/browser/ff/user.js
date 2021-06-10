// darktheme for webinspector:
user_pref("devtools.theme", "dark");
// allow installation of unsecure add-ons:
user_pref("xpinstall.signatures.required", false);
// make DuckDuckGo default search engine:
user_pref("browser.urlbar.placeholderName", "DuckDuckGo");
// allow add-on https://addons.mozilla.org/en-US/firefox/addon/hide-tab to hide tabs:
user_pref("extensions.webextensions.tabhide.enable", true);
// localhost when opening ff:
user_pref("browser.startup.homepage", "localhost:3000");
// no fluff for new tabs:
user_pref("browser.newtabpage.activity-stream.feeds.section.topstories", false);
user_pref("browser.newtabpage.activity-stream.feeds.topsites", false);
user_pref("browser.newtabpage.activity-stream.showSearch", false);
// dont show bookmarks beneath addressbar:
user_pref("browser.toolbars.bookmarks.visibility", "never");
