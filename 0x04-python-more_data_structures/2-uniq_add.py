#!/usr/bin/python3
def uniq_add(my_list=[]):
    sums = 0
    sums = list(dict.fromkeys(my_list))
    sums = sum(sums)
    return(sums)
