fhand = raw_input("Enter the file name: ")
inp = open(fhand)
count = 0
for file in inp :
	if file.startswith("From ") :
		lst = file.split()
		count = count + 1
		print lst[1]
print "There were", count, "lines in the file with From as the first word"		

