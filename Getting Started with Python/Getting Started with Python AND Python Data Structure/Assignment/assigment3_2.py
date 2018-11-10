try:
	hrs = raw_input("Enter Hours: ")
	h = float(hrs)
	r = raw_input("Enter Rate: ")
	r1 = float(r)
except:
	print "Error, please enter numeric input"
	quit()
if (h > 40):
	h -= 40
	tot = (40 * r1) + (h * 15)
else :
	tot = r1 * h
print "Pay :", tot