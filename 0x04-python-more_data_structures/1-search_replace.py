#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list_cp = my_list.copy()
    for i in range(len(my_list_cp)):
        if my_list_cp[i] == search:
            my_list_cp[i] = replace
    return my_list_cp
