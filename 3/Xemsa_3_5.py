#3.5
#Високосный год
"""
if the year number isn't divisible by four, it's a common year;
• otherwise, if the year number isn't divisible by 100, it's a leap year;
• otherwise, if the year number isn't divisible by 400, it's a common 
year;
• otherwise, it's a leap year.
"""

a=2021

if a%4==0:
    if a%100==0:
        if a%400==0:
            print(a,'високосный')
        else:
            print(a,'обычный')
    else:
        print(a,'високосный')
else:
    print(a,'обычный')



