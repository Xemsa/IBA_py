#11.1
#text file
fil = open('file111.txt', mode='r', encoding='utf-8')
st = fil.read() 
fil.close()
di = dict()
for i in range(len(st)):     
    al=st[i].lower()
    if not al.isalpha():
        continue
    if al not in di: 
        di[al] =1
    else:
        va = di[al] + 1
        di[al] = va

for i in sorted (di):
    print (i, di[i], sep=" --> ", end ="\n")

# counters = {st(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
# print (counters)