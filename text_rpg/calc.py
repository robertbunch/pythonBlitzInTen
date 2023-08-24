
#This file does nothing but house the calc function
#this is good. If we need anything related to calc
#we know exactly where to look.
def calc(op,x,y):
    if(op == "sum"):
        return x + y
    elif(op == "mult"):
        return x * y
    
#Python also comes with it's owns modules
#That means, it has a "core" which is the stuff
#that automatically comes with the python command
    #variables
    #lists
    #print/loops
print(math.pi)

#python has a 3rd party module "package manager" 
#called pip
    #pandas - is not part of core. It has to be installed
    #pygame - is not part of core. It has to be installed

