#! python3

import re
count = 0
numlist = list()
hand = open('actual-data.txt')
for line in hand :
	line = line.strip()
	values = re.findall('[0-9]+', line)
#######	One of most crucial line to understand this #####################
	if not values:
		continue
	else:
		for value in values:
			num = int(value)
			# count = count + 1
			numlist.append(num)
print ('The sum is:', sum(numlist))
##########################################################################
	# if len(value) != 1: continue
	# num = int(value[0])
	# print (num)
# 	numlist.append(num)
# print (sum(numlist))
	# count = count + 1
	# tot = tot + num
	# print (tot, count)

							 






