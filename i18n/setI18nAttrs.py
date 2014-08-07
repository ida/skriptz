# !/usr/bin/python

import os
import shutil
from bs4 import BeautifulSoup

msg_nm = 0
msg_id = 0
wanted_file_types = ['.pt']
domain = 'amp.translations'

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

                    #
                    # i18n
                    #
                   
                    # Needs i18n:attribute ? Tags with title, alt 
                    # or value do, collect them:
		    HAS_i18n_ATT = False
		    need_i18n_att = []
                    dont_need_i18n_att = []
		    attis = tag.attrs

                    for atti in attis:
                        if (atti == 'title') or (atti == 'alt') or (atti == 'value'):
			    # Has a val:
			    if len(tag[atti]) > 1:
				# It's not a var:
			    	if tag[atti][0] != '$'and tag[atti][1] != '{':
			            need_i18n_att.append(atti)

			# Overriden by tal-att or i18n-att already set? Ignore them later:
			if atti == ('i18n:attributes' or 'tal:attributes'):
                            atts = tag[atti]
                            atts = atts.split(';')
                            for att in atts:
                                att = att.strip()
                                att = att.split(' ')[0]
				dont_need_i18n_att.append(att)
		    	    if atti == 'i18n:attributes':
				HAS_i18n_ATT = True

		    # Compare and set i18n:attribute:
		    string = ''
		    for need in need_i18n_att:
                	if need not in dont_need_i18n_att:
			    string += ' ' + need + ';'
		    if string != '':
               	    	if HAS_i18n_ATT:
			    string = tag['i18n:attributes'] + string
		    	else:
			    string = string.strip()
			    tag['i18n:attributes'] = string 
	        
		if tag.name == 'input':
		    HAS_TIT = False
		    ats = tag.attrs
		    for at in ats:
			if at == 'value':
			    HAS_TIT = True
		    if HAS_TIT == False:
			print tag
			print file_path

                soup = soup.prettify().encode('ascii', 'xmlcharrefreplace')
                result = open(file_path + '.tmp', 'w')
                result.write(str(soup))
                result.close()
		shutil.move(file_path + '.tmp', file_path)
