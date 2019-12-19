#!/usr/bin/python3
my_list = [1, 2, 3, 1, 4, 2, 5]
my_list.sort()
cp = my_list.copy()
j = -1
for i in range(1, len(cp)):
        if cp[i-1] == cp[i]:
                del cp[i]
print(cp)
print(my_list)
