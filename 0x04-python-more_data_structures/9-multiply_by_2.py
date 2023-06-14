#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = {}
    for i in list(a_dictionary):
        result[i] = a_dictionary[i] * 2
    return result
