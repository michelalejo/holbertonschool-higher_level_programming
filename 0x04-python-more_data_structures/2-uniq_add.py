#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) <= 0:
        return(0)
    my_list.sort()
    k = 0
    for i in range(max(my_list[1:])):
        if my_list[i] == my_list[i-1]:
            del my_list[i]
    for p in range(len(my_list)):
        k = k + my_list[p]
    return(k)
