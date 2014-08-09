# !/usr/bin/python

# i18nize template.s
# TODO: Check, if i18n:attributes are missing.
import os
import shutil
from bs4 import BeautifulSoup # pip install beautifulsoup4

msg_id = 0
msg_name = 0
wanted_file_types = ['.pt', '.zpt', '.cpt']

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
                    tag_contents = tag.contents 
                    tag_txt = ''
                    HAS_TAL = False
                    
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
                            if string != '': tag_txt += string
                    if tag_txt != '':
                    #    if not (tag_txt.startswith(' ${') and tag_txt.endswith('} ')):
                        HAS_TXT = True
                    
                    #######################
                    #   apply i18n-hook   #
                    #######################

                    for atti in tag.parent.attrs:
                        if atti == 'i18n:translate':
                            PAR_HAS_TRANS = True

                    if HAS_TXT and not HAS_TAL:
                        NEED_TRANS = True
                    if PAR_HAS_TRANS:
                        NEED_NAME = True
                    if HAS_TAL:
                        NEED_NAME = True
                    
                    if NEED_TRANS:
                        tag['i18n:translate'] = 'id' + str(msg_id)
                        msg_id += 1
                    elif NEED_NAME:
                        tag['i18n:name'] = 'name' + str(msg_name)
                        msg_name += 1
           
                    # End of tag, loop next. 
                
                # COOK IT: 
                soup = soup.prettify().encode('ascii', 'xmlcharrefreplace')
                result = open(file_path + '.tmp', 'w')
                result.write(str(soup))
                result.close()
                shutil.move(file_path + '.tmp', file_path)
