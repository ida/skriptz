po = 'po.po'
pot = 'pot.pot'

def getEntries(pot):

    entries = []
    entry = []

    with open(pot) as fin:
        for line in fin:
            entry.append(line)
            if line == '\n': # end
                entries.append(entry)
                entry = []

    return entries

def getNuPoEntries():
    nu_po_entries = []
    po_entries = getEntries(po)
    pot_entries = getEntries(pot)
    for pot_e in pot_entries:
        for po_e in po_entries:
            if pot_e[0] == po_e[0]:
                # Has trans?
                if po_e[-2] != 'msgstr ""\n':
                    # Insert trans in entry:
                    pot_e[-2] = po_e[-2]
                    break
        nu_po_entries.append(pot_e)
    return nu_po_entries

def writeNuPo():
    nupo = open('nu.po', 'w')
    nu_po_entries = getNuPoEntries()
    for entry in nu_po_entries:
        if not entry[-3] == 'msgid ""\n': #DEV: skip missing ids
            for e in entry:
                nupo.write(e)
    nupo.close()

writeNuPo()
