# print "Hello World!"
# print ("Hello, World", "Again")
# print """This
# will ignore the new lines
# until it sees another three quotes"""

# Variables - string, number, letters, any other stuff you can make with a keyboard
# and you want to stash something that's not fast, into something that is fast
# There is no declaration in Python.
# In JS...var name = "Shane";
name = "Robert Bunch"
# Python is not heavily typed (for instance C#)
name = "Robert " + "Bunch"
first_name = "Robert";
last_name = "Bunch";
full_name = first_name + " " + last_name
# print full_name

# Arithmatic

the_meaning_of_life = 40 + 2
# print the_meaning_of_life
# print the_meaning_of_life / 2
# print the_meaning_of_life % 5
# 

# print 4 + "Joe"

# print 4 * "Joe"

# Data types (variable types)
# 	Strings - English type stuff for people (in yellow)
# 	Numbers - something with digits and stuff that goes with digits (. -)
# 		Floats, Integers
# 	Booleans - True or False, 1 or 0, Yes or No, On or Off
# 	lists - list of variables in one variable
# 	dictionary - variables of variables
# 	objects - Deal with it later

# Strings
# first_name = "Rob"
# last_name = "Bunch"
# # Format method
# print "Hello {} {}".format(first_name, last_name)
# # print "Hello " + first_name + " " + last_name
# # Placeholders
# print "Hello, %s %s" % (first_name, last_name)
# print "Hello, %s %s for the %drd time!" % (first_name, last_name, 3)

# Floats
# pi_the_magic_float = 3.14
# print type(pi_the_magic_float)
# make_me_an_integer = int(pi_the_magic_float)
# print make_me_an_integer
# print .2  + .1

# Booleans - true or false (Uppercase)
# the_truth = True
# print type(the_truth)
# the_lie = False
# print type(the_lie)

# Raw Input
first_name = raw_input("First name: ")
print first_name
last_name = raw_input("Last name: ")

# Conditionals
# 1 = means you want to assign whatever on the left to whatever on the right
# 2 = means you want to compare whats on the left with what's on the right

if(first_name == last_name):
	print "Your first name is the same as your last name?"

# if you want to compare = or greater than, >=
age = raw_input("How old are you?")
age_as_int = int(age)
# print type(age)
if(age >= 21):
	print "You can buy beer."


