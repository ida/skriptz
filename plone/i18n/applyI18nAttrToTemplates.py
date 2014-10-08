import sys
import os
import shutil

tag_types = ['opening', 'closing', 'selfclosing', 'comment']
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

def getTag(pos):
    """ Returns the tag without brackets, 
        f.e. 'body class="bla"' or '/div'
    """
    tag = ''
    while len(food) > pos + 1:
        pos += 1
        while food[pos] != '>': # TDO: ignore '>' in between "", could be py-ex
            tag += food[pos]
            if len(food) > pos + 1:
                pos += 1
            else:
                pos += 1
                break
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
    return 0

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

def prepare():
    LOOP = True
    pos = -1
    while LOOP and len(food) > pos + 1:
        pos += 1
        if food[pos] == '<':

            tag = getTag(pos)
            tag_type = getTagType(tag)
            tag_text = getText(pos)
            tag_text = trimText(tag_text)
            parent_pos = getParentTag(pos)
            xtext = getText(parent_pos)
            parent_text = trimText(xtext)

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
            # We always need an i18n:name, if parent has text:
            if tag_type is 'opening' and parent_text != '':
                needs_i18n_name.append(pos) # match

def append_string(result, string):
    length = len(string)
    pos = length
    i = 0
    while (i<length):
        result+=string[i]
        i+=1

    return result

def must_patch(pos):
    global xid
    result = ""
    length = len(needs_i18n_trans)
    i = 0
    while (i<length):
        if needs_i18n_trans[i]==pos: 
            k=pos
            attrs = ""
            while (k<len(food)):
                if (food[k]=='>'): break;
                k += 1
                attrs += food[k]

            result += " i18n:translate=\"id-"+str(xid)+"\""
            xid += 1
            break
        i+=1

    length = len(needs_i18n_name)
    i = 0
    while (i<length):
        if needs_i18n_name[i]==pos: 
            result += " i18n:name=\"name-"+str(xid)+"\""
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

# MAIN:
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

                with open(file_path) as fin, open(file_path+".out", 'w') as fout:
                    food = fin.read()
                    res = replace();
                    fout.write(res)
                    # Overwrite original with workingcopy:
                    shutil.move(file_path+".out", file_path)

