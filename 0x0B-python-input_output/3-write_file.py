#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    j = 0
    with open(filename, encoding='utf-8') as s:
        for i in s:
            j += 1
            if nb_lines <= 0 or j <= nb_lines:
                print(i, end="")
