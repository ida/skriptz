# !/usr/bin/python

# Eyecandy for templates, regular indentations.
# Will apply recursively to all files in this directory.
# Usage is: `python prettifyTemplates.py`
# Knitted by Ida Ebkes, 2014, <contact@ida-ebkes.eu>
 
import os
import shutil
from bs4 import BeautifulSoup # pip install beautifulsoup4

wanted_file_types = ['.pt', '.zpt', '.cpt']

# Walk through directory recursively:
for root, dirs, files in os.walk("."):

    # For each file:
    for file_name in files:

        file_path = os.path.join(root, file_name)

        splitted_name = os.path.splitext(file_name)

        if len(splitted_name) > 0:

            suff = splitted_name[1] # can be '.tar.gz'

            if suff in wanted_file_types:

# We specify the parser to use, to avoid mess-ups.
# F.e. if lxml is installed, it would be taken,
# which we don't want because prettify() then
# (see end of file) adds html- and body-tag,
# let's use Python's built-in parser 'html.parser',
# which doesn't add html+body-tags:
                food = open(file_path)
                soup = BeautifulSoup(food, 'html.parser')
                food.close()

                # Such a beautiful, beautiful markup:                
                soup = soup.prettify().encode('ascii', 'xmlcharrefreplace')
                
                result = open(file_path + '.tmp', 'w')
                result.write(str(soup))
                result.close()
                shutil.move(file_path + '.tmp', file_path)
