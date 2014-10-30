pot = 'pot.pot'

def getEntries(pot):
    
    entries = []
    entry = []
    
    with open(pot) as fin:
        for line in fin:
            if line != '\n':
                entry.append(line)
            if line == '\n': # end
                entries.append(entry)
                entry = []
    
    return entries


def getStrs(pot):

    check_paths = []    
    entries = getEntries(pot)
    
    for entry in entries:
    
        def_str = entry[0][2:-1] # minus linebreak
        paths = entry[1:-2]
        msgid = entry[-2][7:-2]
        msgstr = entry[-1][8:-2]

        if msgid == '':
            for path in paths:
                if not path in check_paths:
                    check_paths.append(path)
    print check_paths

getStrs(pot)
