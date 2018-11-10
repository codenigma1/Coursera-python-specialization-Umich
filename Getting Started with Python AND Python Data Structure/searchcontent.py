# Search through file any do u want search #####
file = open("open_command.txt")
for fle in file:
	fle = fle.rstrip() # remove whitespace in the file....ok
	if fle.startswith("from:"):
		print fle
