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
    if isinstance(size, int):
        for i in range(size):
            for j in range(size):
                print('#', end="")
            print()
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
