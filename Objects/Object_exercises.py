
class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def __repr__(self):
        return '%s %s %s' % (self.name, self.email, self.phone)

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1

    def print_contact_info(self):
    	print '%s\'s email: %s, %s\'s phone number: %s' % (self.name, self.email, self.name, self.phone)

    def add_friend(self, other_person):
    	self.friends.append(other_person)

    def num_friends(self):
    	print len(self.friends)


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

jordan.print_contact_info()
print sonny.email,sonny.phone
print jordan.email,jordan.phone


jordan.friends.append(sonny)
sonny.friends.append(jordan)

print jordan.friends[0].name
sonny.num_friends()

print sonny.__repr__()


# MAKE A CLASS

class Vehicle(object):
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def print_info(self):
		print self.year, self.make, self.model

car1 = Vehicle("Chevy", "Tahoe", 2000)

car1.print_info()

