#11.2
#text file*

from os import strerror
# fname = input("File name? \n")
fname ='E:/git/IBA_py/11/file111.txt'
try:
    fil = open(fname, mode='r', encoding='utf-8')   
except IOError as e:
    print("Cannot open the file: ",strerror(e.errno))
else:    
    st = fil.read() 
    fil.close()
# открыли прочли закрыли

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
# заполнил словарь чем юзер послал

# Tip: Use a lambda to change the sort order. 
printme = [x for x in sorted(di.items(), reverse=True, key = lambda kv:(kv[1], kv[0]))] 
# создаём лист кортежей отсортированных по убыванию частот буков в файле



with open("E:/git/IBA_py/11/file111.hist",'w',encoding = 'utf-8') as f:
    for i in range(len(printme)):
        t=printme[i]
        f.write(str(t[0]) + ' --> ' + str(t[1]) + '\n')

for i in range(len(printme)):
    t=printme[i]
    # достали кортежик
    print(t[0],t[1], sep=" --> ", end ="\n")
    # записали



