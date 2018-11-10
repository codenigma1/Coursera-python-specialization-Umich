########The find the largest no############
the_largest_so_far = -1
print "Before",the_largest_so_far
for i in [3, 4, 5, 1, 45, 32, 90]:
	if i > the_largest_so_far:
		the_largest_so_far = i
	print "I : ", i, "the largest: ", the_largest_so_far
print "Final max value is: ", the_largest_so_far
#####it might be worked in some cases. however, isn't always!
smallest_so_far = 100
print"Before", smallest_so_far
for value in [99, 55, 65, 1, 2]:
	if value < smallest_so_far:
		smallest_so_far = value
	print value, smallest_so_far
print "The smallest No. is : ", smallest_so_far	
########Best new Method###########
smallest = None
print "Before the value: ", smallest
for val in [99, 55, 65, 1, 2, 0]:
	if smallest is None: ####Don't use always "is" instruction
		smallest = val
	elif val < smallest:
		smallest = val
	print smallest, val
print "The New method of smallest no. is: ", smallest	

