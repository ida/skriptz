food = open('bsp.py')
string = food.read()
food.close()

def getWords(string):
    """ Get words of between quotations.
        Regard single-, double- and tripled-quotes.
    """
    count = 0
    delis = ['"', "'"]
    deli = None
    words = []
    word = ''
    pos = -1
    WORD = False
    TRIP = False

    while pos < len(string):
        char = string[pos]

        # We have a DELI:
        if char in delis:
            
            # Detect triple delis by looking 
            # for next two characters:
            if len(string) > pos+1:
                if string[pos+1] == deli:
                    if len(string) > pos+2:
                        if string[pos+2] == deli:
                            if TRIP:
                        # If word derived of a triple, we need to remove,
                        # the first two characters, which are quots collected 
                        # of the opening triple-quote-include-deli-loop:
                                word = word[2:]
                                TRIP = False
                            else:
                                TRIP = True
                                deli = None
            
            
            # Compare if same, as starting deli (if deli not None):
            if deli == char:
                
                # Not in triple, word closes, ENDING DELI:
                if not TRIP:
                     
                    # WORD ENDS:
                    deli = None
                
                    # Collect word in list, ignore linebreaks:
                    if word != '' and word != '\n':
                        words.append(word)
                    
                    # Reset word:
                    word = ''


                # We are in triple, collect this deli-char in comment,
                else:
                    word += char
            # If no deli set, set it, STARTING DELI:
            if not deli:
                deli = char
        # Char is not a deli and we are not in a triple quoted word:
        else:
            if deli and not TRIP:
            # A deli is set, we are in a word:
            #if deli:
                # Collect char:
                word += char
            # We are in triple, collect this char:
            elif TRIP:
                word += char
        
        pos += 1
    print words
# RUN
getWords(string)
