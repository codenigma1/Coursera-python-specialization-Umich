# Tuples simple program #
(x, y) = ("Vaibhav", 39)
print  y

# Tuples are also comparable #
a = (9, 2, 5) # It is look only first value of the tuples while comparing #
b = (10, 3, 4)
c = a > b
print c
# Tuple match only first value whether is greater or not #
v = ("vaibhav", "Sachin", "Drag")
k = ("fun", "fuck", "did")
f = v > k
print f

# Sorting Lists of tuples #
d = {"ema": 3, "fun": 4, "shit": 34}
t = d.items()
print t
# t.sort() # Simply sorting a list without variabe #
r = sorted(t)       # Sorted() fuction, it is new fuction for sorting tuples we can assign variable sorted(t) them #
print r

# we can also sort by forloop#
for k,v in sorted(t) :
	print k, v