#! python3

# Also we can find('@') method little bit complex than double split.
# find out too specific information just like double split('@') or split method we used earlier.
############### Symbol informations of Reguar Expressions ######################################
# "^"---> Begining of line, "\"----> Special prefix chracter and it is represent next character, \S-----> white space, \$---> same as said earlier it is represent dollar sign, "."---> It help to display everything, " + or * "---> one or more character print, ([^ ]+)---> non-blanck space, ('^F.+:', a) and ('^F.+?:', a)----> greedy and not, ([0-9.]+)-----> it is represented all kind of number such as 10.00, 12.54, 323.44........etc.


import re   ########## It is at the begining if you want to use regualar expression  ######
x = 'This is my computer 34 no one can messs with her 21 without me 90'
y = re.findall('[0-9]+', x)   #findall()---> function is used for find the specific string and returns list
print (y)
				#######"^""--->for the begining, \S-----> white space, " + or * "---> one or more character print ####

####### Greedy Matching Technique and Non-Greedy Matching Technique ############

a = 'From: Using the computer : chracter'
b = re.findall('^F.+:', a) # It print chracter as much as long ---> greedy funtion
c = re.findall('^F.+?:', a) # It is not greedy funtion
print (b, c)

z = 'From stephen.marquet@uct.ac.za Sat Jan 5 09:14:16 2008'
s = re.findall('^From (\S+@\S+)', z)
t = re.findall('^From .*@([^ ]+)', z)
print (s, t)							 






