astr = "Hello bob"
try:
	istr = int(astr)
except:
	istr = -1
print "Fisrt", istr
astr = "123"
try:
	istr = int(astr)
except:
	istr = -1
print "Second", istr
