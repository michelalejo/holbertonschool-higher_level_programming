#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r') as s:
        for i in range(nb_lines):
                print(s.readline(), end="")
