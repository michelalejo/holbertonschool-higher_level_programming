#!/usr/bin/python3
"""
Programt that prints a name
prints My name is <first name> <last name>
Return: none
"""
def say_my_name(first_name, last_name=""):
    """Programt that prints a name
    prints My name is <first name> <last name>
    Return: none"""
    fn = 0
    ln = 0
    if type(first_name) is str:
        fn = 1
    else:
        raise TypeError('first_name must be a string')
    if type(last_name) is str:
        ln = 1
    else:
        raise TypeError('last_name must be a string')

    if fn == 1 and ln == 0:
        print("My name is {} ".format(first_name))
    elif fn == 0 and ln == 1:
        print("My last name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
