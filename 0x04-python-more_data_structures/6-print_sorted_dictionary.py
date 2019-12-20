#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = a_dictionary
    for i in sorted(a.keys()):
        print("{}: {}".format(i, a.get(i)))
