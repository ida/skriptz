#!/usr/bin/python

# Creates a 'deveggs.cfg' with the entries for buildout
# of a given directory holding the deveggs, when executed in the
# same directory, where the buildout.cfg lives.

import os

path = 'src'

config_name = 'deveggs.cfg'

def getDevEggNames():
    dev_eggs = os.listdir(path)
    return dev_eggs

def prepareString(dev_eggs):
    string = '[buildout]\nextends = buildout.cfg\n[instance]\neggs +=\n'
    for dev_egg in dev_eggs:
        string += '    ' + dev_egg + '\n'
    string += 'develop +=\n'
    for dev_egg in dev_eggs:
        string += '    ' + path + '/' + dev_egg + '\n'
    return string

def createFile(filename, string):
    fil = open(filename, 'w')
    fil.write(string)
    fil.close()

def main():
    filename = config_name
    dev_eggs = getDevEggNames()
    string = prepareString(dev_eggs)
    createFile(filename, string)

main()
