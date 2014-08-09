# !/usr/bin/python
#
#
# i18nize Plone-templates
# =======================
#
# Overwrites and adds i18:domain, i18n:translate and
# i18n:name-attributes for each tag in each file of this
# directory recursively  and creates a POT-file in it, 
# named 'our.domain.pot'.
#
# Usecase: Have one translation-egg holding the domain and translations
# for several eggs (f.e. your dev-eggs), centrally.
#
# Usage is: Install BeautifulSoup (f.e. with `pip install
# beautifulsoup4´), replace the domain-variable below with
# yours, execute ´python applyi18nHooksToTemplates.py` via
# your Terminal (possibly a bash) in the directory where you
# want the files to be altered.
#
# Consider a backup or a VCS-snapshot to be able to return to, 
# *before* executing this file, in case things go haywire.


# TODO: Check, if i18n:attributes are missing.

import os
import shutil
from bs4 import BeautifulSoup

wanted_file_types = ['.pt', '.cpt', '.zpt']
# Replace this var with the domain you want to apply:
domain = 'our.domain'
# Generate msg-ids and -names of increasing number:
msg_id = 0
msg_name = 0
# In dikt we collect msg_ids, their default text
# and a nested list of each file where the msg-id occurs:
dikt = []

# Walk recursively through directory:
for root, dirs, files in os.walk("."):

    # For each file:
    for file_name in files:
        
        # Get current file-path, for later overwrite:
        file_path = os.path.join(root, file_name)
        
        # Get suffix:
        splitted_name = os.path.splitext(file_name)
        if len(splitted_name) > 0:
            suff = splitted_name[1]
            
            # It's a pagetemplate:
            if suff in wanted_file_types:

                food = open(file_path)
                soup = BeautifulSoup(food, 'html.parser')
                tags = soup.find_all()
                
                # For each tag in this template:
                for tag in tags:
                    
                    # Ini/reset vars:
                    HAS_NAME = False
                    HAS_TRANS = False
                    PAR_HAS_TRANS = False
                    HAS_TAL = False
                    tag_txt = ''
                    
                    # Collect tag-attrs:
                    for att in tag.attrs:
                        if att == 'tal:content':
                            HAS_TAL = True
                        elif att == 'tal:replace':
                            HAS_TAL = True
                        elif att == 'i18n:translate':
                            HAS_TRANS = True
                        elif att == 'i18n:name':
                            HAS_NAME = True
                        elif att == 'i18n:domain':
                            HAS_DOMAIN = True

                    # Delete all i18-hooks:
                    if HAS_TRANS:
                        del tag['i18n:translate']
                    if HAS_NAME:
                        del tag['i18n:name']
                    if HAS_DOMAIN:
                        del tag['i18n:domain']

                    # Apply i18:name:
                    for atti in tag.parent.attrs:
                        if atti == 'i18n:translate':
                            PAR_HAS_TRANS = True
                    if PAR_HAS_TRANS:
                        tag['i18n:name'] = 'name-' + str(msg_name)
                        msg_name += 1

                    # Collect text:
                    for content in tag.contents:
# ´tag.contents´returns the tag's texts and child-tags as list-items, e.g.:
# [u"\n    Tag's starting text\n    ", <childtag> childtext </childtag>', u'\n    ending text of tag\n    ']
                        
                        # We have a piece of text:
                        if isinstance(content, unicode):
                            # Remove linebreaks and 
                            # preceding or trailing spaces:
                            string = content.replace('\n','').strip()
                            # Remove superfluous spaces, meaning 
                            # any more than one between words:
                            string = ' '.join(string.split())
                            if string != '':
                                tag_txt += string
                        
                        # We have a child-tag, include in 
                        # ´tag_txt´ as var:
                        else:
                            for at in content.attrs:
                                if at == 'i18n:name':
                                    # Add preceding and ending space:
                                    tag_txt += ' ${' + content[at] + '} '
                        
                    # TAG HAS TEXT:
                    if tag_txt != '':

                        # Remove preceding and ending space
                        # in case text starts or ends with 
                        # a i18n:name-var, that had added spaces
                        # two lines of code above:
                        
                        tag_txt = tag_txt.strip()
                        
                        
                        # APPLY i18n:translate:
                        
                        if not HAS_TAL:
                        
                            IS_DUP = False # ini

                            if dikt != []:
                                for entry in dikt:
                                    if entry[1] == tag_txt:
                                        entry[2].append(file_path)
                                        dup_msg_id = entry[0]
                                        IS_DUP = True

                            if not IS_DUP:
                                # Collekt entry in dikt:
                                new_entry = [msg_id, tag_txt, [file_path]]
                                dikt.append(new_entry)
                                # SET i18n:translate-msgid:
                                tag['i18n:translate'] = 'id-' + str(msg_id)
                                msg_id += 1
                            else:
                                # SET:
                                tag['i18n:translate'] = 'id-' + str(dup_msg_id)

                    # End of tag, loop to next tag.

                # COOK IT: 
                soup = soup.prettify().encode('ascii', 'xmlcharrefreplace')
                result = open(file_path + '.tmp', 'w')
                result.write(str(soup))
                result.close()
                shutil.move(file_path + '.tmp', file_path)

# Create pot-file of dikt:
pot = ''
for entry in dikt:
    pot += '# ' + entry[1] + '\n'
    for fil in entry[2]:
        pot += '# ' + fil + '\n'
    pot += 'msgid="id-' + str(entry[0]) + '"\nmsgstr=""\n\n'
pot = pot.encode('ascii', 'xmlcharrefreplace') 
res = open(domain + '.pot', 'w')
res.write(str(pot))
res.close()
