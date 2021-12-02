Create an extension (add-on) for Firefox
========================================


1. Create a directory and in it add a file named 'manifest.json' with this content:

    {

      "manifest_version": 2,
      "name": "sharpcuts",
      "version": "0.1",

      "content_scripts": [
        {
          "matches": ["*://*/*"],
          "js": ["main.js"]
        }
      ],


      "browser_specific_settings": {
        "gecko": {
          "id": "some-name@example.org"
        }
      }

    }


This injects a script named "main.js", which is expected to be in the directory, too,
and is the place where you can add your scripting magic, for whatever you're up to do.



2. From within the extension directory, do:

    zip -r -FS ../sharpcuts.zip *

3. In firefox about:config set xpinstall.signatures.required to false.

4. In firefox Strg+Shift+A click gear symbol, "Install from file", select zip.



Debug an extension
==================

Open 'about:debugging' in firefox, click 'temporary addon',
select manifest.json of addon.
