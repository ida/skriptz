# What
# ====
# Create an html-doc with a table-like list of all packages on PyPi,
# containing the passed term in their names, including their total
# download-numbers, using `pip` and `vanity`: A huge thanks here to
# Alex Clark and  quite some more brave Pythonistas for those modules.
#
# Why
# ===
# All we are is dust in the wind.
#
# How
# ===
# After downloading this, open a terminal and locate to the script and do:
# $ python getPyPiStats.py collective.
# Where 'collective.' is the term we search for. You'll should then find an
# html-doc in the same directory (folder) where this script lives.
# 
# Further vanity
# ==============
# Scrabbled by Ida Ebkes, August 2016.

import os
import sys
import datetime
from os import system as exe

def installPip(virtenv_path):
    """Install and update pip in a virtualenv to have a fresh env to start."""
    if not os.path.exists(virtenv_path):
        exe('virtualenv ' + virtenv_path + '; pip install pip -U')

def installVanity(virtenv_path):
    """Install and update pip in a virtualenv to have a fresh env to start."""
    if not os.path.exists(virtenv_path):
        exe('virtualenv ' + virtenv_path + '; pip install pip -U')

def getPckgsWithTermInName(term, virtenv_path):
    """Search for term on pypi, return pckg-names as a list."""
    pckgs = []
    exit_code = None
    results_file = 'results.txt'

   # Search pckgs with term in name and pour results into a file:
    command = virtenv_path + '/bin/pip search ' + term + ' > ' + results_file
    exit_code = exe(command)
    if exit_code != 0: exit('Error! Exitcode is "' + str(exit_code) + '".')

    # Read file line by line and extract pckgs:
    lines = open(results_file).readlines()
    for line in lines:
        if line.startswith(term):
            pckgs.append(line.split(' ')[0])
    return pckgs

def getDownloadsOfPckg(pckg_name):
    downloads = None
    results_file = 'download_results.txt'
    find_pattern = pckg_name + ' has been downloaded '
    exe('vanity ' + pckg_name + ' 2> ' + results_file)
    lines = open(results_file).readlines()
    for line in lines:
        if line.startswith(find_pattern):
            downloads = line.split(find_pattern)[1].split(' ')[0]
    return downloads

def genHtlm(pckgs):
    total_downloads = 0
    html = """<html><head><style type="text/css">
    body > div:first-child {
        border-bottom: 1px dotted;
        margin-bottom: 2em;
    }
    body > div:first-child > div:last-child > div:first-child,
    body > div > div:first-child {
        font-weight: bold;
    }
    div div div {
        display: inline-block;
        width: 49%;
        border-top: 1px dotted;
    }
</style></head><body>
<div>
    <div>
        <div>
            Package-name
        </div>
        <div>
            Downloads
        </div>
    </div>"""
    for pckg in pckgs:
        downloads = getDownloadsOfPckg(pckg)
        if downloads: total_downloads += int(''.join(downloads.split(',')))
        else: downloads = 'None'
        html += '''
    <div>
        <div>
            <a title="Link to ''' + pckg + ''' on PyPi"
               href="https://pypi.python.org/pypi/''' + pckg + '''">
                ''' + pckg + '''
            </a>
        </div>
        <div>
            ''' + downloads + '''
        </div>
    </div>'''
    html += """
    <div>
        <div>
            Total downloads:
        </div>
        <div>
            """ + str(total_downloads)[:-3] + """,""" +\
                  str(total_downloads)[-3:] + """
        </div>
    </div>
</div>
<div>
    Generated with:
    <a alt="Link to helper-script"
       href="https://github.com/ida/skriptz/blob/master/py/getPypiStats.py">
       https://github.com/ida/skriptz/blob/master/py/getPypiStats.py
    </a>
</div>
<div>
    Generated on: """ + str(datetime.datetime.now())[:16] + """
</div>
</body>
</html>"""
    open('results.html', 'w').write(html)
    return html

def main(term):
#    installPip()
#    installVanity()
    pckgs = getPckgsWithTermInName(term, '~/.virtenv')
    genHtlm(pckgs)

if __name__ == '__main__':
    term = sys.argv[1]
    main(term)

