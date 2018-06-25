#!/usr/bin/python

# Execute this in the directory where the 'eggs'-directory lives
# and get a versions-config, holding the egg-names and their versions.

import os

eggs_path = 'eggs'
config_path = 'versions.cfg'

def fileNamesListToConfigString(fileNamesList):
    fileNames = [] # let's check for dups
    string = '[versions]\n'
    for fileName in fileNamesList:
        fileName = fileName.split('-')
        if fileName[0] in fileNames:
            print 'We have a dup for "' + fileName[0] + '" !'
        else: fileNames.append(fileName[0])
        string += fileName[0] + ' = ' + fileName[1] + '\n'
    return string

def createFile(filename, string):
    fil = open(filename, 'w')
    fil.write(string)
    fil.close()

def main():
    fileNamesList = os.listdir(eggs_path)
    fileNamesList.sort()
    string = fileNamesListToConfigString(fileNamesList)
    createFile(config_path, string)

main()
