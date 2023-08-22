
# Caesar Cipher Code Challenge
# I will give you a string, and you must print out the Caesar Cipher of that string. The string is defined below, but it is:
# "buqhdydw xem je setu yi byau q cqwys jhysa. edsu oek kdtuhijqdt, yj yi dej jxqj ycfhuiiylu, rkj kdjyb oek te, yj yi cqwys."
# Research Caesar Cipher if you need to! Here is a helpful image that won't tempt you to look at code:
# https://en.wikipedia.org/wiki/Caesar_cipher#/media/File:Caesar_cipher_left_shift_of_3.svg
#Don't cheat or give up early, and don't go too long and get frustrated or discouraged.

encrypted_message = "buqhdydw fojxed yi byau buqhdydw q cqwys jhysa. edsu oek adem xem yj mehai, yj iuuci iycfbu, rkj kdjyb oek te, yj'i cqwys!"
decrypted_alphabet = "abcdefghijklmnopqrstuvwxyz"
decrypted_alphabet_as_list = list(decrypted_alphabet)
encrypted_alphabet1 = "klmnopqrstuvwxyzabcdefghij"
encrypted_alphabet1_as_list = list(encrypted_alphabet1)
encrypted_alphabet2 = "qrstuvwxyzabcdefghijklmnop"
encrypted_alphabet2_as_list = list(encrypted_alphabet2)
decrypted_message = ""

def decrypt_function(encrypted_letter):
	index = encrypted_alphabet2.find(encrypted_letter)
	if(index == -1):
		return encrypted_letter
	else:
		decrypted_letter = decrypted_alphabet[index]
		return decrypted_letter

for letter in encrypted_message:
	correct_letter = decrypt_function(letter)
	decrypted_message += correct_letter

print(decrypted_message)

