class car():
	def __init__(self):
		self.colour = ''
		self.milage = 0.0
		self.autimatic = ''

cars = [car()]*4
for i in range(0, 4):
	cars[i].colour=input('Enter colour: ')
	cars[i].milage=float(input('Enter milage: '))
	cars[i].autimatic=input('Autimatic? [yes, no]: ')
	print(cars[i].colour, cars[i].milage, cars[i].autimatic, '\n')
