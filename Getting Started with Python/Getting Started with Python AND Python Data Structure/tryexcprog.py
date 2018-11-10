name = raw_input("Enter Number: ")
try:
	var = int(name)
except:
	var = -1
if(var > 0):
	print "Hello", var
else:
	print "Please enter the number"