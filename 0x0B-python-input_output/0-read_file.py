#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as star:
        info = star.read()
    print(info, end="")
