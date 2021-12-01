#6.2
#fibonacci

def fibonacci(num:int):
    f1 = f2 = 1
    if num > 2:
        for i in range(num-2):
            f1, f2 = f2, f1 + f2
        return (f2)
    elif num in [1,2]: 
        return 1
    else: 
        return None

for i in range (-1,25):
    print(fibonacci(i))