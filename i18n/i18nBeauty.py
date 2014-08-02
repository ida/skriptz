# !/usr/bin/python

import os
import shutil
from bs4 import BeautifulSoup

msg_nm = 0
msg_id = 0
wanted_file_types = ['.pt']
domain = 'our.translations'

# Walk through directory recursively:
for root, dirs, files in os.walk("."):

    # For each file:
    for file_name in files:

        file_path = os.path.join(root, file_name)

        splitted_name = os.path.splitext(file_name)

        if len(splitted_name) > 0:

            suff = splitted_name[1]

            if suff in wanted_file_types:

                HAS_DOMAIN = False
# We specify the parser to use to avoid mess-ups,
# f.e., if lxml is installed it would be taken,
# which we don't want because prettify() then
# (see end of file) adds html- and body-tag,
# let's use Python's built-in parser 'html.parser':
                food = open(file_path)
                soup = BeautifulSoup(food, 'html.parser')
                tags = soup.find_all()

                for tag in tags:

                    HAS_TAL = False
                    HAS_i18n_ATT = False
                    NEEDS_i18n_ATT = False

                    # Add/replace domain to first tag:
                    if HAS_DOMAIN == False:
                        tag['i18n:domain'] = 'amp.translations'
                        HAS_DOMAIN = True

                    # HAS_TAL which needs translation ?
                    # We can't get unconform attrs like `tal` directly with `tag.has_attr()`,
                    # so let's iterate over attrs to see, if it exist:
                    attis = tag.attrs
                    for atti in attis:
                        if atti == ('tal:content' or 'tal:replace'):
                            # We can't change attr on the fly, set a flag:
                            HAS_TAL = True

                    # NO TAL:
                    if not HAS_TAL:
                    	if tag.string:
                            # HAS TXT:
                    	    if tag.string.strip('\n') != '':
                                # APPLY i18n:translate
                                tag['i18n:translate'] = msg_id
                                msg_id += 1
                    # HAS TAL:
                    else:
                        # APPLY i18n:name
                        tag['i18n:name'] = msg_nm
                        msg_nm += 1

                    #
                    # i18n
                    #
                   
                    HAS_i18n_ATT = False
                     
                    # Needs i18n:attribute ? Tags with title, alt 
                    # or value do, collect them:
                    rel_atts = []
                    for atti in attis:
                        if (atti == 'title') or (atti == 'alt') or (atti == 'value'):
                            rel_atts.append(atti)
                   
                    # Is title, alt or value overridden by a tal:attribute ?
                    need_atts = []
                    tal_att = ''
                    for atti in attis:
                        if atti == ('tal:attributes'):
                            HAS_i18n_ATT = True 
                            tal_atts = tag['tal:attributes']
                            tal_atts = tal_atts.split(';')
                            for tal_att in tal_atts:
                                tal_att = tal_att.strip()
                                tal_att = tal_att.split(' ')[0]
                                if tal_att not in rel_atts:
                                    need_atts.append(tal_att)

                    # Apply i18n:attribute, if needed:
                    if need_atts != []:
                        string = ''
                        # Tag doesn't have i18n:attributes 
                        # already, apply it alltogether:
                        if HAS_i18n_ATT == False:
                            for need in needs_atts:
                                string += need + '; '
                            tag['i18n:attributes'] = string
                        # Tag has i18n:attributes already,
                        # compare needed with existing and 
                        # apply leftover needed:
                        else:
                            for atti in attis:
                                if atti == 'i18n:attributes':
                                    # Get atts and vals of i18n:attributes:
                                    i18n_attis = tag['i18n:attributes'] # 'id foo; alt foo;'
                                    i18n_attis = i18n_attis.strip()
                                    i18n_attis = i18n_attis.split(';')
                                    for att in i18n_attis:
                                        # Get att for comparing, forget val:
                                        att = att.split(' ')[0]
                                        # Remove alrady existing 
                                        # atts in i18n:attributes
                                        # of needed:
                                        if att in need_atts:
                                            need_atts.remove(att)
                            
                                        if need_atts != [] and tag['i18n:attributes'] != '':
                                            
                                            string += tag['i18n:attributes']
                                            string = string.strip()
                                            if string[-1] != ';':
                                                string += ';'
                                            
                                            for att in need_atts:
                                                string += ' ' + att + ';'  
                                        tag['i18n:attributes'] = string
                
                
                soup = soup.prettify().encode('ascii', 'xmlcharrefreplace')
                #result = open(file_name + '.tmp', 'w')
                #result.write(str(soup))
                #result.close()
		#shutil.move(file_path + '.tmp', file_path)
