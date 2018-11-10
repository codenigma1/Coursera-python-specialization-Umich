inp = raw_input("Enter the file name: ")
fhand = open(inp)
count = 0
dic = dict()
for line in fhand :
	if line.startswith("From "):
		lst = line.split()
		hour = lst[5].split(":")
		sec = hour[0]

		dic[sec] = dic.get(sec, 0) + 1
for final,val in sorted(dic.items()) :
	print final, val

# bighour = None
# bigcount = None
# for h1, c1 in dic.items() :
# 	if c1 > bigcount :
# 		bighour = h1
# 		bigcount = c1
# 		print bighour, bigcount		
