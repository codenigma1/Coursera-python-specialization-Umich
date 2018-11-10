# Built in Function and Lists #
List = [2,4,35,5,4,64,6,67,5,553]
print "Return the maximum value: ", max(List)
print "Return the lenght in the list: ", len(List)
print "Return the minimum value: ", min(List)
print "Return the sum value: ", sum(List)
print "Return the average value: ", sum(List)/len(List)

# Sample program find the maximum no. with function #

numlist = list()
while True:
	inp = raw_input("Enter the no.: ")
	if inp == "done":
		break
	inp1 = float(inp)	
	numlist.append(inp1) # look carefully what's going on #
avg = sum(numlist)/len(numlist)
print "The Average is: ", avg

# Split() fuction #
list1 = "This is best course of python"
stuff = list1.split()
print "Returen string into the list", stuff
print stuff[2]
for w in stuff :
	print w
	
