#5.1
#calc 3

def tr(n):
    try:
        return int(n)
    except:
        pass
    try:
        return float(n)
    except:
        pass
    return 0

def calc1(x,y,op):
    match op:
        case "+":
            return(x+y)
        case "-":
            return(x-y)
        case "*":
            return(x*y)
        case "/":
            return(x/y)
        case "**":
            return(x**y)
        case "//":
            return(x//y)
        case "%":
            return(x%y)
        case "odd":
            if (y % 2) != 0:
                print(f"Число {y} - нечётное")
            return(x)
        case "even":
            if (y % 2) == 0:
                print(f"Число {y} - чётное")
            return(x)
        case "type":
            print(type(y))
            return(x)
        case _:
            return(x)

def calc2(li:list,op:str):
    x=0
    match op:
        case "max":
            return(max(li))
        case "min":
            return(min(li))
        case "avg":
            return(sum(li)/len(li))
        case _:
            return(x)
        

an=n=0
o=''

while o!="exit":
    print("У вас есть",an)
    o=input("Действие ")
    o=o.lower()
    o.rstrip()
    if o == "exit":
        break
    elif o in ["max","min","avg"]:
        n = input("Числа через пробел ")
        n = ' '.join(n.split())
        li = list(map(tr,n.split(" ")))
        print(calc2(li,o))
    else:    
        n=tr(input("Число "))
        an=calc1(an,n,o)
