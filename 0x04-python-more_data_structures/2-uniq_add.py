#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    cp = my_list.copy()
    k = 0
    for i in range(max(cp[1:])):
        j = i - 1
        if cp[i-1] == cp[j-1]:
            del cp[i-1]
    for j in range(len(cp)):
        k = k + cp[j]
    return(k)
