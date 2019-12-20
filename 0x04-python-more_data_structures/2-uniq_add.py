#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    list2 = []
    k = 0
    if len(my_list) <= 0:
        return(0)

    if len(my_list) == 1:
        k = k + my_list[0]
        return(k)

    if len(my_list) > 1:
        for i in range(0, len(my_list.copy())):
            if i < len(my_list) - 1:
                if my_list[i] != my_list[i+1]:
                    list2.append(my_list[i])
                    print(my_list)
            else:
                list2.append(my_list[i])
        for p in range(len(list2)):
            k = k + list2[p]
        return(k)
