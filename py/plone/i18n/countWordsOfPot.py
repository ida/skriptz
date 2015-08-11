FIRSTLINE = True
entries = -1
words = 0
food = open('pot.pot').read()
lines = food.splitlines()
for line in lines:
	if FIRSTLINE:
		entries += 1
		FIRSTLINE = False
		line = line[2:-1]
		word = ''
		for char in line:
			word += char
			if char == ' ':
				words += 1
		words += 1
	if line == '': 
		FIRSTLINE = True
words= 300
entries=50
flow = float(float(words)/float(entries))
flow = str(flow).split('.')
aver = flow[0] + '.' + flow[1][0:2] # max 2 deci-digis

print 'We have ' + str(words) + ' words in '+ str(entries) + ' entries, that\'s an average of ' + aver + ' words per entry.' 
