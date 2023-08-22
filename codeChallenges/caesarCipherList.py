#===============As list with with loop=============
message = "buqhdydw fojxed yi byau buqhdydw q cqwys jhysa. edsu oek adem xem yj mehai, yj iuuci iycfbu, rkj kdjyb oek te, yj'i cqwys!"
decrypted_alphabet = "abcdefghijklmnopqrstuvwxyz"
decrypted_alphabet_as_list = list(decrypted_alphabet)
encrypted_alphabet1 = "klmnopqrstuvwxyzabcdefghij"
encrypted_alphabet1_as_list = list(encrypted_alphabet1)
encrypted_alphabet2 = "qrstuvwxyzabcdefghijklmnop"
encrypted_alphabet2_as_list = list(encrypted_alphabet2)
decrypted_message = ""

def decrypt_function(encrypted_letter):
	for i in range(0,len(encrypted_alphabet2_as_list)):
		if(encrypted_alphabet2_as_list[i] == encrypted_letter):
			# i is the index we are after!
			return decrypted_alphabet[i]
	return encrypted_letter

for letter in message:
	correct_letter = decrypt_function(letter)
	decrypted_message += correct_letter

print(decrypted_message)

#===============As list with index=============
encrypted_message = "buqhdydw fojxed yi byau buqhdydw q cqwys jhysa. edsu oek adem xem yj mehai, yj iuuci iycfbu, rkj kdjyb oek te, yj'i cqwys!"
decrypted_alphabet = "abcdefghijklmnopqrstuvwxyz"
decrypted_alphabet_as_list = list(decrypted_alphabet)
encrypted_alphabet1 = "klmnopqrstuvwxyzabcdefghij"
encrypted_alphabet1_as_list = list(encrypted_alphabet1)
encrypted_alphabet2 = "qrstuvwxyzabcdefghijklmnop"
encrypted_alphabet2_as_list = list(encrypted_alphabet2)
decrypted_message = ""

def decrypt_function(encrypted_letter):
	if(encrypted_letter == " " or encrypted_letter == "." or encrypted_letter == "," or encrypted_letter == "'" or encrypted_letter == "!" ):
		return encrypted_letter
	else:
		index = encrypted_alphabet2_as_list.index(encrypted_letter)
		decrypted_letter = decrypted_alphabet[index]
		return decrypted_letter

for letter in encrypted_message:
	correct_letter = decrypt_function(letter)
	decrypted_message += correct_letter

print(decrypted_message)


