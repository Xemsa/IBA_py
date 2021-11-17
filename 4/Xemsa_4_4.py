#4.4
# not in
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_uni_list = []
for i in my_list:
    if i not in my_uni_list:
        my_uni_list.append(i)

print (my_uni_list)