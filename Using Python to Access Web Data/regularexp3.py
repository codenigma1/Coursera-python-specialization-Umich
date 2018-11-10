#! python3

import re
hand = input("Enter the file name: ")
fhand = open(hand)
numlist = list()
for line in fhand:
	line = line.strip()
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	# print (stuff)
	print (len(stuff), stuff)
	if len(stuff) != 1 : continue
	# print (stuff)
	value = float(stuff[0])
	# print (value)
	numlist.append(value)
print ('The Maximum: ', (numlist))	


########################## THIS IS PROGRAM FOLLOWING PROGRAM WITHOUT REGUALR EXPRESSION #######################3

# hand = input ("Enter the file name: ")
# fhand = open(hand)
# numlist = list()
# for line in fhand:
# 	line = line.strip()
# 	if line.startswith('X-DSPAM-Confidence:'):
# 		stuff = line.split()
# 		x = line.split()
# 		val = x[1]
# 		numlist.append(val)
# print ('The maximum value: ', max(numlist))







