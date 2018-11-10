#! python3
x = 'From stephen.marquet@uct.ac.za Sat Jan 5 09:14:16 2008'
y = x.split()
z = y[1]
words = z.split('@')
email = words[1]
print (email)
