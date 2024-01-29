#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if el == search else el for el in my_list]
    return new_list
# new_lists = []
#     for el in my_list:
#         if el == search:
#             new_lists.append(replace)
#         else:
#             new_lists.append(el)
#     return new_lists
