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

def getDaysInMonth(month, year):
    # if feb, check for leap
    if(month == 1 and (year % 4 == 0 or year == 2000)):
        # this is a leap
        return 29
    else:
        return months[month]
     

# leapOn
dayOfWeek = 2 #first day of 1900
months = [31,28,31,30,31,30,31,31,30,31,30,31]
numSundays = 0
# outter loop for year
for year in range(1900,1902):
    # inner loop for month
    for month in range(0,12):
        
        # start of month. Check if dayOfWeek = 0
        if(dayOfWeek == 1 and year != 1900): #need to skip 1900
            print(dayOfWeek,"/",month)
            numSundays += 1
        daysInMonth = getDaysInMonth(month, year)
        # we have the days in this month. Get through them and find new 1
        for date in range(0,daysInMonth):
            print(year,"/",month,"/",date,"-",dayOfWeek)
            dayOfWeek = 1 if dayOfWeek == 7 else dayOfWeek + 1
print(numSundays)        

# JS
# for (let year = 1701; year <= 1800; year++ ){
# 	// inner loop for month
# 	// use 0-11 because the date obj uses 0-11
# 	for(let month = 0; month <= 11; month++){
# 		// pass the date (year, month, 1)
# 		var dateObj = new Date(year, month, 1);
# 		// getDay will return 0-6, 0 for Sunday, 6 for Saturday
# 		var dayOfWeek = dateObj.getDay();
# 		// console.log(dayOfWeek);
# 		if(dayOfWeek == 6){
# 			// it's saturday, and teh 1st day o the month!!
# 			firstSat.push(dateObj);
# 		}
# 	}
# }

# console.log(firstSat.length)
# // console.log(firstSat[12])

# ////WITH FUNCTION
# // Instantiate input variables
# var startYear;
# var endYear;
# function monthsStartingOnSaturday(startYear,endYear,dayOfWeek = 6){
#     // Initialize loop variables
#     var checkDate = new Date(0,0,1,0,0,0,0);
#     var saturdays = 0;
#     var year;
    
# for(year = startYear; year <= endYear; year++){
#     checkDate.setYear(year);
#     for(month = 0; month < 12; month++){
#         checkDate.setMonth(month);
#         if(checkDate.getDay() == dayOfWeek){
#             saturdays++;
#         }
#         else{
#             continue;
#         }
#     }
# }
# return saturdays
# }
# console.log(monthsStartingOnSaturday(1701,1800,6));


# // SCARY/AWESOME WAY...
# var year = 1701;
# var day = 0;
# var daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
# var count = 1;
# while(year <= 1800){
#     for(let i = 0; i < daysInMonth.length; i++){
#         if(year % 4 != 0 || year % 100 == 0 && year % 400 != 0){
#             daysInMonth[1] = 28;
#         }else{
#             // console.log(year);
#             daysInMonth[1] = 29;
#         }
#         day += daysInMonth[i];
#         if (day % 7 == 0){
#             count++
#         }
#     }
#     year++;
#     }
# console.log(count);
