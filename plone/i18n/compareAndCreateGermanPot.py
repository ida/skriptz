po = open('ger.po').read()
pot = open('pot.pot').read()

def getMsgsDict(food):
    paths = []
    msgs_dict = []
    msg_def = ''
    msg_id = ''
    msg_str = ''
    FIRSTLINE = True
    lines = food.splitlines()
    for line in lines:
        line = line.strip() # !
        if FIRSTLINE:
            FIRSTLINE = False
            msg_def = line
        if line.startswith('# ./'):
            paths.append(line)
        if line.startswith('msgid "'):
            msg_id = line
        if line.startswith('msgstr "'):
            msg_str = line
        if line == '':
            FIRSTLINE = True
            msgs_dict.append([msg_def, paths, msg_id, msg_str])
            paths = []
#    for i in range(len(msgs_dict)):
#	    print msgs_dict[i][1] #paths
    return msgs_dict

def createNuPo():
    FOUND_TRANS = False
    nupo_feed = ''
    pot_dict = getMsgsDict(pot)
    po_dict = getMsgsDict(po)
    for entry in pot_dict:
        def_str = entry[0]
        nupo_feed += def_str # default
        nupo_feed += '\n'
        for path in entry[1]:
            nupo_feed += str(path)
            nupo_feed += '\n'
        nupo_feed += entry[2] # msgid
        nupo_feed += '\n'
        # Do we have an equiv def_str in po?
        for entr in po_dict:
            if entr[0] == def_str:
                FOUND_TRANS = True
                nupo_feed += entr[3] # Write translated msgstr.
        if not FOUND_TRANS:
                nupo_feed += entry[3] # Write empty msgstr of pot.
        else:
            FOUND_TRANS = False
        nupo_feed += '\n'
        nupo_feed += '\n'

    nupo = open('nu.po', 'w')
    nupo.write(nupo_feed)
    nupo.close()

createNuPo()
