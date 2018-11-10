# Read whole all fucking data of any file 
file = open("open_command.txt")
for fle in file :
	fle = fle.rstrip()
	# Skip "unintersting lines in the file"
	if not "@gmail.com" in fle:
		print fle