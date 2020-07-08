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


class FootballFan(PartyAnimal):
	point = 0
	def touchdown(self):
		self.point += 7
		self.party()
		print(self.name, 'points', self.point) 



x = PartyAnimal("sally")
x.party()

y = FootballFan('Jim')
y.party()
y.touchdown()








