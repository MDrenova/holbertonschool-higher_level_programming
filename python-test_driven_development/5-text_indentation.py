#!/usr/bin/python3
'''

Module to print a given text
and insterting newlines when encountaring
this type of characters . ? !
'''


def text_indentation(text):
    '''

    Function that prints the text given as argument
    and inserting newlines when encountaring this
    type of characters . ? !
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    spec_char = ".?:"

    for i in spec_char:
        text = text.replace(i, i + "\n\n").replace("\n\n ", "\n\n")
    print(text, end="")
