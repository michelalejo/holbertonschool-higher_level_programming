#!/usr/bin/python3
"""
Programt that prints a square
Print with '#'
Return: none
"""


def print_square(size):
    """Programt that prints a square
    Print with '#'
    Return: none"""

    if type(size) is float:
        if size < 0:
            raise TypeError('size must be an integer')
        size = int(size)
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
