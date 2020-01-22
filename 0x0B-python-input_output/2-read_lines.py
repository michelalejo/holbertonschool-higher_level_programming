#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as s:
        for i in range(nb_lines):
                print(s.readline(), end="")
