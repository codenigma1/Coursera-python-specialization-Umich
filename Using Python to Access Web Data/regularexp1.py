#! python3

import re   ########## It is at the begining if you want to use regualar expression  ######
hand = open('mbox-long.txt')
for line in hand:
	line = line.strip()
	if re.search('^From\S+:', line):#######"^""--->for the begining, \S-----> white space, "+ or *"---> one or more times to print
		print (line)


