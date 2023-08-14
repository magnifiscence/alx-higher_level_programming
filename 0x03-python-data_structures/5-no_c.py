#!/usr/bin/python3

def no_c(my_string):
    """ removes c and C characters from a string"""
    for item in my_string:
        if item == 'c' or item == 'C':
            item = ''
            new_string += item
            return (new_string)
