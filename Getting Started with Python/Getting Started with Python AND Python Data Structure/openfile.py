cr = "Hello\nWorld" # This is a newline code very useful.
print cr
drag = len(cr)


openfile = open("open_command.txt", "r") #This is a syntax you can see that
count = 0
for line in openfile: #This is a "forloop" we read through otherwise we cannot.
	print line
	count = count + 1
print "Lines", count
