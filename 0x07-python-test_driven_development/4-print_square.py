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
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
