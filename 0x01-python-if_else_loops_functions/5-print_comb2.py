#!/usr/bin/python3
for de in range(100):
    if de != 99:
        print("{:d}, ".format(de), end="")
    else:
        print("{:d}".format(de), end="\n")
