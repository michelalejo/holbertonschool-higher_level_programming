#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if number < 0:
    l = number % -10
else
    l = number % 10
print("Last digit of {} is {} and is ".format(n, l), end="")
if n > 5:
    print("greater than 5")
elif n == 0:
    print("0")
else:
    print("less than 6 and not 0")
