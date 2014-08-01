#!/usr/bin/python
# Script to generate model-driven (XML) fieldentries
# for Plone's dexterity-contenttype-forms.
# Assumes you are in this directory: your.product/your/product/model
# Usage is: python addField.py yourmodel.xml yourfieldname fieldtype
# Cruft crafted by Ida Ebkes, <contact@ida-ebkes.eu>, 2013.

import os
import sys
import shutil

# If user enters less or more args than needed, give a hint:
if len(sys.argv) != 4:
    exit("\nThis didn't work out, usage is:\n\
python addField.py [formfile] [fieldname] [fieldtype]\n\
Aborting script-execution now, nothing has been changed, try again.\n")

# Set vars by fetching user's input:
formfile = sys.argv[1]
fieldname = sys.argv[2]
fieldtype = sys.argv[3]

# We want to insert the line after the schema-tag:
insert_after_pattern = '<schema>'
# Make sure tag exists:
if insert_after_pattern not in open(formfile).read():
    sys.exit("\nConflict: Cannot find a schema-tag in '%s', as expected.\n\
Aborting script-execution now, nothing has changed.\n"%formfile)

# Check, if fieldname exists already in formfile:
if fieldname in open(formfile).read():
    # Abort, if so:
    sys.exit ("\n\nConflict: Field '%s' exists already, aborting entry-creation now, nothing has changed.\n\n" %fieldname )

# Check, if fieldtype is valid:
# List from zope.schema-3.7.1/zope/schema/__init__.py:
# TODO: Extend with other field sources: plone.namedfile.field, 
# z3c.relationfield.schema and plone.app.textfield , like referenced on:
# http://developer.plone.org/reference_manuals/external/plone.app.dexterity/reference/fields.html
fieldtypes = [
'MinMaxLen',
'Choice',
'Bytes',
'ASCII',
'BytesLine',
'ASCIILine',
'Text',
'TextLine',
'Bool',
'Int',
'Float',
'Decimal',
'Tuple',
'List',
'Set',
'FrozenSet',
'Password',
'Dict',
'Datetime',
'Date',
'Timedelta',
'Time',
'SourceText',
'Object',
'URI',
'Id',
'DottedName',
'InterfaceField',
]

if fieldtype not in fieldtypes:
    print "\nConflict: '%s' is not a valid field-type, possible types are:\n"%fieldtype
    print fieldtypes
    sys.exit("\nAborting script-executing now, nothing has changed.\n")

# Convention: Use capitalized fieldname for title-tag:
fieldtitle = str.capitalize(fieldname)

fname = str(formfile)
f = open(fname, "a, r+")
fnameTmp = fname + '.tmp'
fTmp = open(fnameTmp, 'w')
line = f.readline()

# Write each line into a workingcopy,
# if keyword is found, insert text after:
while line:
    fTmp.write(line)
    if line.find('<schema>') != -1:
        fTmp.write("""\n\t<field name="%s" type="zope.schema.%s">\n\t\t<description />\n\t\t<title>%s</title>\n\t</field>
                    \n"""% (fieldname,fieldtype,fieldtitle) )
    line = f.readline()


# Finally move workingcopy (tmp) to original:
shutil.move(fnameTmp, fname)
print "\nSuccess: Created entry for field '%s' in '%s'.\n"\
        %(fieldname,formfile)
