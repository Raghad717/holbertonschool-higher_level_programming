#!/usr/bin/python3
"""Defines a square with size property, area computation, and printing."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize the square with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size  # Use setter to validate automatically

    @property
    def size(self):
        """Getter for the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the private size attribute with validation.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character # to stdout.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
