# answer: 23514624000
import time
start_time = time.time() #get our starting time

num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
num_as_string = str(num)
num_as_list = list(str(num_as_string))

highest_product = 0
low_index = 0
high_index = 13
while(high_index < 1001):
    this_product = 1
    spliced_segment = (num_as_string[low_index:high_index])
    if('0' not in spliced_segment):
        for i in spliced_segment:
            if(i == 0):
                break
            this_product *= int(i)
            # print(low_index,high_index,this_product)
        if(this_product > highest_product):
            highest_product = this_product
        if(low_index == 23):
            print(f"Upper 23: {this_product}")
    low_index += 1
    high_index += 1
print(highest_product)

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve as substring {time.time() - start_time}")



start_time = time.time() #get our starting time
num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
num_as_string = str(num)

highest_product = 1
init_spliced_segment = (num_as_string[0:13])
for num in init_spliced_segment:
    highest_product *= int(num)

low_index = 1
high_index = 13 #not 14, because this isn't a range, its an index
last_product = highest_product

while(high_index < 1000):
    new_number = int(num_as_string[high_index])
    previous_first_number = int(num_as_string[low_index-1])
    # print(previous_first_number,new_number)
    if(last_product == 0): #will include previous_first_number as 0
        new_int = num_as_string[low_index:high_index+1]
        this_product = 1
        for i in new_int:
            this_product *= int(i)
    elif(new_number == 0):
        this_product = 0
    else:
        this_product = int(last_product / previous_first_number) * new_number
        if(low_index == 23):
            print(f"Lower 23: {this_product} - {num_as_string[low_index:high_index]}")
    if(this_product > highest_product):
        highest_product = this_product            
    low_index += 1
    high_index += 1
    last_product = this_product
print(highest_product)

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve as swap old with new {time.time() - start_time}")


