# 3.2
# max and min of 10

def tr(n):
    try:
        return int(n)
    except:
        pass
    try:
        return float(n)
    except:
        pass
    return 'NaN'

def maxof2(n1,n2):
    if n1 >= n2:
        return n1
    elif n2 > n1:
        return  n2

def minof2(n1,n2):
    if n1 >= n2:
        return n2
    elif n2 > n1:
        return  n1


f=0
'''for i in range(10):
    print ('Введите число №', i+1 )
    a=tr(input())
    if a=='NaN':
        continue #Если не число, пропускаем оборот
    if f == 0:
        min1=a
        max1=a
        f=1
    min1=minof2(min1,a)
    max1=maxof2(max1,a)'''
# если без цикла
a=tr(input("Введите число №1 "))
if a!='NaN':
    if f == 0:
        min1=a
        max1=a
        f=1

a=tr(input("Введите число №2 "))
if a!='NaN':
    if f == 0:
        min1=a
        max1=a
        f=1
    else:
        min1=minof2(min1,a)
        max1=maxof2(max1,a)

a=tr(input("Введите число №3 "))
if a!='NaN':
    if f == 0:
        min1=a
        max1=a
        f=1
    else:
        min1=minof2(min1,a)
        max1=maxof2(max1,a)

a=tr(input("Введите число №4 "))
if a!='NaN':
    if f == 0:
        min1=a
        max1=a
        f=1
    else:
        min1=minof2(min1,a)
        max1=maxof2(max1,a)

a=tr(input("Введите число №5 "))
if a!='NaN':
    if f == 0:
        min1=a
        max1=a
        f=1
    else:
        min1=minof2(min1,a)
        max1=maxof2(max1,a)

a=tr(input("Введите число №6 "))
if a!='NaN':
    if f == 0:
        min1=a
        max1=a
        f=1
    else:
        min1=minof2(min1,a)
        max1=maxof2(max1,a)

a=tr(input("Введите число №7 "))
if a!='NaN':
    if f == 0:
        min1=a
        max1=a
        f=1
    else:
        min1=minof2(min1,a)
        max1=maxof2(max1,a)

a=tr(input("Введите число №8 "))
if a!='NaN':
    if f == 0:
        min1=a
        max1=a
        f=1
    else:
        min1=minof2(min1,a)
        max1=maxof2(max1,a)

a=tr(input("Введите число №9 "))
if a!='NaN':
    if f == 0:
        min1=a
        max1=a
        f=1
    else:
        min1=minof2(min1,a)
        max1=maxof2(max1,a)

a=tr(input("Введите число №10 "))
if a!='NaN':
    if f == 0:
        min1=a
        max1=a
        f=1
    else:
        min1=minof2(min1,a)
        max1=maxof2(max1,a)


print(min1,max1)