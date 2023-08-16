#!/usr/bin/python3

def max_integer(my_list = []):
    """function that finds the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    biggest = my_list[0]
    for j in range(1, length):
        if my_list[j] > biggest:
            biggest = my_list[j]

            return (biggest)
