#!/usr/bin/python3
def multiplyAll(list_):
    result = 1
    for i in list_:
        result *= i
    return result


def sum_list(list_):
    sum = 0
    for i in list_:
        sum += i
    return sum


def weight_average(my_list=[]):
    if not len(my_list):
        return 0
    Nominator = list(map(multiplyAll, my_list))
    Denominator = [x[-1] for x in my_list]
    return sum_list(Nominator) / sum_list(Denominator)
