import time
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product 
# of two 3-digit numbers. 

#a function that checks if a number is a palindrome
def is_number_a_palindrome(numberToCheck):
  
    numAsList = list(str(numberToCheck)) # here it is in one line! (you can do it in 2 of course)
    numAsList.reverse() #number made into a list, and reversed
    numReversed = int(''.join(numAsList)) # convert back to a number

    #wow, that was a nusience. But we reversed a number by going 
    #number --> str --> list -- .reverse() --> string --> int
    #are they identical? If so then numberToCheck is a palindrome.
    if(numberToCheck == numReversed):
        #Palindrome! Return true
        return True
    else:
        return False

#init our result
highestKnownPalidrome = 0


start_time = time.time()

# We are looking for the largest product of 2, 3 digit numbers
# Start with the 2 smallest 3 digit numbers and go up from there
# We will run 2 loops, each 900 times. For each time through the
# outer loop, the inner loop will go from 100 to 999
# So the outer loop start at 100, and the inner will go for 900 times,
# then it will go to 101, and the inner loop will go another 900 times
# Total is 900 * 900 = 810,000 operations. Python will smile at that.
for i in range(100,1000): #outer loop
    # start at 100 and count up to 999
    for j in range(i,1000): #inner loop
        currentProduct = i * j #product of i and j
                        
        #see if the currentProduct is a palidrome 
        is_this_a_pal = is_number_a_palindrome(currentProduct)
        if (is_this_a_pal):
            #Check if it's larger than highestKnownPalidrome and, if so, store it 
            if ( currentProduct > highestKnownPalidrome ):
                highestKnownPalidrome = currentProduct
                # print(highestKnownPalidrome) #here for testing

print(highestKnownPalidrome)

end_time = time.time()
print(f"--- number of secodns to solve... {end_time - start_time}" )