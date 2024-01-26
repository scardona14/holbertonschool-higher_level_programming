#!/usr/bin/python3
def max_integer(my_list=[]):
    """Returns the max integer in a list of integers"""
    if my_list:
        my_list.sort()
        return my_list[-1]
    else:
        return None
