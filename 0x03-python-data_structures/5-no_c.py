#!/usr/bin/python3
def no_c(my_string):
    my_string_cp = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            my_string_cp += my_string[i]
    return(my_string_cp)
