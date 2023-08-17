
# a function is a block of code that can be called on
# demand! When we call it we can pass it variables!
# this is good. :) It gives us a way to reuse code
# and to get different results/output because we 
# can send it variables
# method is a funciton that belongs to a variable (object)

#when we define a function (def) the () are known as
#the siganture. The varaibles inside the siganture
#are known as parameters
#by default, they come in order
this_is_a_global = "Testing a global var out"
print(f"1 global. {this_is_a_global}")
def calc(operation,x,y):
    n = 7 #this is a local variable! It cannot be seen outside of this function
    print(f"You have called Calc. You have sent the {operation} operation.")
    if(operation == "Sum"):
        #if the function gets "sum" passed to it
        #then print off x + y
        print(x + y)
        print(f"x + y = {x + y} and if I add n we get {x + y + n} ")
        print(f"1. inside calc. {this_is_a_global}")
        this_is_a_global = "It's not anymore!"
        print(f"2. inside calc. {this_is_a_global}")
    elif(operation == "Mult"):
        #multiply x * y
        print(x * y)

#when we call/invoke a function, the varaibles in ()
#are called arguements
#by default the args pass into the params in order
#UNLESS, we use the key/name of the param
print("Line 1")
calc("Sum",2,9) #call/invoke the function calc... which we defined above
print("Line 2")
calc("Mult",10,20) #call/invoke the function calc... which we defined above
calc(x = 9, y = 3, operation="Mult")
# calc(9, 3, "Mult")
# print(n) # this will break our function!
print(f"2. global {this_is_a_global}")