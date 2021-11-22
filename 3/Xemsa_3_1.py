#3.1
#largest of 4

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


def maxof2(n1,n2):
    if n1 >= n2:
        return n1
    elif n2 > n1:
        return  n2

a=b=c=d=0
print('a=')
a=tr(input())

print('b=')
b=tr(input())

print('c=')
c=tr(input())

print('d=')
d=tr(input())

m=maxof2(maxof2(a,b),maxof2(c,d))
print('наибольшее число',m)