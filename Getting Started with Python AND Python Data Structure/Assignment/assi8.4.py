fhand = raw_input("Enter the file name: ")
inp = open(fhand)
result1 = list()
for line in inp :
	lst = line.split()
	lst.sort()
	# This is the condition check here wherher duplicate string are present or not!#
	for i in lst :
		if not i in result1:
			result1.append(i) # append here! #
result1.sort()			
print result1
