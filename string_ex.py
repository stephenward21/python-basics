#Uppercase and Capitalize
stringer = "the string exercises"
print (stringer.upper())
print (stringer.title())

stringer = "the string exercises"
up_string = ""
for stringer in stringer:
	up_string += stringer.upper()
print up_string

#Reverse
reverse_list = stringer.split(" ")
print reverse_list [::-1]

# Leetspeak
p_graph = ("There was an old lady who lived in a shoe.").upper()
result = ""
for letter in p_graph:
	if (letter == "A"):
		result =  result + "4"
	if (letter == "E"):
		result =  result + "3"
	if (letter == "G"):
		result =  result + "6"
	if (letter == "I"):
		result =  result + "1"
	if (letter == "O"):
		result =   result + "0"
	if (letter == "S"):
		result =  result + "5"
	if (letter == "T"):
		result =  result + "7"
	else:
		result = result + letter

print result



# Long Vowels
vowels = ["a", "e", "i", "o", "u"]
long_vow_word = "Good"
count = 0

for letter in long_vow_word:
	if letter in vowels:
		count += 1
		if count > 1:
			long_list = list(long_vow_word)
			vowel_index = long_list.index(letter)
			long_list.remove(letter)
			long_list.insert(vowel_index, letter*4)
			new_vow_word = "".join(long_list)

print (new_vow_word)


	




