# sample program #
c = {"red": 54, "blue": 34, "green": 66}
temp = list() # create empty list #
tup = c.items() # converted into tuples #
for k,v in tup :
	temp.append((v, k)) # then append into list"temp" variable #
print temp
temp.sort(reverse = True)  # yield highest value #
print temp