"""

What
====

Merge all found js-scripts of a given folder into one js-script and
wrap it into one global function, that takes exactly one parameter
named 'appEle', following the approach to bind an app to an ele and
furtheron operate within that scope, independently of other apps.

It is assumed that one of your scripts contains a function named 'main',
that takes the appEle as a parameter, it will be added as the last line
before the closing bracket to get started within the glob-func, also a
var is added inside of the glob-func, named 'appName' and equals the
funcname, that is a convention of the author, ment to be used to share
the glob-name with stylesheets, using the name as prepending selector
for any style-rule.

The result then looks like this:

    function youAppName(appEle) {

      var appName = 'yourAppName'

      // Here all your js-scripts are inserted.

      main(appEle)

    } // End of yourAppName


Why
===

Former global var- and func-names are now wrapped into one function and cannot
conflict with other globs anymore, just the one func-name must be guaranteed to
be unique within the global scope, the window-object.

After the DOM loaded the app can then be intialized like: `appName(appEle)`.


How
===

Of the commandline execute this script:

    python [THIS_SCRIPT_NAME].py appsolutely


Where "appsolutely" stands for the function-name you want to use, if omitted
defaults to 'app'.

By default the results will be poured into a js-file which gets the same
name than the app has, in this example that would be 'appsolutely.js',
you change that to anyother name like this:

    python [THIS_SCRIPT_NAME].py appsolutely my_output.js


By default the script will look for js-files within the folder
where you execute this script, you can specify another folder:

    python [THIS_SCRIPT_NAME].py appsolutely my_output.js path/to/js-scripts


"""

import os
import sys


def forEachJsFile(scripts_path, doSth):
    paths = getJsFilePaths(scripts_path)
    for path in paths:
        doSth(path)

def getChildrenFilePaths(path):
    paths = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            paths.append(file_path)
    return paths

def getJsFilePaths(parent_path):
    js_paths = []
    paths = getChildrenFilePaths(parent_path)
    for path in paths:
        if path.endswith('.js'):
            js_paths.append(path)
    return js_paths

def read(path):
    with open(path) as fil: string = fil.read()
    return string

def write(path, string):
    with open(path, 'w') as fil: fil.write(string)

def main(app_name, output_file_path, input_files_path):
    os.system('echo "function ' + app_name + '(appEle) {" > ' + output_file_path)
    os.system('echo "var appName = \'' + app_name + '\'" >> ' + output_file_path)
    def appendFileToOutputFile(path):
        if not path.endswith('/' + output_file_path):
            os.system('cat ' + path + ' >> ' + output_file_path)
    forEachJsFile(input_files_path, appendFileToOutputFile)
    os.system('echo "  main(appEle)" >> ' + output_file_path)
    os.system('echo "} // End of ' + app_name + '()" >> ' + output_file_path)

if __name__ == '__main__':
    args = sys.argv
    args.pop(0) # remove 1st in-built arg, is no userinput
    if len(args) < 1: args.append('app')
    if len(args) < 2: args.append(args[0] + '.js')
    if len(args) < 3: args.append('./')
    if not args[2].endswith('/'): args[2] += '/'
    main(args[0], args[1], args[2])

