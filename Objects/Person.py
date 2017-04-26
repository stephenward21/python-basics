class Person(object):
	def __init__(self, name, gender, cell):
		self.name = name
		self.gender = gender
		self.species = "Human"
		self.phone = {
			"cell": cell,
			"home": "Who has home phone."
		}

	def greet(self, other_person):
		print "Hello %s, I am %s!" % (other_person, self.name)

	def print_contact_info(self):
		if (self.phone['cell'] != ""):
			print "%s's number is %s" % (self.name, self.phone['cell'])

marissa = Person("Marissa", "female", "77020830803")
print marissa.name,marissa.gender
print marissa.species

merilee = Person("Merilee", "female", "4092809802")
merilee.species = "Robot"

print (merilee.species)
marissa.greet("Rob")



class Vehicle(object):
	def __init__ (self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def print_info(self):
		print self.year, self.model, self.make

	def change_year(self, new_year):
		self.year = new_year

	def get_year(self):
		return self.year

david_cummings_car = Vehicle("McClarren", "Mp4-12c", 2013)
david_cummings_car.print_info()
# david_cummings_car.change_year(2015)  *These two do the same thing*
# david_cummings_car.car.year = 2015
print david_cummings_car.get_year()
print david_cummings_car.year