#!/usr/bin/python3
'''Write a function that appends a string at the end of a text file'''


def append_write(filename="", text=""):
    '''reads a file and write text'''
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
    return len(text)

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
