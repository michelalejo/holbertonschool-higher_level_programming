#!/usr/bin/python3
def best_score(a_dictionary):
    a = a_dictionary
    if a is None:
        return None
    j = 0
    for i in sorted(a.values()):
        if i > j:
            j = i
    return(j)
