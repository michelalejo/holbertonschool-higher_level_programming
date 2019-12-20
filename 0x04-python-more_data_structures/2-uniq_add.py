#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    k = 0
    if len(my_list) <= 0:
        return(0)

    if len(my_list) == 1:
        k = k + my_list[0]
        return(k)

    if len(my_list) > 1:
        for i in range(1, len(my_list.copy())):
            if i < len(my_list) - 1:
                if my_list[i] == my_list[i-1]:
                    del my_list[i]
                    print(my_list)
        for p in range(len(my_list)):
            k = k + my_list[p]
        return(k)
