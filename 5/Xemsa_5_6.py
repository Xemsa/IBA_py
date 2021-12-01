#5.6
#onvert

kmpm=1.609344
lpg = 3.785411784

def liters_100km_to_miles_gallon(lpk:float): 
    return (100 * lpg)/(lpk * kmpm)


def miles_gallon_to_liters_100km(mpg:float):
    return (100 * lpg) / (mpg * kmpm)

print (liters_100km_to_miles_gallon(3.9))
print (liters_100km_to_miles_gallon(7.5))
print (liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
