
#1. Assign a variable to an integer between 1 and 10
correct_number = 3
#2. Ask the user to guess a number between 1 and 10
guessed_number = input("Please guess a number between 1 and 10 > ")
#3. Cast the number the user gave you into an int
guessed_number_as_int = int(guessed_number)
#3b. Cast the correct number into a string
correct_number_as_string = str(correct_number)
#4. If the user's number equals the correct number,
if(guessed_number_as_int == correct_number):
    #5. if so, print an awesome message to the screen
    print("You are awesome! You guessed it!")
#if checking a data type, you dont compare to a string like "int"
#you use the key word for that data type, such as int, str, float, etc.
elif(type(guessed_number_as_int) == int
        #if using "and" and "or" together... use () !!!!! to group them
        and
    (guessed_number_as_int + 1 == correct_number
        #2 or's ... just 1 needs to be true
        #an and, both need to be true
        or
    guessed_number_as_int - 1 == correct_number)):
    #8. if the number is within 1, print a message that they were close
        #and what the number was    
    print("You were close! The number was " + str(correct_number))
else:
    #6. if not, print a sad message to the screen
    # print("Sorry, that is not the number")
    #7. add to the message what the number was
    #sorry that is not correct. the number was 3
    print("Sorry, that is not the number. The number was " + str(correct_number))


