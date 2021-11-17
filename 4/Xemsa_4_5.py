#4.5
#split
s = input("целые числа через пробел ")
li1=s.split(" ")
# print(li1)
# a = 0
numbers = [0]
for i in li1:
    numbers.append(int(i))
# a = sum(numbers)
print(sum(numbers))