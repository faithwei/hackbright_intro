# full_name = ("faith", "ng")

# full_name_convert = list(full_name)
# print full_name_convert

# full_name_convert.sort(reverse=True)
# print full_name_convert

# full_name_reverse = sorted(full_name_convert, reverse=True)
# print full_name_reverse

# number = 1000
# while number >= 100:
# 	print number
# 	number = number - 100

import string 

# print string.printable

encrypt_dict = {}
decrypt_dict = {}

def create_dictionaries():
	global encrypt_dict
	global decrypt_dict

	idx = 0

	for char in string.printable:
		encrypt_dict[char] = idx
		decrypt_dict[idx] = char
		idx = idx+1

	print encrypt_dict
	print decrypt_dict

def encrypt(message):
	# message = raw_input("Enter a message: ")
	encrypted_message = ""
	
	for character in message:
		code = str(encrypt_dict[character])
		encrypted_message += code

	return encrypted_message


create_dictionaries()

print encrypt("main event is here!")