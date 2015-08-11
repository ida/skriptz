# !/usr/bin/python

import os
import shutil

pys = ['.py', '.cpy', '.vpy']

# Walk through directory recursively:
for root, dirs, files in os.walk("."):

    # For each file:
    for file_name in files:

        total += 1

        file_path = os.path.join(root, file_name)

        splitted_name = os.path.splitext(file_name)

        if len(splitted_name) > 0:

            suff = splitted_name[1]

            # *PY
            if suff in pys:
                if (file_path.find('/tests/') == -1):

                    # Something to translate?
                    NEED_MSGFAC = False
                    food = open(file_path).read()
                    find_patterns = ["_('", "_(u'", '_("', '_(u"']
                    for pat in find_patterns:
                        if food.find(pat) != -1:
                            NEED_MSGFAC = True

                    # Yes, let's do sth:
                    if NEED_MSGFAC:
                        with open(conf) as fin, open(conftmp, 'w') as fout:
                            for line in fin:
                                # If exists already:
                                if line.find('<include package=".browser" />') != -1:
                                    LAYER_EXISTS = True

                                # Insert if not exists already:
                                if line.find('</configure>') != -1 and not LAYER_EXISTS:
                                    fout.write('  <include package=".browser" />\n\n')

                                fout.write(line)
                            # Overwrite original with workingcopy:
                            shutil.move(conftmp, conf)
