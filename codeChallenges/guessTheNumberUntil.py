correct_number = 3
# The loop needs to start here
# Allow the user to keep guessing until guess the right answer
keep_guessing = True
while(keep_guessing):
    guessed_number = input("Please guess a number between 1 and 10 > ")
    guessed_number_as_int = int(guessed_number)
    correct_number_as_string = str(correct_number)
    if(guessed_number_as_int == correct_number):
        print("You are awesome! You guessed it!")
        # When the user guesses the right answer, the loop can stop!
        # To stop the loop, change the bool in the while
        # to be false
        keep_guessing = False
    elif(guessed_number_as_int + 1 == correct_number):
        print("You were close!")
    elif(guessed_number_as_int - 1 == correct_number):
        print("You were close!")
    else:
        print("You are not even close!")
