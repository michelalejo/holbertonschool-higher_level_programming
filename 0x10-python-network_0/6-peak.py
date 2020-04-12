#!/usr/bin/python3
""" Find the Peak"""
def find_peak(list_of_integers):
    if list_of_integers == []:
        return
    max = 0
    for n in list_of_integers:
        if n > max:
            max = n
    return (max)