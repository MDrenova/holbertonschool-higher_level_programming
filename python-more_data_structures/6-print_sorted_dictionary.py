#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(_dictionary.items()):
        print(f"{key}: {value}")
# or more like C:
# def print_sorted_dictionary(a_dictionary):
#   key_sort = sorted(a_dictionary.keys())
#   for i in range(len(a_dictionary)):
#     print(f"{key_sort[i]}: { a_dictionary.get(key_sort[i])}")
