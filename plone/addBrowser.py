#!/usr/bin/python

# Adds a browser-boilerplate to an egg generated with zopeskel's 
# "plone"-template, where "Include profile?" was answered with yes.

import os, shutil

LAYER_EXISTS = False
conf = 'configure.zcml'
conftmp = conf + '.tmp'

egg_name = None
setup_file = '../../setup.py'

# Get egg-name:
with open(setup_file) as fin:
    for line in fin:
        if line.find('setup(name=') != -1:
            egg_name = line.split("'")[1]

# Register browser-package in configure:
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


# Boiling the plate:
if not os.path.exists('browser'):

    # Create browser-directories:
    os.makedirs('browser/resources')

    # Create init:
    open('browser/__init__.py', 'w').close()

    # Create interface:
    interface_name = egg_name.split('.')
    interface_name = 'I' + str.capitalize(interface_name[0]) + str.capitalize(interface_name[1])
    interface = open('browser/interfaces.py', 'w')
    interface.write('from zope.interface import Interface\n\n\
class ' + interface_name + '(Interface):\n\
    """Interface for layer-specific customisation.\n\
    """')
    interface.close()

    # Create configure:
    firstname = egg_name.split('.')[0]
    lastname = egg_name.split('.')[1]
    template_name = firstname + '_' + lastname + '_view'
    configure = open('browser/configure.zcml', 'w')
    configure.write('\
<configure\n\
 xmlns="http://namespaces.zope.org/zope"\n\
 xmlns:five="http://namespaces.zope.org/five"\n\
 xmlns:browser="http://namespaces.zope.org/browser"\n\
 i18n_domain="'+egg_name+'">\n\n\
    <include package="plone.app.contentmenu" />\n\n\
    <browser:resourceDirectory\n\
        name="'+egg_name+'.resources"\n\
        directory="resources"\n\
      />\n\n\
    <browser:page\n\
        for="*"\n\
        name="' + template_name + '"\n\
        class="' + egg_name + '.browser.' + template_name + '.' + interface_name[1:] + '"\n\
        permission="zope2.View"\n\
        layer=".interfaces.'+interface_name+'"\n\
      />\n\n\
</configure>')
    configure.close()


    # Create view:
    view = open('browser/' + template_name + '.py', 'w')
    view.write('\
# -*- coding: utf-8 -*-\n\n\
from Products.Five.browser import BrowserView\n\
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile\n\
from zope.interface import implements\n\n\
from ' + egg_name + '.browser.interfaces import ' + interface_name + '\n\n\
class ' + interface_name[1:] + ':\n\
    template = ViewPageTemplateFile("resources/' + template_name + '.pt")\n\
    implements(' + interface_name + ')\n')
    view.close()

    # Create template:
    template = open('browser/resources/' + template_name + '.pt', 'w')
    template.write(template_name + ' successfully loaded!')
    template.close()

    # Create layer:
    layer = open('profiles/default/browserlayer.xml', 'w')
    layer.write('\
<?xml version="1.0"?>\n\
<layers>\n\
    <layer name="' + interface_name + '"\n\
        interface="' + egg_name + '.browser.interfaces.' + interface_name + '">\n\
    </layer>\n\
</layers>')
    layer.close()


    # Register javascript:
    jsreg = open('profiles/default/jsregistry.xml', 'w')
    jsreg.write('\
<object name="portal_javascripts">\n\
 <javascript authenticated="False" cacheable="True" compression="none"\n\
    conditionalcomment="" cookable="True" enabled="True" expression=""\n\
    id="++resource++'+egg_name+'.resources/main.js" inline="False"/>\n\
</object>')
    jsreg.close()

    # Add javascript:
    js = open('browser/resources/main.js', 'w')
    js.write('\
(function($) {\n\
    $(document).ready(function() {\n\
        alert("'+egg_name+'.resources.main.js loaded");\n\
    });\n\
})(jQuery);')
    js.close()

# EOF
