# extract words of between single quotes
import re
# define
delis = ['"', "'"]
deli = None
words = []
word = ''
pos = -1
WORD = False
# feed
food = open('bsp.py')
string = food.read()
food.close()
TRIP = False
count = 0
# act
while pos < len(string):
    char = string[pos]

    # We have a DELI:
    if char in delis:
        
        # Detect  triple delis:
        if len(string) > pos+1:
            if string[pos+1] == deli:
                if len(string) > pos+2:
                    if string[pos+2] == deli:
                        count+=1
                        print TRIP
                        if TRIP: TRIP = False
                        else: TRIP = True
        
        # Compare if same, as starting deli (if deli not None):
        if deli == char:
            
            # Not triple and same as starting deli, word closes, ENDING DELI:
            if not TRIP: deli = None
            
            # Collect word in list, ignore added linebreaks of collecting:
            if word != '' and word != '\n':
                words.append(word)
                #print TRIP
            
            # Reset word:
            word = ''


        # If no deli set, set it, STARTING DELI:
        if not deli:
            deli = char
    # Char is not a deli and we are not in a triple quoted word:
    else:
        if not TRIP and deli:
        # A deli is set, we are in a word:
        #if deli:
            # Collect char:
            word += char
    
    pos += 1



print words

print count


# EOF
