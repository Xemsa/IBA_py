#3.4
#налоги
t=0.15
for i in range(5):
    try:
        a= float(input("Введите число "))
        print (round(a*t,2))
        break
    except:
        print('Хрень какая-то')
