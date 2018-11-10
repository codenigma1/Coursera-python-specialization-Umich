# Sample program of sorting the tuples which one is more repeatative #

fhand = raw_input("Enter the file name: ")
fle = open(fhand)
counts = dict()
for line in fle :
	word = line.split()
	for k in word :
		counts[k] = counts.get(k, 0) + 1
print counts
lst = list()
for k, v in counts.items() :
	lst.append((v, k))
lst.sort(reverse = True)	
for v, k in lst[:10]:
	print k, v

# This is a very short program as above  you can see #
# It's shorter version of above #
c = {"ff": 3, "dd": 34, "we": 65}
print sorted([ (v, k) for k, v in c.items()]) # We can prarmeter in this sorted() function although we cannot in sort()#





