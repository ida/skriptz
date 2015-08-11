FIRSTLINE = True
def_strs = []
po = open('nu.po').read()
lines = po.splitlines()
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
    if line == '':
        entries += 1
        FIRSTLINE = True

print len(def_strs)
print pys, pts, jss
print translated
print entries
words = 0
for s in def_strs:
    for c in s:
        if c == ' ':
            words += 1
        if c == '$':
            words -= 1
        words += 1
#print words
