#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    else:
        val_dict = a_dictionary.values()
        maxim_val = max(val_dict)
        for k, v in a_dictionary.items():
            if v == maxim_val:
                return k
