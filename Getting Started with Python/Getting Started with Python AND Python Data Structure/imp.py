sum = 0
count = 0
while True:
	inp = raw_input("Enter the number: ")
#This is all condition for makeing program	
	if inp == 'done': break #This is important function
	if len(inp) < 1 : break # This is important funtion
	try :
		num = float(inp)
	except :
		print 'Invalid input'
		continue
##############################################			
	count = count + 1
	sum = sum + num
	avg = sum/count
	print num, count, sum

print 'Average is', avg