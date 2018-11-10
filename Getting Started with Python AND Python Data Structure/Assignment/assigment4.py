def computepay(h, r1):
	print "Funtion stat!"
	if (h > 40):
		h -= 40
		tot = (40 * r1) + (h * 15)
	else :
		tot = r1 * h
	print "Pay :", tot
	return tot

try:
	hrs = raw_input("Enter Hours: ")
	h = float(hrs)
	r = raw_input("Enter Rate: ")
	r1 = float(r)
except:
	print "Error, please enter numeric input"
	quit()

print "After enter the code", h, r1
p = computepay(h, r1)
print "We are back to the total", p

