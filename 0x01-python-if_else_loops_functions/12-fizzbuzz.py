#!/usr/bin/python3
def fizzbuzz():
    for fiz in range(1, 101):
        if fiz % 15 == 0:
            print("FizzBuzz", end=' ')
        elif fiz % 5 == 0:
            print("Buzz", end=' ')
        elif fiz % 3 == 0:
            print("Fizz", end=' ')
        else:
            print(fiz, end=' ')
