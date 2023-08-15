
# a loop is a way to run the same code over and over
# and stop when x happens, or when we have done it x times

#while loop goes until x is not true
# counter = 0
# while(counter < 10):
#     # print(counter)
#     counter = counter + 1
# print("Loop has ended!")

# #for loop
# # i = the dish you are on
# # range(0,10) = the 10 dirty dishes in the sink
# for i in range(0,10):
#     if(i == 5):
#         print("Five")
#     else:    
#         print(i)

############For loops with lists#############
# a for loop takes after the "in" an iterable
# iterable = something that has members in the same
# order/sequence that can be iteraed over one at a time

# for letter in "something":
#     print(letter)

cars = [
    "BMW",
    "Ford",
    "Toyota",
]

#database, api, group
for car in cars:
    if(car == "BMW"):
        print("You have a BMW")
    else:
        print(f"I hope you like your car! {car} is a great brand.")