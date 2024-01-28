import time
start_time = time.time() #get our starting time

def bucket_sorter(list,char_position):
    # make our 26 + 1 buckets
    buckets = [[] for i in range(27)]
    print(buckets)
    # go through each word and grab the letter at char_position
    # and put it in the right bucket
    for word in list:
        if(word[char_position] == ' '):
            # this is a blank. It goes in bucket 26
            buckets[26].append(word)
        else:
            bucket_index = ord(word[char_position]) - ord('a')
            # print(bucket_index)
            buckets[bucket_index].append(word)
    # print(buckets)
    # step 2 is concat our buckets into 1 list
    result = []
    for bucket in buckets:
        result += bucket
    return result
def radix_sort(list_to_sort):
    # get the longest element
    longest = max(len(str) for str in list_to_sort)
    # print(longest)
    # pad all the strings shorter than "longest"
    list_to_sort = [str.ljust(longest,' ') for str in list_to_sort] 
    # print(list_to_sort)
    # loop through the characters one at a time, and bucket
    for i in range(longest - 1, -1, -1):
        list_to_sort = bucket_sorter(list_to_sort,i)
    # print(list_to_sort)
    sorted_list_without_pad = [word.strip() for word in list_to_sort]
    return sorted_list_without_pad
animals = [
    "cat",
    "bat",
    "dog",
    "elephant",
    "giraffe",
    "donkey",
    "horse",
]

sorted_list = radix_sort(animals)
print(sorted_list)

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")
