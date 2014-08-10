# !/usr/bin/python

# Get files which need i18n for doublecheck.

import os

delimiters = ['"', "'"]
# needs our own translation-package:
xml_own = ['actions','controlpanel','type']
# needs another translation-package:
xml_plone = ['portlets', 'portal_atct']


pies  = 0
tmpl  = 0
xml   = 0
ecma  = 0
summ  = 0
total = 0

# Walk through directory recursively:
for root, dirs, files in os.walk("."):

    # For each file:
    for file_name in files:

        total += 1

        file_path = os.path.join(root, file_name)

        splitted_name = os.path.splitext(file_name)

        if len(splitted_name) > 0:

            suff = splitted_name[1]

            # JS
            if suff == '.js':# or suff == '.py':
                ecma    += 1
                    
                word = ''
                words = []
                IN_WORD = False
                #print file_path 
                with open(file_path) as fil:
                    line = fil.readline()
                    
                    while(line):
                    
                        pos = 0
                        
                        while len(line) > pos+1:
                
                            char = line[pos]
                            
                            if IN_WORD:
                                word += char
                                while len(line) > pos+1:
                                    pos += 1
                                     
                            # START
                            if char in delimiters:
                                IN_WORD = True
                                word = char
                                delimiter = char
                                TRIPLE_DELIMI = False
# delimiter following delimiter?
                                if len(line) > pos + 1:
                                    if line[pos+1] == delimiter:
                                        if len(line) > pos + 2:
                                            if line[pos+2] == delimiter:
                                                TRIPLE_DELIMI = True
                                                print 'triple'
                                            else:
                                                pass#rint 'double = empty'
                                while (char != delimiter):
                                    while len(line) > pos+1:
                                        pos = pos+1
                                        char = line[pos]
                                        word += char
                                word += char
                                pos = pos+1
#                                print word
                                break
                            # END
                            
                            words.append(word)
                            pos += 1
                        
                        line = fil.readline()

#                if words != []: print words
#                print file_path
                break






summ = pies + tmpl + xml + ecma

#print 'We have ' + str(pies) + ' python-scripts, ' + str(tmpl) + ' page-templates, '  + str(xml) + ' xml-configs, ' + str(ecma) +' javascripts to check. That is a total of ' + str(summ) + '.'
