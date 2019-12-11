#!/usr/bin/python3
up = 0
for rev in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(rev - up)), end="")
    up = 32 if up == 0 else 0
