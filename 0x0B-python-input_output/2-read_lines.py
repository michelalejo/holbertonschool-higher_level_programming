#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as s:
        if nb_lines > 0:
            for i in range(nb_lines):
                print(s.readline(), end="")
        else:
            ff = f.read()
            print(ff, end="")
