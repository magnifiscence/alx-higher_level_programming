#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """function that replaces an element at a particular index in a list"""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
        return (my_list)
