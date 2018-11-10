#########COUNT THE NUMBER OF LOOP########

count = 0
for i in [1, 2, 4, 5, 6, 3, 78,54,6]:
	count += 1	
	print i, count
print "The count is: ",count

##########SUMMING OF THE LOOP#############
var = 0
for sum in [1, 2, 3, 4, 5, 6, 7]:
	var = var + sum
	print var, sum
print "The sum is: ", var

#########AVERAGE OF THE NUMBER############
tot = 0
count1 = 0
print "Before", tot, count1
for value in [23, 33, 54, 65, 67, 99]:
	count1 += 1
	tot = tot + value 
	print count1, value, tot
print "Average :", tot/count1	

