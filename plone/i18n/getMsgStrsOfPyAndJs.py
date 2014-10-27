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

def getMsgStr(pos, food):
    deli = None
    msg_str = ''
    while food[pos] == ' ' or food[pos] == '\n' or food[pos] == '\t': #ignore spaces at beginning
        pos += 1
    if food[pos] == 'u':
        pos += 1
    deli = food[pos]
    while len(food) > pos + 1:
        pos += 1
        if food[pos] == deli:
            break
        msg_str += food[pos]
#    print msg_str
    msg_str = trimStr(msg_str)
    return msg_str

def getMsgStrs():
    msg_strs = []
    msg_str = ''

    for root, dirs, files in os.walk("."):
            for file_name in files:
                if file_name.endswith('py') or file_name.endswith('js'):
                    file_path = os.path.join(root, file_name)
                    if file_path.find('/tests/') == -1:
                        food = open(file_path).read()
                        #print food
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
                                        msg_strs.append(getMsgStr(pos, food))

    print len(msg_strs)
    return msg_strs
getMsgStrs()
