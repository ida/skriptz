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
# act
while pos < len(string):
    char = string[pos]

    if not WORD:
        # Detect deli:
        if char in delis:
            # If none, set it:
            if not deli:
                deli = char
            # Compare if same as starting deli:
            elif deli == char:
                # Yes, word closes:
                WORD = False
                if word != '': words.append(word)
                word = ''
    else: # in word
        word += char
        
    pos += 1


print words





# EOF
