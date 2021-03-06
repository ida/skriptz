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

def addMissingIds(pot):
    misses = 0
    nuentries = []    
    entries = getEntries(pot)
    for entry in entries:
        msgid = entry[-2][7:-2]
        if msgid == '':
            entry[-2] = 'msgid "our-' + str(misses) + '"\n'
            misses += 1
        nuentries.append(entry)
    nupot = open('nu.pot', 'w')
    for entry in nuentries:
        for line in entry:
            nupot.write(line)
        nupot.write('\n')
    nupot.close()

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

def createPotOfPo(po):
    nupot = ''
    po = open(po).read()
    lines = po.splitlines()
    for line in lines:
        print line
        if line.startswith('msgstr'):
            nupot += 'msgstr ""'
        else:
            nupot += line
        nupot += '\n'
    nupot_file = open('nupot.pot', 'w')
    nupot_file.write(nupot)
    nupot_file.close()

def compStrsOfTwoPos(po, nupo):
    oldentries = getEntries(po)
    oldentries = getEntries(po)
    nuentries = getEntries(nupo)

# lookup old id beginning with 'our':
    for oldentry in oldentries:
        oldid = getMsgId(oldentry)
        if oldid.startswith('our-'):
# get refering entry by defstr:
            olddef = getDefStr(oldentry)
            for nuentry in nuentries:
                nudef = getDefStr(nuentry)
                if nudef == olddef:
                    nuid = getMsgId(nuentry)
                    if oldid != nuid:
                        print oldid, nuid


