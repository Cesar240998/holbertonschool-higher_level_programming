#!/usr/bin/python3
"""
This program appends a string at the end of a text file (UTF8) and returns the number of characters added
"""


def write_file(filename="", text=""):
    """
    Write in a file, if doesn't exists create the file
    """

    with open(filename, mode="a", encoding="utf-8") as _file:
        _file.write(text)

    return (len(text))
