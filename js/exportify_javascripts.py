"""

What
====

Look into all found js-scripts of this folder, for each script:

- Collect global var- and function-names
- Wrap script into a define-function of require.js
- At its end return globs as a properties-dict-map


Assumes globs occur only at start of line and nested never at start of line.

Example:

A script like:


var varia = 'valua'

var vario = 'valuo'

function aFunk(para) {
  console.log(para)
}

function bFunk(pari) {
  console.log(pari)
}



Is transformed to:


define([], function() {

[SCRIPT_ABOVE]

    return {
      varia: varia,
      vario: vario,
      aFunk: aFunk,
      bFunk: bFunk
    }

});


Why
===

Folling the pythonic pilosophy of "keep it modular", modulize all the
scripts with require.js and expose its globs as props to make them
importable of other modules.

For example, if the script above is named 'super_module.js', another
script can import and use its vars and funcs after the transformation
like this:


// Import returned dict of super_module.js as supmod:
define([super_module], function(supmod) {

  // Execute a function of super_module:
  supmod.aFunk()

  // Get a variable of super_module.js:
  var varia = supmod.varia

});


Where 'supmod' stands for any name you want to use inside of the script.



How
===

Locate into the folder to be searched for scripts and execute
this of the commandline:

    python [PATH_TO_THIS_SCRIPT]/[THIS_SCRIPT_NAME]


You want to backup or make a experimental branch before, as the js-files
are going to be overwritten with the new content.

"""

import os
import sys


def forEachJsFile(scripts_path, doSth):
    paths = getJsFilePaths(scripts_path)
    for path in paths:
        if not path.endswith('main.js'):
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

def genFileEnd(globs):
    file_end = "\n  return {"
    for i, glob in enumerate(globs):
        file_end += "\n    " + glob + ": " + glob
        if i < len(globs)-1: file_end += ','
    file_end += "\n  }\n});"
    return file_end

def getGlobOfLine(line):
    while not line.startswith(' ') :
        line = line[1:]
    line = line[1:]
    while not line.endswith('('): # func-name ended
        line = line[:-1]
        if  line.startswith('='): # var-name ended
            break
    line = line[:-1]
    line = line.strip()
    return line

def indentLines(lines, indent='  '):
    for i, line in enumerate(lines):
        if line != '':
            line = indent + line
        lines[i] = line
    return lines

def processScript(fileName, INDENT=False):
    file_begin = "define([], function() {"
    file_end = None # generated after globs are collected
    globs = []
    orig_string = read(fileName)
    string = stripMultilineComments(orig_string)
    string = stripInnerFuncs(string)
    lines = string.split('\n')

    for i, line in enumerate(lines):
        if(line.startswith('var ') or line.startswith('function ')):
            glob = getGlobOfLine(line)
            globs.append(glob)

    file_end = genFileEnd(globs)

    if INDENT == True:
        orig_string = orig_string.split('\n')
        orig_string = indentLines(orig_string)
        ('\n').join(orig_string)

    string = file_begin + '\n' + orig_string + '\n' + file_end

    write(fileName, string)

def read(path):
    with open(path) as fil: string = fil.read()
    return string


def stripMultilineComments(string):
    new_string = ''
    IN_COMMENT = False
    i = 0
    while i < len(string)-1:
        if string[i] == '/' and i < len(string) and string[i+1] == '*':
            IN_COMMENT = True
            i += 1
        if IN_COMMENT == True:
            if string[i] == '*' and i < len(string) and string[i+1] == '/':
                IN_COMMENT = False
                i += 1
        else:
            new_string += string[i]
        i += 1
    return new_string


def write(path, string):
    with open(path, 'w') as fil: fil.write(string)

def main():
    forEachJsFile('.', processScript)

if __name__ == '__main__':
    main()
