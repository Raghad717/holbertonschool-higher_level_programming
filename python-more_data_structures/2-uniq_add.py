#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list and return the sum."""
    unique_numbers = set(my_list)
    return sum(unique_numbers)
