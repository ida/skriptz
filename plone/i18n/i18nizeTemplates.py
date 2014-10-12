#dup msgids
import os

domain = 'our.translations'
pot ='the.pot'

tags_to_skip = ['html', 'head', 'style', 'script']

needs_trans = []
needs_name = []
msg_dict = []


def readPot(pot):
    with open(pot) as fin:
        for line in fin:
            if line.startswith('msgid "'):
                msgid = line[7:-2]
            if line.startswith('msgstr "'):
                msgstr = line[8:-2]
                msg_dict.append([msgid, msgstr])

def writePot():
    feed = ''
    for entry in msg_dict:
        feed += 'msgid "' + entry[0] + '"\nmsgstr "' + entry[1] + '"\n\n'
    nupot = open('nu.pot', 'w')
    nupot.write(feed)
    nupot.close()

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
                return tag

    # Not a comment:
    else:
        while len(food) > pos + 1:
            pos += 1
            tag += food[pos] #write

            # Collect everything (also '<') inside 
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
    if tag.startswith('!--'):
        return 'comment'
    elif tag.startswith('/'):
        return 'closing'
    elif tag.endswith('/'):
        return 'selfclosing'
    else:
        return 'opening'

def skipTag(pos): # DEV: not used currently, keeping for ref
    """ Moves pos behind closing tag of tag.
    """
    opencloseratio = 1
    tag = getTag(pos)
    tag_type = getTagType(tag)

    pos += len(tag) + 1 # move behind bracket

    if getTagType(getTag(pos)) == 'opening' or getTagType(getTag(pos)) == 'closing':
        while len(food) > pos + 1:
            pos += 1
            if food[pos] == '<':
                if getTagType(getTag(pos)) == 'opening':
                    opencloseratio += 1
                elif getTagType(getTag(pos)) == 'closing':
                    opencloseratio -= 1
                
                pos += len(getTag(pos)) + 1 # move behind bracket
            
            if opencloseratio == 0:
                break 

    return pos

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

def stripVars(string):
    IN_VAR = False
    stripped = ''
    i = -1
    while len(string) > i + 1:
        i += 1

        if string[i] == '$':
            if (len(string) > i + 1) and (string[i+1] == '{'):
                IN_VAR = True
                i += 1

        if (string[i] == '}') and IN_VAR:
            IN_VAR = False

        if (not IN_VAR) and (string[i] != '}'):
            stripped += string[i] # write

        stripped = trimText(stripped)

    return stripped

def getMsgStrAndCollectNeeds(pos):
    msgstr = ''
    opencloseratio = 1
    tag_pos = pos
    tag = getTag(pos)
    pos += len(tag) + 1 # +1 cause len starts with 1, list with 0

    while len(food) > pos + 1:
        pos += 1

        # Write:
        if food[pos] != '<' and  opencloseratio == 1:
                msgstr += food[pos]       

        # Tag closes:
        if opencloseratio == 0:
            break

        # Found child:
        if food[pos] == '<':
            nxt_tag = getTag(pos)
            nxt_type = getTagType(nxt_tag)

            # Count ratio:
            if nxt_type == 'opening':
                opencloseratio += 1
            elif nxt_type == 'closing':
                opencloseratio -= 1

            ######################################        
            #             i18n:name              #        
            ######################################        
            # Write substitute:
            if (nxt_type== 'opening' and opencloseratio == 2) or \
               (nxt_type== 'selfclosing' and opencloseratio == 1):
                numsgnm = ''
                msgnm = getI18nName(nxt_tag)
                # i18n:name set already:
                if msgnm != '':
                    msgstr += '${' + msgnm  + '}'
                # not set, apply:
                else:
                    if pos not in needs_name:
                        needs_name.append(pos)
            # Move on:
            pos += len(nxt_tag) + 1
            
    ######################################        
    #           i18n:translate           #        
    ######################################        
    # Apply i18n:translate, if neccessary:
    stripped_msgstr = trimText(msgstr)
    if stripped_msgstr != '':
        NEED_TRANS = True
        # Exclude single vars:
        if stripped_msgstr.startswith('${') and stripped_msgstr.endswith('}'):
            # Exclude only vars and no text, assuming we don't want this:
            text = stripVars(stripped_msgstr)
            if text == '':
                NEED_TRANS = False
        if NEED_TRANS:
            if tag_pos not in needs_trans:
                needs_trans.append(tag_pos)

    return msgstr


def collectNeeds(food):
    pos = -1
    while len(food) > pos+1:
        pos += 1
        if food[pos] == '<':
            if (getTagType(getTag(pos)) == 'opening') and (getTag(pos).split(' ')[0] not in tags_to_skip):
                getMsgStrAndCollectNeeds(pos)

def writeNames(food):
    digest = ''
    nmnr = 1
    pos = -1
    while len(food) > pos+1:
        pos += 1
        digest += food[pos]
        if pos in needs_name:
            tag = getTag(pos)
            digest += tag
            if getTagType(tag) == 'selfclosing':
                digest = digest[:-1]
            digest += ' i18n:name="name-' + str(nmnr) + '"'
            if getTagType(tag) == 'selfclosing':
                digest += ' /'
            nmnr += 1
            pos += len(tag)# move on
    return digest

def writeTranslates(food):
    digest = ''
    idnr = 1
    pos = -1
    while len(food) > pos+1:
        pos += 1
        digest += food[pos]
        if pos in needs_trans:

            msgid = ''
            msg = getMsgStrAndCollectNeeds(pos)
            msg = trimText(msg)
            ids = []
            # No dup msgs:
            for entry in msg_dict:
                ids.append(entry[0])
                if entry[1] == msg:
                    msgid = entry[0]
            # New id:
            if msgid == '':
                msgid = 'id-' + str(idnr)
                # No dup id:
                if msgid in ids:
                    while msgid in ids:
                        idnr += 1
                        msgid = 'id-'+ str(idnr)

                idnr += 1
                msg_dict.append([msgid, msg])

            tag = getTag(pos)
            digest += tag
            if getTagType(tag) == 'selfclosing':
                digest = digest[:-1]
            digest += ' i18n:translate="' + msgid + '"'
            if getTagType(tag) == 'selfclosing':
                digest += ' /'
            idnr += 1
            pos += len(tag)# move on
    return digest

def writeTransen(food):
    digest = ''
    msgid = ''
    idnr = 1
    pos = -1
    while len(food) > pos+1:
        pos += 1
        digest += food[pos]
        if pos in needs_name:
            msg = getMsgStrAndCollectNeeds(pos)
            # No dups:
            for entry in msg_dict:
                if entry[1] == msg:
                    msgid = entry[0]
            if line.startwith('msgid "'):
                msgid = line[6:-1]
            # New id:
            if msgid == '':
                msgid = 'id-' + str(idnr)
                idnr += 1

            tag = getTag(pos)
            digest += tag
            digest += ' i18n:translate="' + msgid + '"'
            pos += len(tag) # move on

    return digest

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
        pos += 1
        if food[pos] == '<':
            tag = getTag(pos)
            tag_type = getTagType(tag)
            if tag_type == 'opening':
                opencloseratio += 1
            if tag_type == 'closing':
                opencloseratio -= 1
            pos += len(tag)

    if opencloseratio == 0:
        return True
    else:
        return False

#MAIN
readPot(pot)
wanted_file_types = ['.pt', '.cpt', '.zpt']
# Walk recursively through directory:
for root, dirs, files in os.walk("."):
    # For each file:
    for file_name in files:

        # Get current file-path, for later overwrite:
        file_path = os.path.join(root, file_name)

        # Get suffix:
        splitted_name = os.path.splitext(file_name)
        if len(splitted_name) > 0:
            suff = splitted_name[1]

            # It's a pagetemplate:
            if suff in wanted_file_types:

                with open(file_path) as fin, open(file_path+".tmp", 'w') as fout:
                    food = fin.read()
                    print isValidMarkup(food)
                    if isValidMarkup(food):
                        food = removeExistingI18nAttrs(food)
                        food = addNamespaceAndDomain(food)
                        collectNeeds(food)
                        food = writeNames(food)
                        needs_trans = needs_name = [] # reset
                        collectNeeds(food)
                        food = writeTranslates(food)
                        fout.write(food)
                        # Overwrite original with workingcopy:
#                    shutil.move(file_path+".out", file_path)
                    else:
#if isValidMarkup(food) == False:
                        print 'Erm, this template seems to be frogged up, doesn\'t validate!'
print msg_dict
writePot()
