"""

What
====

Look into all found js-scripts of this folder.
For each script collect glob-vars and funcs and create a properties-dict of it.

For example a script like:


    var varia = 'varia'

    var vario = 'vario'

    function aFunk(para) {
        console.log(para)
    }

    function bFunk(para) {
        console.log(para)
    }


Is transformed to:


    varia: = 'varia',

    vario: = 'vario',

    aFunk: function(para) {
        console.log(para)
    },

    bFunk: function(para) {
        console.log(para)
    }



Why
===

Preparation to modulize all the scripts with require.js


How
===

Locate into the folder to be searched for scripts and execute
this of the commandline:

    python [PATH_TO_THIS_SCRIPT]/[THIS_SCRIPT_NAME]


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

def globToProp(line):
    """
    Turn:
        var varia = 'varia'
    To:
        varia: 'varia'

    Turn:
        function funcName(para) {
    To:
        funcName: function(para) {
    """
    i = 0
    glob = ''
    globEnd = 0
    middle_string = ''
    if line.startswith('function '):
        middle_string = ' function('
    while not line.startswith(' ') : line = line[1:]
    line = line[1:]
    while line[i] != '=' and line[i] != '(':
        i += 1
    globEnd = i
    line = line[0:globEnd].strip() + ':' + middle_string + line[globEnd+1:]
    return line

def processScript(fileName):
    FIRST_GLOB_FOUND = False
    fileContent = read(fileName)
    lines = fileContent.split('\n')
    prop_separator = ','
    previous_line_i = None
    for i, line in enumerate(lines):
        line = line.strip()
        if(line.startswith('var ') or line.startswith('function ')):
            line = globToProp(line)
            if FIRST_GLOB_FOUND:
                previous_line = lines[i-1]
                previous_line += prop_separator
                lines[i-1] = previous_line
            FIRST_GLOB_FOUND = True
            lines[i] = line
    lines = ('\n').join(lines)
    write(fileName, lines)

def main():
    forEachJsFile('.', processScript)

if __name__ == '__main__':
    main()

