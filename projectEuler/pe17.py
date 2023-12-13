import time
start_time = time.time() #get our starting time
# Answer: 21124

# 1-9... we use these A LOT
digits = [
    "one","two","three","four","five",
    "six","seven","eight","nine"
]
# 10-19 which we only use once per 100
unique_numbers = ["ten","eleven","twelve","thirteen",
                "fourteen","fifteen","sixteen","seventeen",
                "eighteen","nineteen"]

# multiples of ten, used once every 100
tens = ["twenty","thirty","forty","fifty","sixty",
        "seventy","eighty","ninety"]

number_list = digits + unique_numbers


for t in tens:
    number_list.append(t)
    for d in digits:
        # grab the digit and stick it on the end of ten
        number_list.append(t+d)

# our 100s - we use digit + "hundred"
for h in digits:
    this_hundred = h+"hundred"
    number_list.append(this_hundred) #"onhundred" or "twohundred"
    # grab the first 99 numbers and put this_hundred on the front
    for num in range(0,99):
        this_num = this_hundred + "and" + number_list[num]
        number_list.append(this_num)
# add onethousand
number_list.append("onethousand")

# for num in number_list:
#     print(num)

count = 0
for word in number_list:
    count += len(word)

print(count)

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")
