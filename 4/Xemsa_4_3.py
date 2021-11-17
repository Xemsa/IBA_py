#4.3
#sort
# ps= [8, 10, 6, 2, 4]
# ps = [int(x) for x in input("через пробел ").split()]
# print("1",ps)

mylist = []
n = int(input("размер списка "))
for i in range(n):
    i = str(i+1)+" "
    k= int( input(i))
    mylist.append(k)

ps = mylist

def bsort(lis):
    # print("до сортировки \n",lis, sep="")
    le=len(lis)
    ok=True
    for i in range (le-1, 0, -1):
        for j in range(0,i):
            if lis[j + 1] < lis[j]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                ok = False
        if ok:
            # print("после сортировки \n",lis, sep="")
            return lis
    # print("после сортировки \n",lis, sep="")
    return lis

def rev_bsort(lis):
    nlis = bsort(lis)
    print(nlis)
    nlis.reverse()
    return nlis


print("Тип сортировки ", end="")
if input("i/r ") == "i":
    print ("increased may",bsort(ps))
    ps.sort()
    nps= ps
    print ("increased met", nps)
else:
    print ("reversed may",rev_bsort(ps))
    # ps.reverse()
    ps.sort(reverse=True)
    nps= ps
    print ("reversed met", nps)

