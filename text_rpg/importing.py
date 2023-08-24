from calc import calc  # this will grab the calc function from the calc file
import math #this comes with python
# from calc import calc as c - this changes the function or class name in THIS file

#Python is a modular langauge
#We can move our functions (and classes) to their own file
#and then, because Python is modular, import them into
#our "main" file
sum = calc("sum",3,2)
print(sum)

