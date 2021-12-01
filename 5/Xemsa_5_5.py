#5.5
#prime

def is_prima(n:int):
    d = 0
    for i in range(1,n):
        if n%i==0:
            d += 1
    return (d < 2)

for i in range(1,20):
    if is_prima(i+1):
        print(i +1, end=" " )
