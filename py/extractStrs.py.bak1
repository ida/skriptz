food = open('bsp.txt').read()
WORD = False
TRIP = False
trip = 0
pos = -1
words = []
word = ''
delis = ['"', "'"]
deli = None
##############################

TRIP_ENDED = False

while len(food) > pos + 1:

    pos += 1

    # DELI:
    if food[pos] in delis:
	if not deli:
	    deli = food[pos]
	if len(food) > pos+1:
    	    if food[pos+1] == deli:
	 	if len(food) > pos+2:
    		    if food[pos+2] == deli:
			pos += 2
			if TRIP: 
			    TRIP_ENDED = True
			    TRIP = False
			    WORD = False
			    deli = None
			else: 
			    TRIP = True
			    WORD = True
		    	    pos += 1
	if TRIP:
	    word += food[pos]
	    pos += 1
	else:
	    if WORD: 
		WORD = False
		deli = None
	    else:
		if not TRIP_ENDED: 
		    WORD = True
		    pos += 1
		else:
		    TRIP_ENDED = False
    if WORD:
        word += food[pos]
print word		
##############################
