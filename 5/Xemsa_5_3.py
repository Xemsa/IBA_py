#5.3
#leap 3 + days

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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end = " ")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")