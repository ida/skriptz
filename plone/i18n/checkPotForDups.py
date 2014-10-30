dup = None
FIRSTLINE = True
entries = 0
firstlines = []
dups = []
ids = []
dup_ids = []
dup_pairs = []
pot = open('pot.pot').read()
lines = pot.splitlines()
for line in lines:

    if FIRSTLINE:
        FIRSTLINE = False
        if line not in firstlines:
            dup = line
        else:
            dups.append(line)

    if line.startswith('msgid') and line != 'msgid ""':
        if line not in ids:
            ids.append(line)
            if dup:
                firstlines.append(dup)
                dup = None
        else:
            if dup:
                pair = dup_pairs.append([dup, line])
                dup = None
            else:
                dup_ids.append(line)

    if line == '':
        FIRSTLINE = True
        entries += 1

print dups
print '---'
print dup_ids
print '---'
print dup_pairs
