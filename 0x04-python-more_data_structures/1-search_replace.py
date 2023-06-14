#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [x for x in my_list if x != search else replace]
