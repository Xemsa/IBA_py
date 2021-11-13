#3.6
#геймлуп из 
print("Угадай число, магл")
i=0
while True:
    try:
        n=int(input())
    except:
        print('Я загадал целое число')
        n=0
    i+=1
    if n==7:
        print("Поздравляю, ты угадал")
        break
    if i%7==0:
        print("Ха-ха! Ты застрял в лупе")
    if i==99:
        print('Ты проиграл')
        break
