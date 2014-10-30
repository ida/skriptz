FIRSTLINE = True
def_strs = []
po = open('pot.pot').read()
lines = po.splitlines()
missing_ids = 0 
translated = 0 
pys = 0 
pts = 0
jss = 0
entries = 0
for line in lines:
    if FIRSTLINE:
        def_str = line[2:]
        FIRSTLINE = False
    if line.startswith('# ./'):
        if line.endswith('pt'):
            pts += 1
        if line.endswith('py'):
            pys += 1
        if line.endswith('js'):
            jss += 1
    if line == 'msgstr ""':
        def_strs.append(def_str)
    if line.startswith('msgstr "') and not line.endswith('""'):
        translated += 1
    if line == 'msgid ""':
        missing_ids += 1
    if line == '':
        entries += 1
        FIRSTLINE = True

print missing_ids
words = 0
for s in def_strs:
    for c in s:
        if c == ' ':
            words += 1
        if c == '$':
            words -= 1
        words += 1
#print words
