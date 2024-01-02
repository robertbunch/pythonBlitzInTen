import time
start_time = time.time() #get our starting time
# Answer: 171
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def get_num_days(month,year):
    if(month == 2):
        #this is feb. is it a leap year?
        if(year % 400 == 0):
            #this is a century leap year
            return 29
        elif(year % 4 == 0 and year % 100 != 0):
            # this is a non-century leap year
            return 29
        else:
            # this is a non-leap feb
            return 28
    else:
        return months[month]

#0 in index 0 so January can be index 1
months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day_of_week = 2 #Sunday = 1, Monday = 2, etc.
number_of_sundays = 0 #init final answer
sundays_by_year = {}

#year loop - we only need to check every 28 years, becaues the calendar repeats
for year in range(1900,1929):
    sundays_by_year[year] = 0
    #is this a leap year
    for month in range(1,13):
        num_days_in_month = get_num_days(month, year)
        # print("year: ",year," month: ",month,"-",num_days_in_month)
        if(day_of_week == 1):
            # this is a sunday! and the first day of this month
            sundays_by_year[year] += 1
            if(year != 1900): number_of_sundays += 1
        for date in range(1,num_days_in_month+1):
            # reset day of week to 1 if we were on 7, others incrament by 1
            day_of_week = 1 if day_of_week == 7 else day_of_week + 1

for year in range(1929,2001):
    sundays_by_year[year] = sundays_by_year[year - 28]
    number_of_sundays += sundays_by_year[year]

print(number_of_sundays)
print(sundays_by_year)

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")
