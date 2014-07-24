# !/usr/bin/python

# Get some stats about file-types recursively of the directory where you execute:
# python getFileTypeStats.py

import os

wanted_file_types = ['.js', '.py','.pt','.cpt', '.xml', '.zpt', '.cpy', '.vpy']

unwanted_file_types = ['.dtml', '.patch', '.props', '.robot', '.ZPL', '.yml', '.c', '.pyc','.png','.txt', '.zcml', '.css', '.GPL', '.csv', '.in', '.gif', '.jpg', '.cfg', '.mo', '.po', '.pot', '.sample', '.rst', '.pack', '.idx', '.stx', '.swp', '.avi', '.ini', '.metadata', '.ico', '.3gp', '.py_tmpl', '.ini_tmpl', '.bat']

defined_file_types = wanted_file_types + unwanted_file_types

py_fy = 0
pg_tm = 0
zpgtm = 0
xml   = 0
js    = 0
to_ch = 0
summ  = 0

# Walk through directory recursively:
for root, dirs, files in os.walk("."):

    # For each file:
    for file_name in files:

        file_path = os.path.join(root, file_name)

        splitted_name = os.path.splitext(file_name)

        if len(splitted_name) > 0:

            suff = splitted_name[1]

            if suff in wanted_file_types:
                if suff == '.py':
                    py_fy += 1
                elif suff == '.zpt':
                    zpgtm += 1
                elif suff == '.pt':
                    pg_tm += 1
                elif suff == '.xml':
                    xml   += 1
                elif suff == '.js':
                    js    += 1
                else:
                    print suff
                    to_ch += 1

        else:
            print 'No extension-suffix for: ' + splitted_name


        if (  (suff not in defined_file_types) and (suff != '') ) :
            print 'Unknown file-extension-suffix: ' + suff

summ = py_fy + pg_tm + zpgtm + xml + to_ch

print 'We have ' + str(py_fy) + ' python-scripts, ' + str(pg_tm) + ' page-templates, ' + str(zpgtm) + ' zope-templates, ' + str(xml) + ' xml-configs, ' + str(js) +' javascripts and ' + str(to_ch)  + ' other (.cpt, .cpy, .vpy) to check. That is a total of ' + str(summ) + '.'
