Add-ons
=======


Dark Reader
-----------

Toggle darkreader for all sites:     Alt+Shift+D

Toggle darkreader for current site:  Alt+Shift+A



Shortkeys
---------

After install there is always a JSON.parse-error in the webconsole!
The error disappears, when viewing controlpanel for the first time.

For that go to 'about:addons', click '...' at addon-entry,
select 'Manage', click '...', select 'Preferences'.

Do *not* go to 'about:addons', click gear symbol and select
'Manage Extensions Shortcuts'! Again: Do *NOT* do this!




Profiles
========


Copy data between profiles
---------------------------

Example passwords:

    cp old_profile/key4.db      new_profile

    cp old_profile/logins.json  new_profile


More examples:

https://support.mozilla.org/en-US/kb/recovering-important-data-from-an-old-profile#w_copying-files-between-profile-folders



Commandline
===========

This shows most of the available options:

    firefox -h | less

Here are some more:

    man firefox

That shows for example an option which opens the console in a new window centered in front of browser:

    firefox -jsconsole

This opens the inspector for firefox itself (see ./profile/chrome/userChrome.css):

    firefox --jsdebugger

However not all, here is more information:

    https://wiki.mozilla.org/Firefox/CommandLineOptions
    https://web.archive.org/web/20211101172958/https://wiki.mozilla.org/Firefox/CommandLineOptions


For example on how to create a new profile:

    firefox -CreateProfile AdaLovelace

Or how to create a profile in a (non-existing) specific directory:

    firefox -CreateProfile "AlanTuring /path/to/profile-directory"

