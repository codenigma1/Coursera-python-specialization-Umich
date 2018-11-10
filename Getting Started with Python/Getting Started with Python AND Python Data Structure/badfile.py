# Read whole all fucking data of any file
file = raw_input("Enter the file name: ")
try :
	file1 = open(file)
except :
	print "File cannot open", file
	exit()
count = 0
for file2 in file1 :
	file2 = file2.strip()
	# Skip "unintersting lines in the file"
	if file2.startswith("from:") :
		count = count + 1
		file3 = file2
		print file3
	# Process our "interest" line
		print "There were", count, "subject line in", file3