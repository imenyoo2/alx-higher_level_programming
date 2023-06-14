#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary:
        for i in range(list(a_dictionary).count(value)):
            del a_dictionary[value]
