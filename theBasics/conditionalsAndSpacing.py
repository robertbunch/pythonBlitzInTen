
name = input("Please enter your name > ")
# print(name)

# what if we want to say something differnet based
# on who the person is?
if(name == "Rob"): #an if statement takes () and in the () we put Left thing == Right thing
	print("Hello, instructor " + name)
	#python is an indented language!
else:
	print("Hello, Student")
print("Out of conditionals statement")

# mon nom est - My name is - Huh? Uh, I guess so...
# je m'appelle - I call myself - Ya. That's good. Well done.

#elif means it is part of the conditional statement
#it falls down like a waterfall, and the first one
#that is true, is the ONLY one that will be run
#in other words, an elif means "which one of these is true"
if(name == "Rob"):
	print("Hello, instructor")
elif(name == "Akash"):
	print("Hello, assistant!")
else:
	print("Hello, there")

#more than 1 if, means they are evaluated separately
# if(name == "Rob"):
# 	print("Hello, instructor")
# if(name == "Akash"):
# 	print("Hello, assistant!")
# else:
# 	print("Hello, there")

x = 3
if(x == 3 or x == 5):
	print("You're number is 3 or 5")
else:
	print("You're number is NOT 3 or 5")

if(x == 3 and name == "Rob"):
	print("You have a common name and a common number")
else:
	print("Not Rob and 3")
