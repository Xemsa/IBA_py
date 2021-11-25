#4.6
#repeat
s = input("целые числа через пробел ")
bar=list(map(int,s.split(" ")))
# bar = [ 1, 0, 2, 0, 2,1]
bar.sort()
foo=[]
for i in bar:
    if i in foo:
        continue
    temp=i
    bar.remove(i)
    if temp in bar:
        foo.append (temp)
print (foo)