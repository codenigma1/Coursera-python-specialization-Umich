class PartyAnimal(object):
	x = 0

# the constructor 

	def __init__(self):
		print('I am constructor')

	def party(self):
		self.x = self.x + 1
		print('So far', self.x)

# the destructor

	def destructor(self):
		del self.x
		print('I am destructor', self.x)

	# def __del__(self):
	# 	print ('I am the destructor', self.x)


x = PartyAnimal()

x.party()
x.party()
x.party()
x.party()
x = 42
print(x)




truth = "beauty"
index = 0
letters = []
while index < len(truth):
    letters.append(truth[index])
    index += 2

letters = '-'.join(letters)
print(letters)





