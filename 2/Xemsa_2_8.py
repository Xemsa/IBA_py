#2.8
#calc

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



print('x=')
x=int(input())

print('y=')
y=int(input())

print('operation is')
op=str(input())

print(calc1(x,y,op))



