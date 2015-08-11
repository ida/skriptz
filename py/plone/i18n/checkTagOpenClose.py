food = open('my.pt').read()
IN_TAG = False
IN_COMMENT = False
IN_QUOTES = False
pos = -1
tag = ''
while (len(food) > pos + 1):
    pos += 1
    
    # Tag opens:
    if (food[pos] == '<') and (IN_QUOTES== False):
        IN_TAG = True
        
        # Special case comments:
        if len(food) > pos + 3 and food[pos+1:pos+3] == '!--':
            IN_COMMENT = True

    # Tag closes:
    if (food[pos] == '>') and (IN_QUOTES == False):
        IN_TAG = False
        
        if IN_COMMENT:
            if (pos -2 > -1) and (food[pos-1] == '-' and food[pos-2] == '-'):
                IN_COMMENT = False

        tag = tag[1:] #remove starting bracket

        return tag # gotcha

    # Quotes in tag (attr-vals):
    if food[pos] == '"' and IN_TAG:
        if IN_QUOTES: IN_QUOTES = False
        else: IN_QUOTES = True
    
    # Write tag:
    if IN_TAG:
        tag += food[pos]
