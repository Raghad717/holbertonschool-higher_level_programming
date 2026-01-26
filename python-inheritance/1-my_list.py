#!/usr/bin/python3
"""
1-my_list module
Contains the MyList class that inherits from list
and can print itself sorted.
"""


class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original."""
        print(sorted(self))
