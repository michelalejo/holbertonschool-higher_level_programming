#!/usr/bin/python3
def uppercase(str):
    for lo in str:
        if ord(lo) > 96 and ord(lo) < 123:
            up = ord(lo) - 32
        else:
            up = ord(lo)
        print("{:c}".format(up), end="")
    else:
        print()
