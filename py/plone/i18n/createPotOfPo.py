import shutil
source = 'our.translations.pot'
target = source + '.tmp'
with open(source) as fin, open(target, 'w') as fout:
    for line in fin:
        if line.startswith('msgstr "'):
            fout.write('msgstr ""\n')
        else:
            fout.write(line)
    shutil.move(target, source)            
