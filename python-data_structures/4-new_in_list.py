#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Return a copy of the list with the element at idx replaced.

    Does not modify the original list.
    """
    new_list = my_list.copy()
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list
