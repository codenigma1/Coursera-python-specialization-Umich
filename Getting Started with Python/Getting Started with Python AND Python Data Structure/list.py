# List items #
print ["tupples", 34, 34.5]

# Print what you like it in list #
friends = ["Vaibhav", "Naruto", "Batman"]
print "Welcome", friends[1]

# Immutable list #

fruit = "Banana"
# fruit[0] = "b" # string doesn't change data #
# It will give teaceback....#
x = fruit.lower()
print x

# Mutable list #
num = [2,44,3,5,53,5]  # List does change data #
num[3] = 23
print num

# Difference between length and range #
print "Range is: ", range(4)
print "Len is: ", len(friends)
print "Range is: ", range(len(friends))

# concatenation list but it doesn't hurt list #
a = [1,2,3]
b = [4,5,6]
c = a + b
print "comnbined list: ", c
print "doesn't hurt previous list: ", a

# List slice to the string #
# Remember: Just like string, second string up to but not including #
t = [2,3,4,5,6,7,8,3,21,21,313]
print "Remember: Just like string, second string up to but not including: ", t[1:3]
print t[4:9]
print t[3:7]
print t[:]




