# !/usr/bin/python
import os
delimiter = ''
delimiters = ['"', "'"]
word = ''
words = []
IN_WORD = False
BROKE = False
for root, dirs, files in os.walk("."):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        if  file_name.endswith('py'):
            with open(file_path) as fil:
                line = fil.readline()
                
                while(line):
                    
                    pos = -1

                    if line[pos] in delimiters:
                        print 'line starts with deli'
                        
                    while (len(line) > pos+1):
                        
                        pos+=1
                        
                        if (line[pos] == delimiter):
                        
                            if IN_WORD: 
                                
                                IN_WORD = False
                                words.append(word)
                                print word
                                word = ''
                            
                            else: 
                                
                                IN_WORD = True

                        if IN_WORD: 
                            
                            word += line[pos]
                            
                    

                    # Read next line:
                    line = fil.readline()
                    BROKE = False
