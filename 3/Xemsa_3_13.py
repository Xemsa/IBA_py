#3.13
#2 bits
a = int('1101',2)

b =a & 0b010
b >>= 1

if b == 0:
    a +=2
print(a)