score = raw_input("Enter Score: ")
s = float(score)
if(0 <= s <= 1.0):
	if(s >= 0.9):
		print "A"
	elif(s >= 0.8):
		print "B"
	elif(s >= 0.7):
		print "C"m
	elif(s >= 0.6):
		print "D"
	#elif(s < 0.6):
		#print "F"
	else:
		s < 0.6
		print "f"
else:
	print "an error"
