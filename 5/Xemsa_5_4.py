#5.4
#дай оф еаре

def is_year_leap(year:int):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def days_in_month(year:int, month:int):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month in [2]:
        return 28 + is_year_leap(year)
    else: 
        return 0

def day_of_year(year:int, month:int, day:int):
    sumdays = 0
    for i in range(month):
        sumdays += days_in_month(year, i)
    return sumdays + day

print (day_of_year(2021,11,21))
