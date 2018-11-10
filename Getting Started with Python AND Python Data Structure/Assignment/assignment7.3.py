file = raw_input("Enter a file name: ")
try :
	handle = open(file)
except :
	print "please correct name because file doesn't exist"
	exit()	
file1 = handle.read().upper()  # we can use two function at time
# file2 = file1.upper()
print file1
	

