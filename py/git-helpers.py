import os
from adi.commons.commons import *

def parseGitStatusReport(report_file):

    fname = None
    modified_files = []

    os.system('git status > ' + report_file)
    lines = getLines(report_file)
    for line in lines:
        line = line.strip()
        if line.startswith('modified:'):
            fname = line.split()[-1]
            modified_files.append(fname)

    delFile(report_file)
    return modified_files

def getModifiedFileNames(report_file):
    modified_files = parseGitStatusReport(report_file)
    return modified_files

def coma():
    modified_files = getModifiedFileNames('git-status-report.tmp')
    modified_files = ' '.join(modified_files)
    os.system('git commit -am "Update %s"'%modified_files)

coma()
