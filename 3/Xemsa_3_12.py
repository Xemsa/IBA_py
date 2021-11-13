#3.12


# Write the calculator.
# Operations: + - / * ** // % and or 
# not type() round() max() min()
# • Use the input() to get type of 
# operation and data from user.
# • input() int() float() type() and so 
# on. Comments###
# • use if/elif/esle, for/while

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
        case _:
            return(x)
an=0
o=''

while o!="exit":
    print("У вас есть",an)
    o=input("действие ")
    n=tr(input("число "))
    an=calc1(an,n,o)
