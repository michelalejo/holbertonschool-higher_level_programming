#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    k = 0
    for i in range(max(my_list[1:])):
        j = i - 1
        if my_list[i-1] == my_list[j-1]:
            del my_list[i-1]
    for j in range(len(my_list)):
        k = k + my_list[j]
    return(k)
