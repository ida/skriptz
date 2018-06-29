# Create a file 'versions.cfg', holding the additional egg-names and their
# versions, in comparison to another eggs-cache.
#
# Assumes in every cache each egg occurs only once, and if it exist in the other
# cache, too, they are of same version.
#
# TODO. Print warning, if there's a negative difference, meaning the first eggs-cache has not
# eggs which the other eggs-cache has.
#
# Usage:
# $ python [this_script_path] [eggs_cache_path] [other_eggs_cache_path]
#

import os
import sys

config_path = 'versions.cfg'

def getDiffOfConfigStrings(config_string, other_config_string):
    additional_lines = []
    lines = config_string.split('\n')
    other_lines = other_config_string.split('\n')
    for other_line in other_lines:
        if other_line not in lines:
            additional_lines.append(other_line)
#        if line not in other_lines:
#            print "The first config has an egg, which the other doesn't have:"
    return '\n'.join(additional_lines)
        
def fileNamesListToConfigString(fileNamesList):
    string = ''
    fileNames = [] # let's check for dups
    for fileName in fileNamesList:
        fileName = fileName.split('-')
        if fileName[0] in fileNames:
            print 'We have a dup for "' + fileName[0] + '" !'
        fileNames.append(fileName[0])
        string += fileName[0] + ' = ' + fileName[1] + '\n'
    return string

def genConfigStringOfEggsPath(eggs_path):
    file_names_list = os.listdir(eggs_path)
    file_names_list.sort()
    config_string = fileNamesListToConfigString(file_names_list)
    return config_string

def createFile(filename, string):
    fil = open(filename, 'w')
    fil.write(string)
    fil.close()

def main():
    eggs_path = sys.argv[1]
    other_eggs_path = sys.argv[2]
    string = genConfigStringOfEggsPath(eggs_path)
    other_string = genConfigStringOfEggsPath(other_eggs_path)
    string = getDiffOfConfigStrings(string, other_string)
    string = '[versions]\n' + string
    createFile(config_path, string)

main()
