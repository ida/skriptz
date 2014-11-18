#!/usr/bin/python

# Execute this in the directory where the dev-eggs live
# and get a config holding the entries and extending buildout.cfg.
# Then run buildout with the created config: `./bin/buildout -c deveggs.cfg`

import os

config_name = 'deveggs.cfg'


def prepareString(dev_eggs):
    path = os.getcwd()
    string = '[buildout]\nextends = buildout.cfg\ndevelop +=\n'
    for dev_egg in dev_eggs:
        string += '    ' + path + '/' + dev_egg + '\n'
    string += '[instance]\neggs +=\n'
    for dev_egg in dev_eggs:
        string += '    ' + dev_egg + '\n'
    return string

def createFile(filename, string):
    fil = open(filename, 'w')
    fil.write(string)
    fil.close()

def main():
    filename = config_name
    dev_eggs = os.listdir('.')
    string = prepareString(dev_eggs)
    createFile(filename, string)

main()
