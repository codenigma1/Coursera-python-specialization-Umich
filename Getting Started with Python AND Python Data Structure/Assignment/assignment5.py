largest = None
smallest = None
data = []
while True:
	try:
		num = raw_input("Enter a number: ")
		if num == "done" :
			break
		else:
			data.append(num)
	except:
		print("Invaid input") 
	
largest = max(data)
smallest = min(data)
print "Invaid input"	
print "Maximum", largest
print "Minimum", smallest


#if smallest == largest is None:
    #smallest = val
    #largest = val
#elif val < smallest:
    #smallest = val
    #elif val > largest:
    #largest = val
