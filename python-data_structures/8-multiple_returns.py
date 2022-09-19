#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if (size != 0):
        first_letter = sentence[0]
    new_tuple = (size, first_letter) if size > 0 else (size, None)
    return (new_tuple)
