#!/usr/bin/python3
for num in range(99):
    if num / 10 < num % 10 and num != 89:
        print('{:02d},'.format(num), end=' ')
    elif num == 89:
        print(num)
