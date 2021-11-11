#2.6
#algebra

def y(x):
    y=3*x**3 - 2*x**2 + 3*x - 1
    return y

'''
x = 0
print(y(x)*1.0)

x = 1
print(float(y(x)))

x = -1
print(y(x)/1)
'''
x=float(input())
print(y(x))