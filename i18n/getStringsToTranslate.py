# !/usr/bin/python

# Get strings between '' or ""

wanted_file_types = ['.py', '.cpy', '.vpy']
IN_WORD = False
delimiter = ''
word = ''
words = []

# Walk recursively through directory:
for root, dirs, files in os.walk("."):
    # For each file:
    for file_name in files:
        print file_name
        file_path = os.path.join(root, file_name)
        splitted_name = os.path.splitext(file_name)
        if len(splitted_name) > 0:
            suff = splitted_name[1]
            if suff in wanted_file_types:
                with open(file_path) as fil:
                    line = fil.readline()
                    while(line):
                        for i in range(len(line)):
                            char = line[i]
                            print char
                            if char == '"' or char == "'":
                                if IN_WORD:
                                    if char == delimiter:
                                        IN_WORD = False
                                        words.append(word)
                                        word = ''
                                    else:
                                        word += char
                                else:
                                    IN_WORD = True
                                    delimiter = char
                            elif IN_WORD:
                                word += char
                        line = fil.readline()



###################################################
print words
###################################################
