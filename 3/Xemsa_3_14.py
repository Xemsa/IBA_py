#3.14
#34 bits

a = int('0101010111',2)
b =a & 0b110
b >>= 1

if b == 3:
    a -=6

print(a)
