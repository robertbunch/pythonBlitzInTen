#Sorting an unsorted list is a classic computer science problem
#Bubble sort, the one we are doing here, is the entry level sort
#I will give you a list of random numbers. You should write a function
#that implaments bubble sort to put them in the correct order.
#Bubble sort loops through the list, looking at each number in the list
#The first time through, it compares 1 and 2. If 1 is bigger, they swap places
#Otherwise they stay in their place.
#Then it compares 2 and 3... same thing, swap if 1 is bigger, otherwise leave alone
#Go to the end of the list, then start over
#It is called bubble sort because the large numbers "bubble up" to the top

def bubbleSort(random_list):
    #get length of the list so we can loop through
    list_length = len(random_list)
    swapped = False
    #no reason to check the last number
    for i in range(0,list_length-1):
        #we don't need to loop through all numbers...
        #because each time through, we know the number 
        #just moved to the end is largest  
        for j in range(0, list_length-i-1): 
            if random_list[j] > random_list[j + 1]:
                swapped = True
                #stash random_list[j] because we need to overwrite it
                temp = random_list[j]
                random_list[j] = random_list[j + 1]
                random_list[j + 1] = temp
         
        #if we get through the whole list without a swap, the
        #list is already in order so stop
        if(swapped == False):
            # break #break isn't enough because it will only stop
            #the current loop. We need to end the sort
            return
 
 
#Seed data
list_of_random_numbers = [14,91,201,5,2,34,55]
 
bubbleSort(list_of_random_numbers)
 
print(f"Sorted list is: {''.join(str(list_of_random_numbers))}")