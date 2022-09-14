#!/usr/bin/python3
"""this script defines a square based on the last file"""


class Square:
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    """

    def __init__(self, size=0):
        """initialises the size obj attr
        to size that was pased in
        private instance attribute: size"""

        self.__size = size

    @property
    def size(self):
        """getter function to get the atrr"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter function to set the attr"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        size.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
