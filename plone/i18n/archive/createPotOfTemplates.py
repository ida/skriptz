# !/usr/bin/python

import os
import shutil
from bs4 import BeautifulSoup # pip install beautifulsoup4

wanted_file_types = ['.pt', '.zpt', '.cpt']
msg_id = ''
pot = ''
defaults = []

# Walk through directory recursively:
for root, dirs, files in os.walk("."):

    # For each file:
    for file_name in files:

        file_path = os.path.join(root, file_name)

        splitted_name = os.path.splitext(file_name)

        if len(splitted_name) > 0:

            suff = splitted_name[1] # can be '.tar.gz'

            if suff in wanted_file_types:

                food = open(file_path)
                soup = BeautifulSoup(food, 'html.parser')
                tags = soup.find_all()
                
                for tag in tags:
                    HAS_NAME = False
                    tag_txt = ''
                    for att in tag.attrs: 
                        if att == 'i18n:translate':    
                            msg_id = tag[att]            
                            for content in tag.contents:
                                
                                if isinstance(content, unicode):
                                    # Remove linebreaks:
                                    string = content.replace('\n','').strip()
                                    # Remove superfluous spaces:
                                    string = ' '.join(string.split())
                                    if string != '': 
                                        tag_txt += string
                                else:
                                    for at in content.attrs:
                                        if at == 'i18n:name':
                                            tag_txt = ' ${' + content["i18n:name"] + '} '
                                            HAS_NAME = True
                                    if not HAS_NAME:
                                        tag_txt = ' ${i18n:name} '
                    if tag_txt != '':                                        
                        pot += '#. Default: "' + tag_txt + '"\n\
#: ' + file_path + ':\n\
msgid "' + msg_id + '"\n\
msgstr ""\n\n'
                # COOK IT: 
                pot = pot.encode('ascii', 'xmlcharrefreplace')
                result = open('amp.translations.pot', 'w')
                result.write(str(pot))
                result.close()
                #shutil.move(file_path + '.tmp', file_path)
