# Split() fuction #
list1 = "This is best course of python"
stuff = list1.split()
print "Returen string into the list", stuff
print stuff[2]
for w in stuff :
	print w

# Either Split() fuction uses replace space into list or Arugument into space #

list2 = "python;informatics;book"
stuff1 = list2.split()
print stuff1
print len(stuff1)
stuff2 = list2.split(";") # The argument pass ";" #
print stuff2
print len(stuff2)




