# Compare first line of angi.txt with last line of .pot:
pot = open('message_ids.pot').read()
po = open('angi.txt').read()
ENTRY_STARTS = True
read_line = ''
pot_msgs = []
po_msgs = []
matched = []
only_in_pot = []
only_in_po = []

# Collect strs of pot:
pot_lines = pot.splitlines()
for line in pot_lines:
    #print ':::'+line+':::'
    if line == '':
        msgstr = read_line[8:-1]
        #if msgstr != '' and not ( msgstr.startswith('${') and msgstr.endswith('}') ):
        if msgstr != '':
            pot_msgs.append(msgstr)
    read_line = line

# Collect strs of po:
po_lines = po.splitlines()
for line in po_lines:
    if ENTRY_STARTS:
        msgstr = line[2:]
        if msgstr != '':
            po_msgs.append(msgstr)
        ENTRY_STARTS = False

    if line == '':
        ENTRY_STARTS = True

# Compare pot and po:
for entry in pot_msgs:
    if entry in po_msgs:
        matched.append(entry)
    else:
        only_in_pot.append(entry)

# Compare po and pot:
for entry in po_msgs:
    if entry in pot_msgs:
        if not entry in matched:
            print 'UPS!',+entry
    else:
        only_in_po.append(entry)


print 'pot_msgs'
print len(pot_msgs)
print 'po_msgs'
print len(po_msgs)
print 'matched'
print len(matched)
print 'only_in_pot'
print len(only_in_pot)
print 'only_in_po'
print len(only_in_po)
print only_in_po
print only_in_pot
