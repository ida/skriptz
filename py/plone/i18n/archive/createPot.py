# !/usr/bin/python

# TD: regard \' in pystrs:
# 'A message to \'nobody\' or \'somebody\'.'
# TD: Check if regard variable-substitutes in pys:
# 'Bla %s blubb.'%varia

# Creates a pot file for i18n-translations.
# Will look for and extract all strings prepended with an underscore
# or of a tag's i18n:translate-attribute, recursively to the given location
# where this file is executed.
# Usage is: `python createPot.py` outcome is a file named
# "message_ids.pot" in the same directory.

import os, re
entries = 0
msg_ids = []
pot_entries = []
single_quoted_patterns = ["_(u'", "_('"]
double_quoted_patterns = ['_(u"', '_("', 'i18n:translate="']
find_patterns = single_quoted_patterns + double_quoted_patterns

#DEV stats:
pies = 0
jies = 0
ties = 0

# Collect msg-id's in list:
for root, dirs, files in os.walk("."):
    # For each file:
    for file_name in files:
        # Unless it's this file:
        if file_name.find('createPot.py') == -1 and file_name.find('.swp') == -1:
            file_path = os.path.join(root, file_name)
            with open(file_path) as fil:
                line = fil.readline()
                line_nr = 1
                while(line):
                    for pat in find_patterns:
                        # Look for pattern:
                        if line.find(pat) != -1:
                            # Extract msg-id of between quotation-marks:
                            if pat in single_quoted_patterns:
                                prep_regex = re.escape(pat) + "(.*)[']"
                                result = re.search(prep_regex, line)
                                if result:
                                    result_chunks = result.group(1)
                                    msg_id = result_chunks.split("'")[0]
                                else:
                                    print 'Ups:'
                                    print file_path
                                # result_chunks can be e.g.:
                                # "Login failed'), 'error"
                                # or:
                                # "label_password', default=u'Password"
                            
                            if pat in double_quoted_patterns:
                                prep_regex = re.escape(pat) + '(.*)["]'
                                result = re.search(prep_regex, line)
                                if result:
                                    result_chunks = result.group(1)
                                    msg_id = result_chunks.split('"')[0]
                                else:
                                    print 'Ups:'
                                    print file_path
                            
                            # Not empty:
                            if msg_id is not '':
                            
                                # No dups:
                                if msg_id not in msg_ids:
                            
                                    # Collect in list:
                                    msg_ids.append(msg_id)
                                    pot_entry = '#'+file_path+', '+str(line_nr)+':\nmsgid "'+msg_id+'"\nmsgstr ""\n\n'
                                    pot_entries.append(pot_entry)
                                    entries += 1
                            
                                elif msg_id in msg_ids:
                                    pass#rint 'DUP: ' + msg_id
                            
                            #if msg_id == '"':
                            #    print result.group(0)
                            #    print result.group(1)
                            # Empty, e.g. `i18n:translate=""`:
#                            else:
#                                print "Please add missing message-id for i18n in:"
#                                print file_path
                    line = fil.readline()
                    line_nr = line_nr + 1
# Create pot-file of list:
pot = open('message_ids.pot', 'w')
for entry in pot_entries:
    pot.write(entry)
pot.close()
#DEV stats:
print 'py: ' + str(pies)
print 'js: ' + str(jies)
print 'pt: ' + str(ties)
print 'tot:' + str(entries)

