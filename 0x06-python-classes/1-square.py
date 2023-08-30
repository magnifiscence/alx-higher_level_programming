#!/usr/bin/python3
"""
Module 1-square
Defines a class Square with size as a private attribute
"""

class Square:
    """
    class Square definition

    Args:
    size : size of side of a square
    """
    def __init__(self, size):
        """
        initializes square

        Attributes:
        size: size of side of a square
        """
        self.__size = size
