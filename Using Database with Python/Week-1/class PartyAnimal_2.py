class PartyAnimal(object):
	x = 0
	name = ''

# the constructor 

	def __init__(self, z):
		self.name = z
		print(self.name, 'constructor')

	def party(self):
		self.x = self.x + 1
		print(self.name, "party count", self.x)

x = PartyAnimal("sally")

x.party()


y = PartyAnimal('Jim')
y.party()
y.party()








