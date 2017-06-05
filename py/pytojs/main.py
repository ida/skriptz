# My Python-to-Javascript-converter.
# Write in Python get Javascript.
# Resolves for- if- and def-blocks to Javascript.
# Example:
# for item in items:
#   doSth(item)
# Becomes:
# for(var i=0; i < items.length; i++) {
#   var item = items[i]
#   doSth(item)
# }
# Usage:
# python ./pytojs/main.py inputfile.pyjs # extension can be anything
# Result:
# Creates or overwrites in a JS-file with the same name
# in the directory where you execute this script.
# TODO: Regard nested blocks and indentation.

import sys

def transformForLoop(string):
    """We expect string to be like 'for item in items'."""
    words = string.split(' ')
    items = words[-1]
    string = 'for(var i=0; i < ' + items + '.length; i++) {\n\
    var ' + words[1] + ' = ' + items + '[i]'
    return string

def transformFunLoop(string):
    """We expect string to be like 'fun someName'."""
    words = string.split(' ')
    name = words[-1]
    string = 'function ' + name + '() {'
    return string

def isUpcomingWord(string, i, word):
    if i < len(string) - len(word) and string[i:i+len(word)] == word:
        return True
    else: return False

def pyToJs(string):
    string_new = ''
    i = 0
    keyword_current = 'for '
    keyword_end = ':'
    replace_start = None
    BLOCK = False
    KEYWORD = False

    keywords = [keyword_current, 'fun ']

    while i < len(string):
        for keyword in keywords:
            if isUpcomingWord(string, i, keyword):
                KEYWORD = True
                replace_start = i
                keyword_current = keyword

        if KEYWORD:
            if isUpcomingWord(string, i, keyword_end):
                string_to_replace = string[replace_start:i]
                if keyword_current == 'for ':
                    string_new += transformForLoop(string_to_replace)
                else:
                    string_new += transformFunLoop(string_to_replace)

                KEYWORD = False
                BLOCK = True
        else:
            if BLOCK:
                if string[i] == '\n' and i + 1 < len(string) and string[i+1] == '\n':
                    BLOCK = False
                    string_new += '\n}' # insert end-deli of for/if/function-block
            string_new += string[i]
        i += 1
    return string_new

def main():
    infile = sys.argv[1]
    outfile = infile.split('.')[0] + '.js'
    string = open(infile).read()
    string = pyToJs(string)
    open(outfile, 'w').write(string)

main()
