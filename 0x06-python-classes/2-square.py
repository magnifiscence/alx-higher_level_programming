#!/usr/bin/python3
"""
Defines a class Square with size as private attribute
"""


class Square:
    """
    class Square definition

    Args:
    size: size of a side in square
    """
    def __init__(self, size=0):
        self._size = size
        try
        size == int
        except
        raise TypeError:
            print("size must be an integer")

            try
            size >= 0
            except
            raise ValueError:
                print("size must be >= 0")
