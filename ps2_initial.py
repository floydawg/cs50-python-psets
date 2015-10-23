name = raw_input("What is your name: ")

initials = name[0].upper()

for letter in range(0, len(name)):
	if name[letter]  == " ":
		initials += name[letter+1].upper()

print initials
