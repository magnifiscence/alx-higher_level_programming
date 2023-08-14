#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """function prints integers of a list in reverse order"""
    if not my_list:
        pass
    else:
        for i in my_list[::-1]:
            print("{:d}".format(i))
