#!/usr/bin/python3
"""1. Write to a file"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file (UTF8) and
    returns the number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
