#4.8
"""
Write a program that reads two numbers aa and bb 
from the keyboard, calculates and displays the arithmetic 
mean of all numbers from the segment [a; b], which are 
multiples of 3.
In the example below, the arithmetic mean is 
calculated for numbers on the segment [-5; 12]. The total 
number of numbers divisible by 3 on this segment is 6: -
3, 0, 3, 6, 9, 12. Their arithmetic mean is 4.5
The program receives input to the intervals, within 
which there is always at least one number that is divisible 
by 3.
"""

n1 = int(input("Начало сегмента "))
n2 = int(input("Конец "))

li = [int(x) for x in range(n1,n2+1)]
an = []

for i in li:
    if i%3 == 0:
        an.append(i)

print(sum(an)/len(an))

