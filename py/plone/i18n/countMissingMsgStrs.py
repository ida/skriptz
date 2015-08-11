po = open('nu.po').read()
lines = po.splitlines()
trans = 0
miss = 0
for line in lines:
    if line.startswith('msgstr "'):
        if line == 'msgstr ""':
            miss += 1
        else:
            trans += 1
print trans
print miss
