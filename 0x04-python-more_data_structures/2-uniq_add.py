#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    k = 0
    if len(my_list) <= 0:
        return(0)

    if len(my_list) > 1:
        for i in range(max(my_list[:])):
            j = i - 1
            if my_list[i-1] == my_list[j-1]:
                del my_list[i-1]
        for p in range(len(my_list)):
            k = k + my_list[p]
        return(k)

    if len(my_list) == 1:
        k = k + my_list[0]
        return(k)
