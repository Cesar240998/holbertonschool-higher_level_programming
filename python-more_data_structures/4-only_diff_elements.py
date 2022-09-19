#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    temp = []
    for item in set_1:
        if item not in set_2:
            temp.append(item)
    for item in set_2:
        if item not in set_1:
            temp.append(item)
    return temp
