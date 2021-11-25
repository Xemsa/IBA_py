# 4.2
# list 2

#step 1
beatles = []
print (beatles)

#step 2
beatles += ["John Lennon", "Paul McCartney", "George Harrison"]
print (beatles)

#step 3
for i in ['Stu Sutcliffe', 'Pete Best']:
    st_i = "Добавить " + i +"? y/n\n"
    if input(st_i) == "y":
    # if True:
        beatles.append (i)
        # print (beatles)
print (beatles)

#step 4
# foo = len(beatles)
# for i in range(foo):
#     if beatles[foo-i-1] in ['Stu Sutcliffe', 'Pete Best']:
#         del beatles[foo-i-1]
#         print (beatles)
# print (beatles)

for i in reversed(beatles):
    if i in ['Stu Sutcliffe', 'Pete Best']:
        beatles.remove(i)
        # print (beatles)
print (beatles)

#step 5
beatles.insert(0,"Ringo Starr")
print (beatles)