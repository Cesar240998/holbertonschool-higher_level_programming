#!/usr/bin/python3
"""
This program appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Write in a file, if doesn't exists create the file
    """

    with open(filename, mode="a", encoding="utf-8") as _file:
        _file.write(text)

    return (len(text))
