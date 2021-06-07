#!/usr/bin/python3
"""
Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Write a function that prints a text with 2
    new lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ignore_space = True
    for char in range(len(text)):
        if text[char] == ' ' and ignore_space:
            continue
        else:
            if text[char] not in ".?:":
                print(text[char], end='')
                ignore_space = False
            else:
                print(text[char], end='\n\n')
                ignore_space = True
