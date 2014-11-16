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

def getComment(pos, food):
	""" Returns everything until '-->' is encountered."""
	comment = ''
	while len(food) > pos+1:
		pos += 1
		# Collect each char...
		comment += food[pos]
		# ... until comment ends:
		if food[pos] == '-' and (len(food) > pos+2 and food[pos:pos+2] == '-->'):
			comment += food[pos+1] # should be a '-'
			break # It's called break-up, 'cause it's broken.
	return comment

def getTag(pos, food):
	""" Returns a tag without brackets."""
	IN_QUOTES = False
	tag = ''

	# Firstly, regard the special case comments:
	if len(food) > pos + 3 and food[pos+1:pos+3] == '!--':
		tag = getComment(pos, food)
		return tag

	# Not a comment, go on:
	while len(food) > pos+1:
		pos += 1

		# Check for end of tag: If we encounter a closing bracket and
		# we're not inside of a quotation (=attr's val), that's it.
		if food[pos] == '"': # TDO: Regard single quotes, as well.
			if IN_QUOTES: IN_QUOTES = False
			else: IN_QUOTES = True
		if not IN_QUOTES and food[pos] == '>':
			break # Tag ends here.
		
		# Collect each char until loop breaks (= we meet end of tag):
		tag += food[pos]

	return tag


def getTagType(tag):
	"""Expects the tag without brackets and it's not a comment-tag."""

	# TDO: Do we need to regard spaces? For now, assume that's not given.

	# Tags, which don't need to declare a closure:
	implicitly_closing = ['meta', 'link']

	tag_type = None

	if tag.startswith('/'):
		tag_type = 'closing'
	# Also regard '<?xml', '<!DOCTYPE':
	elif tag.endswith('/') or tag.startswith('!') or tag.startswith('?') or tag.split(' ')[0] in implicitly_closing:
		tag_type = 'selfclosing'
	# Comments, they are so special:
	elif tag.startswith('!--'):
		tag_type = 'comment'
	else:
		tag_type = 'opening'

	return tag_type	


def getTags(food):
	""" Returns a list of tags' start-positions."""
	tags = []
	pos = -1
	while len(food) > pos+1:
		pos += 1
		if food[pos] == '<':
			tag = getTag(pos, food)
			tags.append(pos)
			pos += len(tag) + 1 # Move on.
	return tags

def getTagContent(pos, food):
	""" Expects an opening tag, returns everything between opening- and closing-tag."""
	
	tag_content = ''

	opencloseratio = 1 # One tag is opened.

	tag = getTag(pos, food)
	tag_name = tag.split(' ')[0]

	pos += len(tag) + 1 # Move on.

	while len(food) > pos+1:
		pos += 1

		# Next tag starts:
		if food[pos] == '<':
			nxt_tag = getTag(pos, food)
			nxt_tag_type = getTagType(nxt_tag)

			# Collect ratio:
			if nxt_tag_type == 'opening':
				opencloseratio += 1
			elif nxt_tag_type == 'closing':
				opencloseratio -= 1

		# Break loop, when end-tag is reached:
		if opencloseratio == 0:
			pos += len(nxt_tag) + 1 # Move on.
			break
		
		# Collect every char, as long as loop loops:
		tag_content += food[pos]

	return tag_content

def getI18nAtt(tag, att_name):
	pos = -1
	val = ''
	att_start = 'i18n:' + att_name + '="'
	att_len = len(att_start)

	if tag.find(att_start) != -1: # tag has att

		while len(tag) > pos + 1:
			pos += 1
			if len(tag) > pos + att_len and tag[pos:pos+att_len] == att_start:
				pos += att_len # move on
				while len(tag) > pos + 1 and tag[pos] != '"':
					val += tag[pos]
					pos += 1
	else:
		return ''#TDO: None
	return val

def getMsgStr(tag_content):
	""" Expects a tag's complete html-content, substitutes first children with vars."""
	msg_str = ''
	text = '' # msg_str without vars
	opencloseratio = 0
	pos = -1
	while len(tag_content) > pos+1:
		pos += 1
		# Found child:
		if tag_content[pos] == '<':
			# Check conditions:
			child = getTag(pos, tag_content)
			child_type = getTagType(child)
			if child_type == 'opening':
				opencloseratio += 1
				# Write var:
				if opencloseratio == 1:
					msg_str += '${' + getI18nAtt(child, 'name') + '}'
			elif child_type == 'closing':
				opencloseratio -= 1
			elif child_type == 'selfclosing':
				# Write var:
				msg_str += '${' + getI18nAtt(child, 'name') + '}'
			# Move on:
			pos += len(child) + 1
		# Write text:
		if opencloseratio == 0 and tag_content[pos] != '>':
			text += tag_content[pos]
			msg_str += tag_content[pos]

	msg_str = trimStr(msg_str)
	text = trimStr(text)
	return msg_str, text

def getMsgDict():
    DUP = False
    same_str_dif_id = []
    msg_dict = [] # [ [ msgid, msgstr, [paths] ], ]
    tags_to_skip = ['head', 'meta', 'link', 'script', 'style', ]

    for root, dirs, files in os.walk("."):
        for file_name in files:
            if file_name.endswith('pt'):
                file_path = os.path.join(root, file_name)
                food = open(file_path).read()

                tags = getTags(food)
                for pos in tags:
                    tag = getTag(pos, food)
                    if tag.split(' ')[0] == 'script':
                        print tag

# MAIN
getMsgDict()
# EOF
