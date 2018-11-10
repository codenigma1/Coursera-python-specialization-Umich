# This is a sample problem of dictionarie with simple idioms #
# what is largest word and value#
# This is steps for converted text into the list #

inp = raw_input("Open the file: ")
handle = open(inp, "r")
red = handle.read()
line = red.split()

# This is steps put into the dictionarie  and assign the value #

counts = dict()
for word in line :
	counts[word] = counts.get(word, 0) + 1
print counts	

# This is steps of find bigcount and bigword#

bigcount = None
bigword = None
for text,count in counts.items() :
	if bigcount is None or count > bigcount : # This conditin is very important to user understad look carefully#
		bigword = text
		bigcount = count
print bigword, bigcount		