#!/usr/bin/python3
"""defines the function text_indentation(text)"""


def text_indentation(text):
    """prints a text with 2 new lines after some characters"""
    # testing for text type
    if type(text) is not str:
        raise TypeError("text must be a string")

    print_space = True
    for i in text:
        if i in ".?:":
            # prints 2 new lines
            print("\n")
            print_space = False
        elif i == " " and not print_space:
            continue
        else:
            print(i, end="")
            print_space = True
