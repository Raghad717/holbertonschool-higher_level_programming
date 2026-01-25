#!/usr/bin/python3
"""Defines a square with size, position, area computation, and printing."""


class Square:
    """Represents a square with a private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with optional size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position (x, y) of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for the private position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the private position attribute with validation.

        Args:
            value (tuple): The new position to set.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # to stdout with its position.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print each row with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
