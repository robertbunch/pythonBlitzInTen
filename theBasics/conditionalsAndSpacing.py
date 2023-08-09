
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
if(name == "Rob"):
	print("Hello, instructor")
if(name == "Akash"):
	print("Hello, assistant!")
else:
	print("Hello, there")