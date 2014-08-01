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
                HAS_TAL = False
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

                    # Add/replace domain to first tag:
                    if HAS_DOMAIN == False:
                        tag['i18n:domain'] = 'amp.translations'
                        HAS_DOMAIN = True

                    # HAS_TAL ?
                    # We can't get unconform attrs like `tal` directly with `tag.has_attr()`,
                    # so let's iterate over attrs to see, if it's exist:
                    attis = tag.attrs
                    for atti in attis:
                        if atti == ('tal:content' or 'tal:replace'):
                            # We can't change attr on the fly, set a flag:
                            HAS_TAL = True

                    # Not a TAL?
                    if not HAS_TAL:
                    	if tag.string:
                    	    if tag.string.strip('\n') != '':
                        	tag['i18n:translate'] = msg_id
                        	msg_id += 1

                    else:
                        tag['i18n:name'] = msg_nm
                        msg_nm += 1

                soup = soup.prettify().encode('ascii', 'xmlcharrefreplace')
                result = open(file_path + '.tmp', 'w')
                result.write(str(soup))
                result.close()
		shutil.move(file_path + '.tmp', file_path)
