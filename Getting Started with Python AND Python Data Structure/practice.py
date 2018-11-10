# d = {'a': 10, 'b': 12, 'c': 13}
# t = list()
# for k, v in d.items():
# 	t.append((v,k))
# 	t.sort(reverse = True)
# print t 		

fhand = raw_input('Enter the file name: ')
file = open(fhand)
d = dict()
for line in file:
	words = line.split()
	for word in words:
		d[word] = d.get(word, 0) + 1

lst = list()
for k,v in d.items():
	lst.append((v,k))
lst.sort(reverse = True)
for v, k in lst[:10]:
	print k, v			

