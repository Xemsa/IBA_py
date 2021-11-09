#2.5
#miles and kilometers
miles = 7.38
kilometers = 12.25
coef=1.609
m2k = round(miles * coef,2) 
print(miles, "miles is", m2k, "kilometers")
k2m = round(kilometers/coef,2) 
print(kilometers, 'kilometers is', k2m, 'miles')
