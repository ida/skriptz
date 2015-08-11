# TODO: handle backslashes in collected strs
import os
import shutil

#DEVdomain = 'our.translations'
domain = 'amp.translations'

pot = domain+ '.pot' # Path to pot-file

if not os.path.exists(pot):
    open(pot, 'w').close()

# This will run over all dirs, can be also several eggs.
# In our case we want only eggs starting with the first part
# of our namespace (here: 'our') to be included.
# Set prefix below to '', if you want to  grasp all dirs.
prefix = domain.split('.')[0] + '.' # include dot for sharp results later
#prefix = ''

skip_tags = ['html', 'head', 'style', 'script', 'tal:comment', 'metal:comment']

g_idnr = 1
g_nmnr = 1
msg_dict = []

def readPot(pot):
    with open(pot) as fin:
        for line in fin:
            if line.startswith('msgid "'):
                msgid = line[7:-2]
            if line.startswith('msgstr "'):
                msgstr = line[8:-2]
                msg_dict.append([msgid, msgstr])

def writePot(pot):
    feed = ''
    for entry in msg_dict:
        feed += 'msgid "' + entry[0] + '"\nmsgstr "' + entry[1] + '"\n\n'
    pot = open(pot, 'w')
    pot.write(feed)
    pot.close()

def getTag(pos):
    """ Returns the tag without brackets,
        f.e. 'body class="bla"' or '/div'
    """
    tag = ''

    # Special case comments:
    if len(food) > pos + 3 and food[pos:pos+3] == '!--':
        while len(food) > pos + 1:
            pos += 1
            tag += food[pos]
            if food[pos] == '-' and len(food) > pos + 3 and food[pos:pos+3] == '-->':
                tag += food[pos]
                print tag
                return tag

    # Not a comment:
    else:
        while len(food) > pos + 1:
            pos += 1
            tag += food[pos] #write

            # Collect everything (also '>') inside 
            # of quotes and move on cursor:
            if food[pos] == '"':
                while len(food) > pos +1:
                    pos += 1
                    tag += food[pos] #write
                    if food[pos] == '"':
                        break
            # Tag stops and we are not in quotes:
            elif food[pos] == '>':
                # Remove closing bracket:
                tag = tag[:-1]
                break

    return tag

def getTagType(tag):
    # Can be also '<!DOCTYPE html>' or '<?xml version="1.0">'.
    if tag.startswith('!') or tag.startswith('?'): 
        return 'comment'
    elif tag.startswith('/'):
        return 'closing'
    elif tag.endswith('/') or tag.startswith('meta') or tag.startswith('link'):
        return 'selfclosing'
    else:
        return 'opening'

def getParentTag(pos): # Not used, but keeping it for reference.
    inComment=False
    inQuote=False
    inTag = False
    closingPos = -1
    pos -= 1
    level=0
    while pos > -1:
        if (inTag and food[pos]=='"'):
            if (inQuote): inComment=inQuote=False
            else:         inComment=inQuote=True
        elif not inQuote and food[pos]=='>':
            inTag = True
            closingPos = pos
        elif not inQuote and food[pos]=='<':
            if food[pos+1]!='/' and closingPos>0 and food[closingPos-1]!='/':
                level+=1
            elif food[pos+1]=='/':
                level-=1
            closingPos = -1
            inTag=False

        if level==1:
            return pos

        pos -= 1
    return None

def getNextSibling(pos):
    """ Expects an opening tag to be passed.""" 
    openclose_ratio = 1
    pos += len(getTag(pos))
    while len(food) > pos + 1:
        pos += 1
        if food[pos] == '<':
            
            tag = getTag(pos)
            tag_type = getTagType(tag)
            pos += len(tag)
            
            if tag_type == 'opening':
                openclose_ratio += 1
            elif tag_type == 'closing':
                openclose_ratio -= 1
            elif tag_type == 'comment':
                pos += len(tag) + 1

            if openclose_ratio == 0:
                while len(food) > pos + 1:
                    pos += 1
                    if food[pos] == '<':
                        tag = getTag(pos)
                        tag_type = getTagType(tag)
                        if (tag_type == 'opening') or (tag_type == 'selfclosing'):
                            return pos
                        else:
                            pos = len(tag) + 1
                return None

def getChildren(pos):
    """ Expects an opening tag to be passed.""" 
    
    children = []
    opencloseratio = 0
    
    tag = getTag(pos)

    pos += len(tag) + 1
    
    while len(food) > pos + 1:
        
        pos += 1
        
        if food[pos] == '<':
            
            tag = getTag(pos)
            tag_type = getTagType(tag)
            
            if tag_type == 'opening':
                opencloseratio += 1
                
                if opencloseratio == 1:
                    children.append(pos) #collect child
            
            
            elif tag_type == 'closing':
                opencloseratio -= 1
            
            elif tag_type == 'selfclosing' and opencloseratio == 0:
                children.append(pos) #collect child

            if opencloseratio == -1:
                break
            
            pos += len(tag)

    return children


def trimText(txt):
    """ Removes linebreaks and tabs,
        any whitespace more than one between words,
        and all whitespaces preceding or trailing the str.
    """
    if txt is None: txt = '' # ouch
    txt = txt.replace('\n','')
    txt = txt.replace('\t','')
    txt = ' '.join(txt.split())
    txt = txt.strip()
    return txt

def getText(pos):
    """Returns the text of a tag, ignores children."""
    text = ''
    pos += len(getTag(pos)) + 1
    opencloseratio = 1
    while len(food) > pos + 1:
        pos += 1
        if opencloseratio == 1 and food[pos] != '<':
            text += food[pos]  # write
        if food[pos] == '<':
            tag = getTag(pos)
            if len(food) > pos + 2:
                pos += len(tag) + 2 # move behind closing bracket
            else:
                pos += len(tag) + 1
            tag_type = getTagType(tag)
            
            if tag_type == 'opening':
                opencloseratio += 1
            elif tag_type == 'closing':
                opencloseratio -= 1
        
        if opencloseratio == 0:
            break
    text = trimText(text)

    return text


def getMsgStr(pos):
    """Returns msgstr, substitutes children with name-vars."""
    text = ''
    pos += len(getTag(pos)) + 1
    opencloseratio = 1
    while len(food) > pos + 1:
        pos += 1
        
        if opencloseratio == 1 and food[pos] != '<':
            text += food[pos]  # write
        
        if food[pos] == '<':
            tag = getTag(pos)
            tag_type = getTagType(tag)
            pos += len(tag) + 1 # move on closing bracket
            
            if tag_type == 'opening':
                opencloseratio += 1
                    
            elif tag_type == 'closing':
                opencloseratio -= 1

            if (tag_type == 'selfclosing') \
            or (tag_type == 'opening' and opencloseratio == 2):
                name = getI18nName(tag)
                text += '${' + name  + '}'


            pos += 1 # move behind closing bracket
        
        if opencloseratio == 0:
            break
    
    text = trimText(text)

    return text



def getI18nName(tag):
    name = ''
    IN_NAME = False
    p = -1
    while len(tag) > p:
        p += 1
        # We have an i18n:name-attr:
        if len(tag) > p + 11 and tag[p:p+11] == 'i18n:name="':
            # Move to first quote:
            p += 11
            IN_NAME = True
        # Write:
        if IN_NAME:
            name += tag[p]
        # Ending quotes:
        if IN_NAME and (tag[p] == '"'):
            break
    # Remove last quote:
    name = name[:-1]

    return name


def removeExistingI18nAttrs(food):
    feed = ''
    pos = -1
    while len(food) > pos + 1:
        pos += 1
        feed += food[pos] # Write each char

        # Ignore i18n, except namespace-decla and i18n:attrs:
        if food[pos:pos+5] == 'i18n:' and food[pos-1] == ' ' and food[pos+5] != 'a':
            # Remove already collected starting 'i' and space before:
            feed = feed[:-2]
            # Move on position:
            while (len(food) > pos + 1):
                pos += 1
                if food[pos] == '"':
                    while (len(food) > pos + 1):
                        pos += 1
                        if food[pos] == '"':
                            break
                    break
    return feed

def addNamespaceAndDomain(food):
    feed = ''
    xmlns = ''
    nspace = ''
    idomain = ' i18n:domain="' + domain + '"'
    pos = -1
    APPLIED = False
    while len(food) > pos + 1:
        pos += 1
        feed += food[pos] # Write each char
        if food[pos] == '<' and APPLIED == False:
            tag = getTag(pos)
            if getTagType(tag) == 'opening':
                if tag.startswith('html'):
                    if tag.find('xmlns="') == -1:
                        xmlns = ' xmlns="http://www.w3.org/1999/xhtml"'
                    if tag.find('xmlns:i18n') == -1:
                        nspace = ' xmlns:i18n="http://xml.zope.org/namespaces/i18n"'

                feed += tag + xmlns + nspace + idomain
                APPLIED = True
                pos += len(tag)

    return feed

def isValidMarkup(food):
    opencloseratio = 0
    pos = -1
    while len(food) > pos+1:
        if food[pos] == '<':
            tag = getTag(pos)
            tag_type = getTagType(tag)
            if tag_type == 'opening': #TODO: Skip head, style and link.
                opencloseratio += 1
            if tag_type == 'closing':
                opencloseratio -= 1
            pos += len(tag) + 1
        pos += 1

    if opencloseratio == 0:
        return True
    else:
        opencloseratio = 0
        return False

def hasRoot(food):
    pos = -1
    while len(food) > pos+1:
        pos += 1
        if food[pos] == '<':
            tag = getTag(pos)
            tag_type= getTagType(tag)
            if tag_type == 'opening':
                if getNextSibling(pos):
                    return False
                else:
                    return True
            elif tag_type == 'selfclosing':
                return False
            elif tag_type == 'closing':
                print 'Holy moly, template seems to start with a closing tag!'
            else:
                pos + len(tag) + 1

def collectNeeds(food):
    needs_trans = []
    needs_name = []
    pos = -1
    while len(food) > pos + 1:
        pos += 1

        if food[pos] == '<':
            tag = getTag(pos)
            tag_type = getTagType(tag)
            if (tag_type == 'opening') \
            and (tag not in skip_tags) \
            and (tag.find('use-macro') == -1) \
            and (tag.find('tal:comment') == -1) \
            and (tag.find('tal:replace') == -1) \
            and (tag.find('tal:content') == -1):
                tag_text = getText(pos)
                # Needs trans:
                if tag_text != '':
                    needs_trans.append(pos)
                    # Children need name:
                    children = getChildren(pos)
                    for child in children:
                        needs_name.append(child)

            pos += len(tag) + 1 #move on bracket
    
    return needs_name, needs_trans

def writeNames(food, g_nmnr):
    nmnr = g_nmnr
    needs =collectNeeds(food)
    needs_name = needs[0]
    needs[0]
    digest = ''
    pos = -1
    while len(food) > pos + 1:
        pos += 1
        digest += food[pos] # write

        if pos in needs_name:
            tag = getTag(pos)
            digest += tag
            pos += len(tag) + 1
            tag_type = getTagType(tag)
            if tag_type == 'selfclosing':
                digest = digest[:-1]

            digest += ' i18n:name="name-' + str(nmnr) + '"'
            if tag_type == 'selfclosing':
                digest += ' /'
            nmnr += 1
            pos -= 1

    g_nmnr = nmnr

    return [digest, g_nmnr]

def writeTrans(food, g_idnr):
    idnr = g_idnr
    needs_trans = collectNeeds(food)[1]
    digest = ''
    pos = -1
    while len(food) > pos + 1:
        pos += 1
        digest += food[pos] # write

        if pos in needs_trans:

            tag = getTag(pos)
            digest += tag
            msgid = ''
            msgstr = getMsgStr(pos)
            
            pos += len(tag) + 1
            
            # No dups:
            for entry in msg_dict:
                if entry[1] == msgstr:
                    msgid = entry[0]
            
            # New id:
            if msgid == '':
                msgid = 'id-' + str(idnr)
                idnr += 1
                msg_dict.append([msgid, msgstr])

            
            # Write trans:
            digest += ' i18n:translate="' + msgid + '"'
            pos -= 1

    return [digest, idnr]


############
#   MAIN   #
############
readPot(pot)
wanted_file_types = ['.pt', '.cpt', '.zpt']
# Walk recursively through directory:
for root, dirs, files in os.walk("."):
    # For each file:
    for file_name in files:

        # Get current file-path, for later overwrite:
        file_path = os.path.join(root, file_name)

        # Regard possible prefix, if prefix is '', all
        # files will be considered:
        if file_path.startswith('./' + prefix) and not file_path.startswith('./' + domain + '/') \
        and not file_path.startswith('amp.ezupgrade') \
        and not file_path.startswith('amp.model') \
        and not file_path.startswith('amp.pas') \
        and not file_path.startswith('amp.ussa_api'): #DEV

            # Get suffix:
            splitted_name = os.path.splitext(file_name)
            if len(splitted_name) > 0:
                suff = splitted_name[1]

                # It's a pagetemplate:
                if suff in wanted_file_types:

                    with open(file_path) as fin, open(file_path + ".tmp", 'w') as fout:
                        food = fin.read()
                        if isValidMarkup(food):
                            # Heavy manipulations:
                            if not hasRoot(food):
                                food = '<div class="rootTagWrapper">' + food + '</div>'
                            food = removeExistingI18nAttrs(food)
                            food = addNamespaceAndDomain(food)
                            names = writeNames(food, g_nmnr)
                            food = names[0]
                            g_nmnr = names[1]
                            trans = writeTrans(food, g_idnr)
                            food = trans[0]
                            g_idnr = trans[1]
                            fout.write(food) # write
                            # Overwrite original with workingcopy:
                            shutil.move(file_path + ".tmp", file_path)
                        else:
#                            print '! The following template does have more or less opening than closing tags:'
#                            print file_path
                            # Remove leftover workingcopy:
                            os.remove(file_path + '.tmp')
writePot(pot)
