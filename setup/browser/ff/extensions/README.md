1. Create a directory, add a file named 'manifest.json' with this content:

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


2. From within the extension directory, do:

    zip -r -FS ../sharpcuts.zip *

3. In firefox about:config set xpinstall.signatures.required to false.

4. In firefox Strg+Shift+A click gear symbol, "Install from file", select zip.
