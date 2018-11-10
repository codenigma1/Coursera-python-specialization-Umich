hrs = raw_input("Enter Hours: ")
st = float(hrs)
r = raw_input("Enter Rate: ")
sr = float(r)
if (st > 40):
	#st = float(hrs)
	#sr = int(r)
	st -= 40
	tot = (40 * sr) + (st * 15) + 3.75
	#total = float(tot)
	#print "Pay: ", tot
else:
	tot = sr * st
	#print "Pay: ", tot
print "Pay: ", tot

