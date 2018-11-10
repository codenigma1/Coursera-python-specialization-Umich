#in, lower, upper function used!
dick = "vaibhav"
if "z" in dick:
	print "Found it!".upper()
	exit()
print "Not Found".lower()

#Ask which type of data types
stuff = 12.3
print type(stuff)

#find fuction
fruit = "Hello banana"
f = fruit.find("na")
print f
f1 = fruit.find("zz")
print f1

#Replace fuction
f2 = fruit.replace("banana", "Vaibhav")
print f2

# Replace chracter
f3 = fruit.replace("ana", "G!")
print f3

# Stripping White Space left or removing space
dk = " Text Wrangler  "
f4 = dk.lstrip()
print f4

# Stripping White Space of right
f4 = dk.lstrip()
print f4

#Stripping whole space
f5 = dk.strip()
print f5

#Prefix data check start
f6 = fruit.startswith("Hello")
print f6

#
f7 = fruit.startswith("h")
print f7
################This is a example of find and concatenation #############
data = "stephen.marquard@uct.ac.za Sat Jan 5 09: 14: 16 2008"
atpos = data.find("@")
print atpos

bpos = data.find(" ")
print bpos
########print source to destination############ Passing text.
host = data[atpos + 1:bpos]
print host #source   destination
