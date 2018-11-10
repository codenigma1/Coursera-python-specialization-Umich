#####Filtering Loop or Searching##########

print "Before"
for value in [23, 45, 42, 45, 545, 6, 677]:
	if value > 40 :
		print "Large number is: ", value
	print "After going to top"
print "Done"		


#########Boolean############
found = "false"
print "Before: ", found
for i in [23, 43, 45, 54, 33, 33, 99]:
	if i == 33:
		print "true", i
		#break
	else:	
		print found, i
print "Done"	