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
def getDefStr(entry):
    return entry[0][2:-1] 
def getPaths(entry):
    return entry[1:-2]
def getMsgId(entry):
    return entry[-2][7:-2]
def getMsgStr(entry):
    return entry[-1][8:-2]

def getDupedStrs(pot):
    msgstrs = []
    dups = []
    entries = getEntries(pot)
    for entry in entries:
        def_str = getDefStr(entry)
        if not def_str in msgstrs:
            msgstrs.append(def_str)
        else:
            dups.append(def_str)
    return dups

def getMissingIds(pot):
    
    misses = 0
    check_paths = []    
    entries = getEntries(pot)
    
    for entry in entries:
    
        paths = entry[1:-2]
        msgid = entry[-2][7:-2]
        if msgid == '':
            misses += 1
            for path in paths:
                if not path in check_paths:
                    check_paths.append(path)
    print check_paths
    print len(check_paths)
    print misses

def getSaneEntries(pot):
    entries = getEntries(pot)
    sane_entries = []
    # Remove dups:
    dups = getDupedStrs(pot)    
    for entry in entries:
        if not (getMsgId(entry) == '') and (getDefStr(entry) in dups):
            sane_entries.append(entry)
    nupot = open('nu.pot', 'w')
    for entry in sane_entries:
        for line in entry:
            nupot.write(line)
        nupot.write('\n')
    nupot.close()

getSaneEntries(pot)
