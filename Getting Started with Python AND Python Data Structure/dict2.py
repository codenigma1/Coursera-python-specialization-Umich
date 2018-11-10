# This program counting the no. of repeating word #
counts = dict()
line = raw_input("Enter the line of text: ")
words = line.split()
print "List is: ", words
print "counting :"
for word in words : 
	counts[word] = counts.get(word, 0) + 1 # This line is very useful try to understand get() function#

print "Counts :", counts

# using forloop we can print #
count1 = {"frd" : 1, "sat" : 32, "sun" : 34} # This is way we can define dictionarie #
for key in count1 :
	print key, count1[key]	
