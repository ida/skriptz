# TODO: i18n:attributes
# TODO: Regard, if there is no wrapping root-tag, holding all children.
# TODO: No msgid-dups.

# This script removes all i18n-attrs and adds 
# i18n:translate and i18n:name, where needed.

domain = 'amp.translations'

import sys
import os
import shutil

tag_types = ['opening', 'closing', 'selfclosing', 'comment']
tags_to_skip = ['head', 'script', 'style']
xid = 1

opened_tags = 1
needs_i18n_trans = []
needs_i18n_name = []
needs_i18n_attr = [] # TDO

def trimText(txt):
    if txt is None: txt = '' # ouch
    txt = txt.replace('\n','')
    txt = txt.replace('\t','')
    txt = ' '.join(txt.split())
    txt = txt.strip()
    return txt

def skipComment(pos):
    if len(food) > pos + 1:
        if food[pos+1] == '!':
            if len(food) > pos + 2:
                if food[pos+2] == '-':
                    if len(food) > pos + 3:
                        if food[pos+3]  == '-':
                            pos += 3
                            while len(food) > pos + 1:
                                pos += 1
                                if food[pos] == '-':
                                    if len(food) > pos + 1:
                                        pos += 1
                                        if food[pos]  == '-':
                                            if len(food) > pos + 1:
                                                pos += 1
                                                if food[pos]  == '>':
                                                    pos += 1
                                                    break
    return pos

def skipTag(tag_name, pos):
    tag_length = len(tag)
    while len(food) > pos + 1:
        pos += 1
        if tag[pos] and tag[pos+1:pos+tag_length+1] == tag_name:
            pos += tag_length + 2 # move behind bracket
        return pos

def getTag(pos):
    """ Returns the tag without brackets, 
        f.e. 'body class="bla"' or '/div'
    """
    tag = ''
    while len(food) > pos + 1:
        pos += 1
        tag += food[pos]

        # Collect everything inside of quotes
        # and move on cursor:
        if food[pos] == '"':
            while len(food) > pos +1:
                pos += 1
                tag += food[pos]
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

def getParentTag(pos):
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
            if openclose_ratio == 0:
                while len(food) > pos + 1:
                    pos += 1
                    if food[pos] == '<':
                        tag = getTag(pos)
                        tag_type = getTagType(tag)
                        if (tag_type == 'opening') or (tag_type == 'selfclosing'):
                            return pos
                        else:
                            pos = len(tag)
                return None

def getText(pos):
  p = pos;
  inTag = False
  isCloseTag = 0
  level=0
  inComment=False
  inQuote=False
  tag = ""
  stack = []
  result = ""
  currentLevel = -1
  lenn = len(food)
  while (p<lenn):
    if (inTag and food[p]=='"'):
        if (inQuote): inComment=inQuote=False
        else:         inComment=inQuote=True
    elif (food[p]=='>' and food[p-2]=='-' and food[p-1]=='-'):
        inTag = inComment = False
    elif (not inComment and food[p]=='>'):
        if (isCloseTag>0):
            level += 1
        elif (isCloseTag<0):
            level -= 1
        if (level<=0):
            return result # return
        inTag = False
    elif (not inComment and food[p]=='<'):
        isCloseTag = 1;
        inTag = True
    elif(not inComment and food[p]=='/'):
        isCloseTag=0;
        if(food[p-1]=='<'):
            isCloseTag = -1
    elif(not inQuote and food[p]=='!' and inTag):
        inComment = True
    elif(inTag):
        tag += food[p]
    elif(not inComment):
        if (currentLevel==-1 and level>0):
          currentLevel = level
        if (level==currentLevel):
          result += food[p]

    p += 1;

# Is first tag a sibling of another tag? Then it's not a wrapper-tag.
def prepare():
    chars_before_first_tag = ''
    ONE_TIME = False
    GRUEN = True
    FIRST_TAG = False
    pos = -1
    parent_tag = ''
    parent_text = ''
    while len(food) > pos + 1:
        pos += 1
        if not FIRST_TAG:
            chars_before_first_tag += food[pos]
        if food[pos] == '<':
            if not ONE_TIME:
                if getNextSibling(pos):
                    print 'Oh, oh, we don\'t have  root-tag!'
                ONE_TIME = True
            FIRST_TAG = True
            tag = getTag(pos)
            if chars_before_first_tag != '<':
                chars_before_first_tag = trimText(chars_before_first_tag)
                if chars_before_first_tag != '<':
                    GRUEN = False
            # Exceptionize special tags:
            if tag.split(' ')[0] not in tags_to_skip:
                tag_type = getTagType(tag)
                tag_text = trimText(getText(pos))
                parent_pos = getParentTag(pos)
                # Has parent:
                if parent_pos:
                    parent_tag = getTag(parent_pos)
                    parent_text = trimText(getText(parent_pos))
                ##################
                # i18n:translate #
                ##################
                if tag_type is 'opening' and tag_text is not '':
                    # We don't need i18n:translate, if tag is 
                    # created dynamically of a tal-statement:
                    if (tag.find('tal:content') == -1) and (tag.find('tal:replace') == -1):
                        needs_i18n_trans.append(pos) # match
                ##################
                #   i18n:name    #
                ##################
                if (parent_text != '') and ((tag_type is 'opening') or (tag_type is 'selfclosing')):
                    needs_i18n_name.append(pos) # match
    if not GRUEN:
        print "Oh, oh, there are characters before first tag starts:"
        print chars_before_first_tag[0:-1]

def append_string(result, string):
    
    # Regard pos for selfclosing tags needs to be one more left:
    SELFCLOSED = False
    if result.endswith('/'):
        SELFCLOSED = True
        result = result[:-1]
        if result.endswith(' '):
            result = result[:-1]

    length = len(string)
    pos = length
    i = 0
    while (i<length):
        result+=string[i]
        i+=1

    # Re-add removed chars of selfclosing:
    result = result
    if SELFCLOSED:
        result = result + '/'
    return result

def must_patch(pos):
    global xid
    result = ""
    length = len(needs_i18n_trans)
    i = 0
    while (i<length):
        if needs_i18n_trans[i]==pos:
            result += " i18n:translate=\"id-" + str(xid) + "\""
            xid += 1
            break
        i+=1

    length = len(needs_i18n_name)
    i = 0
    while (i<length):
        if needs_i18n_name[i]==pos:
            result += " i18n:name=\"name-"+str(xid) + "\""
            xid += 1
            break
        i+=1

    return result

def replace():
    prepare()

    pos = 0
    result = ""
    off = 0
    while (pos<len(food)):
        patch = must_patch(pos)
        result += food[pos]
        if (len(patch)>0):
            tag = getTag(pos);
            off = 0
            while(off<len(tag)):
                result += food[pos+off+1]
                off += 1
            pos+=len(tag)
            result = append_string(result, patch)
        pos += 1
    return result

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


########
# MAIN #
########
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
                                
                opened_tags = 1
                needs_i18n_trans = []
                needs_i18n_name = []
                needs_i18n_attr = [] # TDO

                with open(file_path) as fin, open(file_path + '.tmp', 'w') as fout:
                    food = fin.read()
                    food = removeExistingI18nAttrs(food)
                    food = addNamespaceAndDomain(food)
                    food = replace();
                    fout.write(food)
                    # Overwrite original with workingcopy:
                    shutil.move(file_path + '.tmp', file_path)
