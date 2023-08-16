#!/usr/bin/python3
def new_in_list(my_list, idx, element):
""" function replaces an element in a newly copied list in a specified position"""
if idx < 0 or idx > len(my_list) - 1:
    return (my_list)

my_list2 = my_list.copy()
my_list2[idx] = element
return (my_list2)
