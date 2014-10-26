po = open('ger.po').read()
pot = open('pot.pot').read()

def getMsgsDict(food):
	msgs_dict = []
	msg_def = ''
	msg_id = ''
	msg_str = ''
	FIRSTLINE = True
	lines = food.splitlines()
	for line in lines:
		# Remove preceding and trailing whitespaces:
		line = line.strip()
		if FIRSTLINE:
			FIRSTLINE = False
			msg_def = line[2:]
		if line.startswith('msgid "'):
			msg_id = line[7:-1]
		if line.startswith('msgstr "'):
			msg_str = line[8:-1]
		if line == '':
			FIRSTLINE = True
			msgs_dict.append([msg_def, msg_id, msg_str]) 
	return msgs_dict

def createNuPo():
	nupo = open('nu.po', 'w')
	lines = pot.splitlines()
	po_dict = getMsgsDict(po) #[[def,id,str],]
	nu_line = ''
	pot_str = ''
	mstr = ''
	FIRSTLINE = True
	# Read every line in pot:
	for line in lines:
		if FIRSTLINE:
			FIRSTLINE = False
			def_str = line[2:-1]
			# Compare, if we have a german trans:
			for entry in po_dict:
				if entry[0] == def_str:
					mstr = entry[2]
					# Yes we do, add trans to nupo:
					nu_line = 'msgstr "' + mstr + '"'
					break #needed?
		if line == '':
			FIRSTLINE = True
		if line.startswith('msgstr "') and nu_line !=  '':
			line = nu_line
			nu_line = ''
		nupo.write(line + '\n')
	nupo.close()
createNuPo()
