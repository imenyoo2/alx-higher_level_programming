#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in range(len(my_list)):
        if my_list.index(my_list[i]) == i:
            sum += my_list[i]
    return sum
