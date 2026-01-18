#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list.

    Returns a new list of True/False depending on divisibility by 2.
    """
    return [num % 2 == 0 for num in my_list]
