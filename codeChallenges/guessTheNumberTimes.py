correct_number = 3
# The loop needs to start here
# Allow the user to keep guessing until guess the right answer
number_of_tries = input("How many guesses would you like? > ")
number_of_tries = int(number_of_tries)
# i is just a variable name! 
# we could call it "guess_num"
# start i at 1, and stop (dont include) number_of_tries +1
for i in range(1,number_of_tries+1):
    print(f"You are currently on guess {i}.")
    guessed_number = input("Please guess a number between 1 and 10 > ")
    guessed_number_as_int = int(guessed_number)
    correct_number_as_string = str(correct_number)
    if(guessed_number_as_int == correct_number):
        print("You are awesome! You guessed it!")
        # Inside of a for loop, if you want to break out early
        # use ... the break command
        break
    elif(guessed_number_as_int + 1 == correct_number):
        print("You were close!")
    elif(guessed_number_as_int - 1 == correct_number):
        print("You were close!")
    else:
        print("You are not even close!")
print(f"It took you {i}")