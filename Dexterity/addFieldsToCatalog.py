#!/usr/bin/python

# Creates indizi for Plone's portal_catalog,
# taken from a given dexterity-model-xml-file,
# f.e. in order to make fields available to topics.
# Assumes, you are in the same directory as your profiles-folder.
# Usage is: python createIndiziOfModel.py your_dexterity_model.xml
# Requires > Python-2.7.
# Cruft crafted by Ida Ebkes, <contact@ida-ebkes.eu>, 2013.
# License: Free as a bee and as in freedom, aka DTFWYW.

import os
import re
import sys
import shutil

# It's assumed we have a profiles-folder here:
if not os.path.exists('./profiles'):
    exit("\nProblem: Cannot find the assumed profiles-folder in this directory,\
\n aborting script-execution now, nothing has been changed.\n")

# If user enters less or more than required input, give a hint:
if len(sys.argv) != 2:
    print '\n'
    print "This didn't work out, usage is:\n"
    print "python addFieldsToCatalog.py path/to/your_dexterity_form_model.xml\n"
    print 'Aborting script-execution now, nothing has been changed, try again.'
    print '\n'
    exit()

# Fetch user's input:
formfile = sys.argv[1]

# Create a catalog.xml, if not existing already:
if not os.path.exists('./profiles/default/catalog.xml'):
    skel_string = '<?xml version="1.0"?>\
\n<object name="portal_catalog" meta_type="Plone Catalog Tool">\
\n<!-- Add indexes here on penalty of death or worse, see:\
\nhttp://maurits.vanrees.org/weblog/archive/2009/12/catalog -->\
\n</object>'
    catalog_file = open('./profiles/default/catalog.xml', 'w')
    catalog_file.write(skel_string)
    catalog_file.close()
    print "\nCreated catalog.xml in profiles/default"

# Collect fields and their meta_types from xml-model:
fieldnames = []
metatypes = []
f = open(formfile)
line = f.readline()
while line:
    if line.find('<field name="') != -1:
        # Assumes apostroph after 'name', is the first 
        # apostroph in the line, which works here.
        # Note: adding more characters in first pattern would 
        # return also these chars (removing only last char 
        # of first pattern but all of second pattern):
        fieldname=line[line.find('"')+1:line.find('" type="')]
        fieldnames.append(fieldname)
        # A much sharper result gives this, thanks to:
        # http://stackoverflow.com/questions/3368969/find-string-between-two-substrings
        result = re.search('type="(.*)"', line)
        metatype = result.group(1)
        metatypes.append(metatype)
    line = f.readline()


# Provide working-copy in order to be able to search and write line-by-line:
source = './profiles/default/catalog.xml'
target = './profiles/default/catalog.xml.tmp'

# Write field-entries:
for fieldname in fieldnames:

    # TODO: Check metatype and apply fitting index, f.e.
    # 'FieldIndex' for text, 'DateIndex' for dates, etc.
    # For now, we take a static value:
    metatype = 'FieldIndex'

    with open(source) as fin, open(target, 'w') as fout:

        FOUND = False

        for line in fin:
            # Check, if field-entry exists already:
            #match = re.search(r'word:\w\w\w', line)
            match = re.search(fieldname, line)
            if match:
                FOUND = True
                print "Skipping entry for", fieldname, "already exists."
            # Look for the line, where string should be inserted before:
            else:
                if line.strip() == '</object>' and FOUND == False:

                    # Finally write the entry:
                    fout.write('\n\t<index name="%s" meta_type="%s">\n\t\t<indexed_attr value="%s" />\n\t</index>\n\n'%(fieldname,metatype,fieldname) )
                    print "Created entry for", fieldname, "."
            # Write line of source-file (original) to target-file (workingcopy):
            fout.write(line)

        # Last but not least, overwrite original with workingcopy,
        # including the new entry:
        shutil.move(target, source)
print "End of script-execution."
