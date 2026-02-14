#!/usr/bin/python3


def replace_in_list(my_list, idx, element):

    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    my_list[idx] = element

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {} is {}".format(idx, element_at(my_list, idx)))