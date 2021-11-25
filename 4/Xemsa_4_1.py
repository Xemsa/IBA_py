# 4.1
# list 1
li = [1,2,3,4,5]
# print(li)
#step 0
le = len(li)
print(le)
#step 1
lmid=le//2
# li[lmid] = int('9')
li[lmid] = int(input("integer, plz "))
print(li)
#step 2
del li[-1]
print(li)

#step 3
print(len(li))
