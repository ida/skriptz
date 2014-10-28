#TDO: exclude comments
import os

def trimStr(string):
	string = string.replace('\n', '')
	string = string.replace('\t', '')
	strings = string.split(' ')
	string = ''
	for s in strings:
		if s  != '':
			string += s
			if strings[-1] != s:
				string += ' '
	return string

def getMsgStr(pos, food, deli):
    para = ''
    msg = [] # [id, def]
    msg_id = ''
    msg_def = ''
    while len(food) > pos + 1:
        pos += 1
        if food[pos] == deli:
            break
        msg_id += food[pos]
    msg_id = trimStr(msg_id)
    # Has id and default:
    if food[pos+1] == ',':
        pos += 1
        while food[pos] == ' ' or food[pos] == '\n' or food[pos] == '\t': #ignore spaces at beginning
            pos += 1
            while len(food) > pos + 1:
                pos += 1
                para += food[pos]
                if food[pos] == '"' or food[pos] == "'":
                    deli = food[pos]
                    while len(food) > pos + 1:
                        pos += 1
                        if food[pos] == deli:
                            break
                        msg_def += food[pos]
    # No default:
    else:
        msg_def = msg_id

    # Escape quotations:
    msg_id = msg_id.replace('"', '\\"')
    msg_def = msg_def.replace('"', '\\"')
    return [msg_id, msg_def]

def getMsgsDict():
    deli = None
    msgs_dict = [] # [def_str, [paths], id, str]
    msg_strs = []
    msg_str = ''

    for root, dirs, files in os.walk("."):
            for file_name in files:
                if file_name.endswith('py') or file_name.endswith('js'):
                    file_path = os.path.join(root, file_name)
                    if file_path.find('/tests/') == -1:
                        food = open(file_path).read()
                        pos = -1
                        while len(food) > pos + 1:
                            pos += 1
                            if food[pos] == '_':
                                if len(food) > pos+1:
                                    pos += 1
                                    if file_name.endswith('js'):
                                        if food[pos] == '_':
                                            pos += 1
                                    if food[pos] == '(':
                                        pos += 1
                                        while food[pos] == ' ' or food[pos] == '\n' or food[pos] == '\t': #ignore spaces at beginning
                                            pos += 1
                                        if food[pos] == 'u':
                                            pos += 1
                                        if food[pos] == '"' or food[pos] == "'":
                                            deli = food[pos]
                                            msg = getMsgStr(pos, food, deli)
                                            msg_id = msg[0]
                                            msg_str = msg[1]
                                            if msg_str != '':
                                                if msg_str in msg_strs: # is dup
                                                    for entry in msgs_dict: # get dup
                                                        if entry[0] == msg_str:
                                                            entry[1].append('#' + file_path) # add path
                                                else: # no dup, fresh entry:
                                                    entry = [ '# ' + msg_str, ['#' + file_path], 'msgid "' + msg_id + '"', 'msgstr ""' ]
                                                    msgs_dict.append(entry)
                                                msg_strs.append(msg_str)

    return msgs_dict

def writePot():
    lines = []
    mdict = getMsgsDict()
    print len(mdict)
    for entry in mdict:
        lines.append(entry[0])
        lines.append('\n')
        for child in entry[1]:
            lines.append(child)
            lines.append('\n')
        lines.append(entry[2])
        lines.append('\n')
        lines.append(entry[3])
        lines.append('\n')
        lines.append('\n')

    pot = open('ofPyAndJs.pot', 'w')
    for line in lines:
        pot.write(line)
    pot.close()

writePot()

def mergePots():
    pt_pot = open('pot.pot').read()
    py_js_pot = open('ofPyAndJs.pot').read()
    merge_pot = pt_pot + py_js_pot
    mpot = open('merge.pot', 'w')
    mpot.write(merge_pot)
    mpot.close()
mergePots()
