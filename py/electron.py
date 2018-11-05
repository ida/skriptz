# Helpers for creating electron-apps.

import os

def addApp(app_name):
    if os.path.exists(app_name):
        os.system('rm -rf ' + app_name) # DEV: destroy
        # return # PROD: abort
    os.system('mkdir ' + app_name)
    nodifyDirectory(app_name)
    electrifyDirectory(app_name)

def nodifyDirectory(directory_path):
    """
    Make directory to be a node-app.
    """
    string = """{
  "description": "An electron-app of yet unknown purpose.",
  "repository": "https://",
  "license": "MIT",
  "devDependencies": {
    "electron": "^2.0.0"
  }
}"""
    with open(directory_path + '/package.json', 'w') as fil:
        fil.write(string)


def electrifyDirectory(directory_path):
    """
    Make a directory to be an electron-app for development.
  "devDependencies": {
    "electron": "^2.0.0"
  }
    """
    string = None
    with open(directory_path + '/package.json') as fil:
        string = fil.read()
    if string.find('devDependencies') == -1:
        print('no devDependencies')


if __name__ == '__main__':
    addApp('electra')

