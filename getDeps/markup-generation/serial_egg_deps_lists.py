# /usr/bin/python

# Get recursively dependencies of an egg and return a file 'list_snippet'.html
# containing all inolved eggs as an unordered html-list, followed flat one by another, each list containing an egg's
# declared dependencies of its requires.txt-file as list-items.

import glob, os, re

basket = '/home/edith/.buildout/eggs/'

all_eggs = [] # during collecting dependencies, registrate each egg here, if not already there

kol_eggs = [] # kollekt egg after html-list crea for later comparison, we don't want dup-lists

def get_versions(name):
""" Return egg's available versions in basket (eggs-cache-directory)
    as a flat list, collecting its system-paths with glob()
"""
    # First trim string: TODO: still necessary?
    if name.find('[') != -1: # remove possible part-declas in same line not at beginning
        nu_name = name.split('[')
        name = str(nu_name[0]).strip() # remove leftover whitespaces of in between
    
    paths = glob.glob(basket + name + '-*')
    
    if paths:
        versions = []
    
        for egg_path in paths:
                # versioin-number of between first two minus-chars:
                version = re.search('-(.*?)-', egg_path)
                version = version.group(1)
                versions.append(version)
    
    else: versions = ['No egg found']
    
    versions.sort(reverse=True) # newest first, oldest last
    
    return versions

def get_deps(name):
""" Return dependencies of an egg as a flat list of its requirements.txt-file
"""
    deps = []
    dep_name = ''
    dep_version = ''
    version = get_versions(name)[0] # only newest for now, TODO: extend for all versions
    paths = glob.glob(basket + str(name) + '-' + str(version) + '*')
    if paths:
        req_path = paths[0]
        req_file = req_path + '/EGG-INFO/requires.txt'
    else: req_file = 'No reqfile found'
    if(os.path.exists(req_file)):
        with open(req_file) as req:
            line = req.readline()
            while(line):
                line = line.rstrip('\n').strip()
                if line.startswith('['): # skip everything after a starting parts-decla(-line)
                    break
                elif not(line == ''): # exclude possible empty string after stripping lines which only contained a linebreak
                    match_object = re.search(r"[<>=]*[<>=]",line)
                    if match_object:
                        op_start = match_object.span()[0]
                        #op_end = match_object.span()[1]
                        #op     = str(line[op_start:op_end]).strip()
                        dep_name   = str(line[0:op_start]).strip()
                        #DEV: dep_version     = line[op_end:len(line)]
                        dep_version     = line[op_start:len(line)]
                    else:
                        dep_name = str(line).strip()
                        dep_versions     = get_versions(dep_name)
                        if dep_versions:
                            dep_version = dep_versions[-1] # newest
                    if not(dep_name is '' or dep_version is ''): # needed?
                        if dep_name.find('[') != -1: # remove possible part-declas in same line not at beginning
                            nu_dep_name = dep_name.split('[')
                            dep_name = str(nu_dep_name[0]).strip() #remove leftover whitespaces of in between
                        dep_entry = dep_name, dep_version
                        deps.append(dep_entry)
                        if dep_name not in all_eggs:
                            all_eggs.append(dep_name)
                line = req.readline()
    else: deps = 'No deps'
    return deps


def rekur_get_deps(name, version):
    while name not in kol_eggs:
        # Start:
        html = '<ul class="'+name+'">\n\t<li>'+name+'<span>'+version+'</span>\n\t\t<ul class="deps">\n'
        deps = get_deps(name)
        kol_eggs.append(name)
        # Middle:
        if deps == 'No deps':
            html += '\t\t\t<li>No deps</li>\n'
        else:
            for dep in deps:
                    html += '\t\t\t<li>'+str(dep[0])+'<span>'+str(dep[1])+'</span></li>\n'
        # End:
        html += '\t</ul>\n\t</li>\n</ul>\n'
        with open('list_snipppet.html', 'a') as dalist:
            dalist.write(html)
        for egg in all_eggs:
            if (egg not in kol_eggs):
                name = egg

rekur_get_deps('Products.CMFPlone','4.3.3')
