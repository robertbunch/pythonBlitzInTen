
# a function is a block of code that can be called on
# demand! When we call it we can pass it variables!
# this is good. :) It gives us a way to reuse code
# and to get different results/output because we 
# can send it variables
# method is a funciton that belongs to a variable (object)

def calc(operation,x,y):
    print(f"You have called Calc. You have sent the {operation} operation.")
    if(operation == "Sum"):
        #if the function gets "sum" passed to it
        #then print off x + y
        print(x + y)
    elif(operation == "Mult"):
        #multiply x * y
        print(x * y)

print("Line 1")
calc("Sum",2,9)
print("Line 2")
calc("Mult",10,20)
