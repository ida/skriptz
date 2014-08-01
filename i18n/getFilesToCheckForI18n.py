# !/usr/bin/python

# Get files which need i18n for doublecheck.

import os

# needs our own translation-package:
xml_own = ['actions','controlpanel','type']
# needs another translation-package:
xml_plone = ['portlets', 'portal_atct']


pies  = 0
tmpl  = 0
xml   = 0
ecma  = 0
summ  = 0
total = 0

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
            if suff == ('.py' or '.cpy' or 'vpy'):
                if (file_path.find('/tests/') == -1):
                    if file_name != ('merge.py' and 'setup.py' and 'config.py' and 'setuphandlers.py'):
                        isEmpty = True
                        with open(file_path) as fil:
                            line = fil.readline()
                            while(line):
                                if line[0] != '#' and line != '' and line != '\n':
                                    isEmpty = False
                                    foundApo = False
                                    if (line.find('"') != -1) or (line.find("'") != -1):
                                        if (line.find('Initializer') == -1) and (line.find("loadMigrationProfile") == -1) and (line.find("pkg_resources") == -1):
                                            foundApo = True

                                line = fil.readline()
                        if not isEmpty and foundApo:
                            pies += 1

            # *PT
            elif suff == '.zpt' or suff == '.pt':
                tmpl += 1

            # XML
            elif suff == '.xml' and file_path.find('profile') != -1:
                if ( file_path.find('upgrades') == -1 and file_path.find('uninstall') == -1 and file_path.find('type') != -1 or file_name in (xml_own or xml_plone) ):
                    xml   += 1

            # JS
            elif suff == '.js':
                ecma    += 1


summ = pies + tmpl + xml + ecma

print 'We have ' + str(pies) + ' python-scripts, ' + str(tmpl) + ' page-templates, '  + str(xml) + ' xml-configs, ' + str(ecma) +' javascripts to check. That is a total of ' + str(summ) + '.'
