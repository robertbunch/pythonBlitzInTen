
#numbers are floats or integers
print(int(3.14))

#Floats have an is_integer()
#will tell you if the float has anything other than .0000...
the_number_pi = 3.14
print(type(the_number_pi))
print(the_number_pi.is_integer())

#abs = absolute value = removes the - from any number
print(abs(-100)) #100
print(abs(100)) #100

#guess_the_number game, we checked both -1 from the number
#and +1 from the number. We could use abs and write 
#that conditional in 1 line

# pow = power, and it takes 2 numbers, 
#first is the number to raise by a power
#second is the power to raise by
print(pow(2,5)) # 2 * 2 * 2 * 2 * 2 = 32
print(pow(5,2)) # 5 * 5 = 25
print(pow(5.2,2.2)) 

#round = round the number to x places
#first = the number to round
#second = the number of decimals to round to
#if we dont give it the number of places, it rounds to int
print(round(2.23423455235423))
print(round(2.2342355235423,5))

