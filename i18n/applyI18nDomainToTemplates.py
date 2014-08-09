# !/usr/bin/python

# Removes all 'i18n:domain'-attributes of each file
# and applies our defined domain to each first tag
# of a file.

# Will apply to each file recursively of the dirctory
# where you execute `python applyI18nDomainToTemplates.py`

# Ida Ebkes, 2014, <contact@ida-ebkes.eu>

import os
import shutil
from bs4 import BeautifulSoup # pip install beautifulsoup4

wanted_file_types = ['.pt', '.zpt', '.cpt']
domain = 'our.translations'

# Walk through directory recursively:
for root, dirs, files in os.walk("."):

    # For each file:
    for file_name in files:

        file_path = os.path.join(root, file_name)

        splitted_name = os.path.splitext(file_name)

        if len(splitted_name) > 0:

            suff = splitted_name[1] # can be '.tar.gz'

            if suff in wanted_file_types:

                FILE_HAS_DOMAIN = False
# We specify the parser to use, to avoid mess-ups.
# F.e. if lxml is installed, it would be taken,
# which we don't want because prettify() then
# (see end of file) adds html- and body-tag,
# let's use Python's built-in parser 'html.parser',
# which doesn't add html+body-tags:
                food = open(file_path)
                soup = BeautifulSoup(food, 'html.parser')
                tags = soup.find_all()
                
                # For each tag:
                for tag in tags:
                    
                    ###################
                    #   i18n:domain   #
                    ###################

                    # We only want our domain once applied to first tag
                    # and nowhere else, because though shallt not have 
                    # other domains than mine besides me, the allmighty
                    # domain.

                    # Remove domain of all tags:
                    if HAS_DOMAIN:
                        del tag['i18n:domain']

                    # Apply domain to first tag:
                    if FILE_HAS_DOMAIN == False:
                        tag['i18n:domain'] = domain
                        FILE_HAS_DOMAIN = True
                
                # COOK IT: 
                soup = soup.prettify().encode('ascii', 'xmlcharrefreplace')
                result = open(file_path + '.tmp', 'w')
                result.write(str(soup))
                result.close()
                shutil.move(file_path + '.tmp', file_path)
