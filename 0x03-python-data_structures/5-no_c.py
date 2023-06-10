#!/usr/bin/python3
def no_c(my_string):
    clearedString = ""
    for i in my_string:
        if i != "c" or i != "C":
            clearedString += i
    return clearedString
