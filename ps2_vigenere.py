# program that takes a cipher that is a string
# and then encodes a user-entered message using that
# ciper
import sys
if len(sys.argv) != 2:
	print "Please enter only one cipher on the command line."
else:
	cipher = str(sys.argv[1]).lower()
	for i in cipher:
		if not i.isalpha():
			print "Please enter a cipher using only letters"
			sys.exit()

	string = raw_input("Enter a string to be converted: ")
	encoded_string = ""
	j = 0
	for letter in string:
		if letter.isalpha():
			if letter.isupper():
				shift = 65
			else:
				shift = 97
			int_letter = ord(letter) - shift
			cipher_shift = ord(cipher[j]) - 97
			int_letter = (int_letter + cipher_shift) % 26
			new_letter = chr(int_letter + shift)
			encoded_string += new_letter
			j += 1
			if j >= len(cipher):
				j = 0
		else:
			encoded_string += letter

	print encoded_string


