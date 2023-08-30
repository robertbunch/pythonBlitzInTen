# This challenge comes from the website https://projecteuler.net/problem=4.
# You'll have no trouble finding help online with these if you need it ;)

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def amIAPalindrome(numberToCheck):
	# Step one is to check if the number is a palidrome 
    # reverse would be handy here, so convert the str to a list
    # First convert to a string and then to a list... 
    # in one fell swoop!
	numAsList = list(str(numberToCheck))
	numAsList.reverse()
	# convert back to a number
	numReversed = int(''.join(numAsList))

    #wow, that was a nusience. But we reversed a number by going 
    #number --> str --> list -- .reverse() --> strin --> int
	#are they identical? If so then numberToCheck is a palindrome.
	if(numberToCheck == numReversed):
		#Palindrome found. Return true
		return True
	else:
		return False

#init our result
highestKnownPalidrome = 0

# We are looking for the largest product of 2, 3 digit numbers
# Start with the 2 smallest 3 digit numbers and go up from there
for i in range(100,1000):
	# Same, start at 100 and count up to 999
	for j in range(100,1000):
		#stash product of i and j
		currentProduct = i * j
						
		#see if our stashed var is a palidrome 
		if ( amIAPalindrome(currentProduct)):
			# console.log(currentProduct)
			#Check if it's larger than highestKnownPalidrome and, if so, store it 
			if ( currentProduct > highestKnownPalidrome ):
				highestKnownPalidrome = currentProduct
				print(highestKnownPalidrome)

# print(highestKnownPalidrome)