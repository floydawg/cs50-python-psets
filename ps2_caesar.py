import sys
if len(sys.argv) != 2:
	print "Please enter only one cipher on the command line."
else:
	cipher = int(sys.argv[1]) 
	string = raw_input("Enter a string to be converted: ")
	encoded_string = ""
	for letter in string:
		if letter.isalpha():
			if letter.isupper():
				shift = 65
			else:
				shift = 97
			int_letter = ord(letter) - shift
			int_letter = (int_letter + cipher) % 26
			new_letter = chr(int_letter + shift)
			encoded_string += new_letter
		else:
			encoded_string += letter

	print encoded_string


