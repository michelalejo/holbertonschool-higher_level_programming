#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    k = 0
    if len(my_list) <= 0:
        return(0)

    if len(my_list) > 2:
        for i in range(max(my_list[1:])):
            if my_list[i-1] == my_list[i]:
                del my_list[i]
        for p in range(len(my_list)):
            k = k + my_list[p]
        return(k)

    if len(my_list) >= 2:
        for i in range(max(my_list[1:])):
            if my_list[i-1] == my_list[i]:
                del my_list[i]
        for p in range(len(my_list)):
            if my_list[p-1] != my_list[p]:
                k = k + my_list[p]
            return(k)

    if len(my_list) == 1:
        k = k + my_list[0]
        return(k)
