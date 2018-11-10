#fruit = "banana"
#f = fruit[1]
#print f
#n =3
#w = fruit[n-1]
#print w
#print len(fruit)
fruit = "banana"
index = 0
for value in fruit:
	print value,index
	index = index + 1
print "Done!"

fruit = "banana"
count = 0
while count <  len(fruit):
	letter = fruit[count]
	print count, letter
	count = count + 1
print "Done!"

for letter in fruit :
	if letter == "a":
		count = count + 1
		print count
print "Hello"
