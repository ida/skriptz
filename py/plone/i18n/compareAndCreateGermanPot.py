po = 'po.po'
ger = 'ger.po'

def getEntries(po):
    entries = []
    entry = []
    with open(po) as fin:
        for line in fin:
            if line != '\n': # end
            entry.append(line)
            if line == '\n': # end
                if entry != []: #regard multiple emptylines
                    entries.append(entry)
                    entry = []

    return entries

def addMissingTrans():
    nu_po_entries = []
    po_entries = getEntries(po)
    ger_entries = getEntries(ger)
    print ger_entries
    for poe in po_entries:
        # Trans is missing:
        if poe[-2] == 'msgstr ""\n':
            dstr = poe[0]
            for ge in ger_entries:
                # Where defstr equals:
                g_dstr == ge[0]
        nu_po_entries.append(poe)
    return nu_po_entries

def writeNuPo():
    nupo = open('nu.po', 'w')
    nu_po_entries = addMissingTrans()
    for entry in nu_po_entries:
#        if not entry[-3] == 'msgid ""\n': #DEV: skip missing ids
        for e in entry:
            nupo.write(e)
    nupo.close()

writeNuPo()
