#!/usr/bin/python3
""" Find the Peak"""
def find_peak(list_of_integers):
    max = 0
    for n in list_of_integers:
        if n > max:
            max = n
    if max > 0:
        return (max)
    else:
        return (None)