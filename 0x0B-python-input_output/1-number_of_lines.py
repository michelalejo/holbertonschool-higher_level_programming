#!/usr/bin/python3
def number_of_lines(filename=""):
    i = 0
    with open(filename, 'r') as f:
        for star in f:
            i += 1
    return i
