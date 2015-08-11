# !/usr/bin/python

# Get strings between '' or ""
# Handle triplequotes

import os

wanted_filetypes = ['py']
exclude_file_paths = ['/Paste', '/test']
exclude_files = ['setup.py']
exclude_words = ['', # no empty strs\
'pkg_resources'] # in first __init__.py
WORD = False
delimiters = ['"', "'"]
delimiter = ''
word = ''
words = []
preceding_line = ''
preceding_chars = ''
TRIP = False
KLASS = False
EXCLUDE = False
UNICODE = False
DEVMAX = 17
DEVMAX = 7777

# Walk recursively through directory:
for root, dirs, files in os.walk("."):
    # For each file:
    for file_name in files:
        file_path = os.path.join(root, file_name)
        if DEVMAX > 0:
            DEVMAX -= 1
            
            TYPE = False
            PATH = True
            NAME = True

            for wanted in wanted_filetypes:
                if file_name.endswith(wanted) != -1:
                    TYPE = True

            for ex_path in exclude_file_paths:
                if file_path.find(ex_path) != -1:
                    PATH = False
            
            for ex_file in exclude_files:
                if file_name == ex_file:
                    NAME = False

            if TYPE and PATH and NAME:
                with open(file_path) as fil:
                    line = fil.readline()
                    while(line):

                        for i in range(len(line)):
                            char = line[i]
                            preceding_chars += char

                            # FOUND DELI:
                            if char in delimiters:

                                if WORD:
                                    
                                    if char == delimiter:
                                        WORD = False
                                        
                                        # Triple quotes?
                                        if len(line) > i+1:
                                            if line[i+1] == delimiter:
                                                if len(line) > i+2:
                                                    if line[i+2] == delimiter:
                                                        END_TRIP = True
                                                    else: END_TRIP = False

                                        #word = ' '.join(word.split()) # remove superfluous space

                                        if KLASS: 
                                            if word not in exclude_words:
                                                word = 'KLASS: ' + word
                                                exclude_words.append(word)
                                                                                
                                        if word not in exclude_words and not EXCLUDE:
                                            
                                            words.append(word)
                                        if EXCLUDE: EXCLUDE = False                       
                                        word = ''
                                    
                                    # Collect chars in word:
                                    else:
                                        word += char
                                
                                else:
                                    WORD = True
                                    delimiter = char
                                    
                                    # WORD STARTS: 
                                
                                    # Triple quotes?
                                    if i-1 >= 0:
                                        if line[i-1] == delimiter:
                                            if i-2 >= 0:
                                                if line[i-2] == delimiter:
                                                    TRIP = True
                                    
                                    # Preceding char:
                                    if i-1 >= 0:
                                        # Preceding square-bracket?
                                        if line[i-1] == '[':
                                            EXCLUDE = True
                                        # Preceding unicode-decla?
                                        elif line[i-1] == 'u':
                                            UNICODE = True
                                        # Preceding round bracket?
                                        elif line[i-1] == '(':
                                            # Pre-preceding char:
                                            if i-2 >= 0:
                                                # i18n-hook?
                                                if line[i-2] == '_':
                                                    # Not a doubled underscore?
                                                    if i-3 >= 0:
                                                        if line[i-3] == '_':
                                                            pass
                                                        else:
                                                            #print file_path
                                                            print line

                            # NO DELI, collect char, if WORD:
                            elif WORD:
                                word += char
                        
                        if line.startswith('class'):
                            KLASS = True
                        else:
                            KLASS = False


                        preceding_line = line
                        line = fil.readline()

#                print file_path
###################################################
for word in words:
#    print ':'+word+':'
    pass
#print words
#print file_path
            #print len(words)
#            print file_path
            #print exclude_words
###################################################
