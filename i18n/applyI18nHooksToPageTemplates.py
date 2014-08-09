# !/usr/bin/python

# i18nize templates
# TODO: Check, if i18n:attributes are missing.

import os
import shutil
from bs4 import BeautifulSoup # pip install beautifulsoup4

msg_id = 0
msg_name = 0
wanted_file_types = ['.pt', '.zpt', '.cpt']
dikt = []
dikt = [  [ 'example_msg_id', 'example_msg_str', ['file1.pt', 'file2.pt'] ]  ]

for root, dirs, files in os.walk("."):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        splitted_name = os.path.splitext(file_name)
        if len(splitted_name) > 0:
            suff = splitted_name[1] 
            if suff in wanted_file_types:

                food = open(file_path)
                soup = BeautifulSoup(food, 'html.parser')
                tags = soup.find_all()
                
                # For each tag:
                for tag in tags:
                    HAS_TXT = False
                    NEED_TRANS = False
                    NEED_NAME = False
                    HAS_NAME = False
                    HAS_TRANS = False
                    PAR_HAS_TRANS = False
                    HAS_TAL = False
                    tag_contents = tag.contents 
                    tag_txt = ''
                    
                    for att in tag.attrs:
                        if att == 'tal:content':
                            HAS_TAL = True
                        elif att == 'tal:replace':
                            HAS_TAL = True
                        elif att == 'i18n:translate':
                            HAS_TRANS = True
                        elif att == 'i18n:name':
                            HAS_NAME = True

                    # First, delete all existing hooks:
                    if HAS_TRANS:
                        del tag['i18n:translate']
                    if HAS_NAME:
                        del tag['i18n:name']


                    ####################
                    #   check parent   #
                    ####################

                    for atti in tag.parent.attrs:
                        if atti == 'i18n:translate':
                            PAR_HAS_TRANS = True

                    if PAR_HAS_TRANS:
                        tag['i18n:name'] = 'name-' + str(msg_name)
                        msg_name += 1
                    
                    ####################
                    #   collect text   #
                    ####################

                    # Do I have text?
                    for content in tag_contents:
                    # tag.contents returns its (unicode-)text and 
                    # child-tags as list-items, e.g.:
# [u"\n    Tag's starting text\n    ", <childtag> childtext </childtag>', u'\n    ending text of tag\n    ']
                        # Yes, text please:
                        if isinstance(content, unicode):
                            # Remove linebreaks:
                            string = content.replace('\n','').strip()
                            # Remove superfluous (=more than one between words) spaces:
                            string = ' '.join(string.split()) # split'n'join: cool! no regex needed :)
                            if string != '':
                                tag_txt += string
                        else:
                            for at in content.attrs:
                                if at == 'i18n:name':
                                    tag_txt += ' ${' + content["i18n:name"] + '} '
                                    HAS_NAME = True
                            #if not HAS_NAME:
                            #    tag_txt += ' ${i18n:name} '
                        
                    # HAS TEXT:
                    if tag_txt != '':

                        # APPLY HOOKS:
                        if not HAS_TAL:
                            IS_DUP = False
                            for entry in dikt:
                                if entry[1] == tag_txt:
                                    entry[2].append(file_path)
                                    dup_msg_id = entry[0]

                                    IS_DUP = True

                            if not IS_DUP:
                                new_entry = [msg_id, tag_txt, [file_path]]
                                dikt.append(new_entry)
                                tag['i18n:translate'] = 'id-' + str(msg_id)
                                if msg_id < 4: print msg_id, tag.name
                                msg_id += 1
                            else:
                                tag['i18n:translate'] = 'id-' + str(dup_msg_id)

                    # End of tag, loop next. 
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
    pot += 'msgid="' + str(entry[0]) + '"\nmsgstr=""\n\n'
res = open('main.pot', 'w')
res.write(pot)
res.close()
