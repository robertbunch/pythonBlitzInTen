
#This file does nothing but house the calc function
#this is good. If we need anything related to calc
#we know exactly where to look.
def calc(op,x,y):
    if(op == "sum"):
        return x + y
    elif(op == "mult"):
        return x * y