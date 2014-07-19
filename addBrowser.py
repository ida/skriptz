#!/usr/bin/python

# Adds a browser-boilerplate to an egg generated with zopeksel's
# "plone"-template, where "Include profile?" was answered with yes.

import os

LAYER_EXISTS = False
egg_name = ''

# Register browser-package:
with open('configure.zcml') as fin, open('configure.zcml.tmp', 'w') as fout:

    for line in fin:

        # Gett egg-name:
        if line.find('i18n_domain="') != -1:
            egg_name = line.split('"')
            egg_name = egg_name[1]

        # If exists already:
        if line.find('<include package=".browser" />') != -1:

            LAYER_EXISTS = True


        # Insert if not exists already:
        if line.find('</configure>') != -1 and not LAYER_EXISTS:

            fout.write('  <include package=".browser" />\n\n')


        fout.write(line)

# Boiling the plate:
if not os.path.exists('browser'):
    # Create browserpackage:
    os.makedirs('browser')
    # Create init:
    open('browser/__init__.py', 'w').close()
    # Create interface:
    interface_name = egg_name.split('.')
    interface_name = 'I' + str.capitalize(interface_name[0]) + str.capitalize(interface_name[1])
    interface = open('browser/interfaces.py', 'w')
    interface.write('from zope.interface import Interface\nclass ' + interface_name + '(Interface):')
    interface.close()
    # Create configure:
    configure = open('browser/configure.zcml', 'w')
    configure.write('\
<configure\n\
 xmlns="http://namespaces.zope.org/zope"\n\
 xmlns:five="http://namespaces.zope.org/five"\n\
 xmlns:browser="http://namespaces.zope.org/browser"\n\
 i18n_domain="'+egg_name+'">\n\
 <include package="plone.app.contentmenu" />\n\
</configure>')
    configure.close()
    # Create layer:
    layer = open('profiles/default/browserlayer.xml', 'w')
    layer.write('<?xml version="1.0"?>\n<layers>\n\t<layer name"' + interface_name + '"\n\
\t\tinterface="' + egg_name + '.browser.interfaces.' + interface_name + '" />\n\
\t</layer>\n</layers>')
    layer.close()
