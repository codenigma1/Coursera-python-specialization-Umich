while True:
	line = raw_input("Enter the string ")
	if line[0] == "#":
		continue #This goes back onto the top of the loop.
	if line == "done":
		break #This statment jump into out of current loop of body!
	print "Try another one"	
print "U Gone"	
