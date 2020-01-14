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
        coincidence = ['.', '?', ':']
        launch = 0
        for i, x in enumerate(text):
            if x in coincidence:
                print(text[launch:i + 1].strip() + "\n")
                launch = i + 1
        print(text[launch:].strip(), end='')
    if not isinstance(text, str):
        raise TypeError('text must be a string')
