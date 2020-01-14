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

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for x in range(size):
            print('#' * size)
