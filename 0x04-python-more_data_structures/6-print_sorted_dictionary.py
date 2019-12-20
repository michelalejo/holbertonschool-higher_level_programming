#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = a_dictionary
    for i, j in sorted(a.items()):
        print("{}: {}".format(i, j))
