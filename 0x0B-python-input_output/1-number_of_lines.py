#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as star:
        for i in star:
            i += 1
    return i
