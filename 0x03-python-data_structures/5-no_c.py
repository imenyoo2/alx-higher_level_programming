#!/usr/bin/python3
def no_c(my_string):
    clearedString = ""
    for i in my_string:
        if i != "c" and i != "C":
            clearedString += i
    return clearedString
