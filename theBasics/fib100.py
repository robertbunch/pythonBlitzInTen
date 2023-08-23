#Usually we access a list element with list_name[i]
#You can access any element in a list anytime no matter what i is
#For instance list_name[i+1] or list_name[i*3]...

list_of_fib = [0,1]

#i should be the sequence number you are calculating
def append_and_print_fib(i):
    new_number = list_of_fib[i-1] + list_of_fib[i-2]
    list_of_fib.append(new_number)

#loop here
for i in range(2,100):
    #call the function and send the sequence number to calculate
    append_and_print_fib(i)

print(list_of_fib[99])