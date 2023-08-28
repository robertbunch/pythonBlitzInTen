
# #id will give us a unique integer to represent that variable
# x = 3
# y = x #we are pointing y at x, UNTIL the value of one changes
# print(id(x)) #same value as line below, because 3 is immutable
# print(id(y)) #same value as line above, because 3 is immutable
# x += 1 #will make x 4
# print(id(x))  #values have diverged. 3 is unchangable so, it must make a new value in memory
# print(id(y)) #same as above. It has not changed
# x -= 1 #x is back to 3
# print(id(x)) #uses teh original 3, because...3 is imutable. Doesn't matter, if x and y are related
# z = 3
# print(id(x))
# print(id(y))
# print(id(z)) #Woah. Even though x and z are never associated, Python is smart. It uses the same memory to reference an unchangable integer

x = []
print(id(x)) #x hasn't changed, its value has
x.append(1)
print(id(x))
y = x 
print(id(y))
x.append(2) #x is adding a number
y.append("Hello") #y is adding a number
#lists are mutable!!! Python will not change the id (place in memory)
#it will change the thing in memory and x and y are changing
#the same thing
print(id(x))
print(id(y))

