#!/usr/bin/python3
"""
Programt that prints a text with 2 new lines after each coincidence
coincidence characters: ., ? and :
Return: none
"""


def text_indentation(text):
    """Programt that prints a text with 2 new lines after each coincidence
    coincidence characters: ., ? and :
    Return: none"""

    if isinstance(text, str):
        form = ['.', '?', ':']
        start = 0
        for i, x in enumerate(text):
            if x in form:
                print(text[start:i + 1].strip() + '\n')
                start = i + 1
        print(text[start:].strip(), end='')
    if not isinstance(text, str):
        raise TypeError('text must be a string')
