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
        
def fileNamesToConfigString(file_names):
    string = ''
    collected_file_names = [] # let's check for dups
    for file_name in file_names:
        file_name = file_name.split('-')
        if file_name[0] in file_names:
            print 'We have a dup for "' + file_name[0] + '" !'
        collected_file_names.append(file_name[0])
        string += file_name[0] + ' = ' + file_name[1] + '\n'
    return string

def genConfigStringOfEggsPath(eggs_path):
    file_names = os.listdir(eggs_path)
    file_names.sort()
    config_string = fileNamesToConfigString(file_names)
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
