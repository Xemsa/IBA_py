#6.1
#factorial

def factorial(num:int):
    an=1
    li = []
    if num > 1:
        li = [int(x) for x in range(1,num+1)]
    elif num in [0,1]:
        li = [1]
    else:
        return 
    for i in li:
        an *= i
    return an

for i in range (-1,9):
    print(factorial(i))

