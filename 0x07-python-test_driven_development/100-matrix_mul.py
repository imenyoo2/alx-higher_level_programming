#!/usr/bin/python3
"""define matrix_mul function"""


def test_matrix(m_a, m_b):
    """test mat and raise failure exeptions with name"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")
    else:
        for l1 in m_a:
            if type(l1) is not list:
                raise TypeError("m_a must be a list of lists")
        for l2 in m_b:
            if type(l2) is not list:
                raise TypeError("m_b must be a list of lists")
        for l1 in m_a:
            for i in l1:
                if type(i) is not int and type(i) is not float:
                    raise TypeError("m_a should contain only " +
                                    "integers or floats")
        for l2 in m_b:
            for i in l2:
                if type(i) is not int and type(i) is not float:
                    raise TypeError("m_b should contain only " +
                                    "integers or floats")
    # testing for empty
    if m_a == [] or m_a[0] == []:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b[0] == []:
        raise ValueError("m_b can't be empty")
    # testing for equal lengh rows
    length = len(m_a[0])
    for li in m_a:
        if len(li) != length:
            raise TypeError("each row of m_a must be of the same size")

    length = len(m_b[0])
    for li in m_b:
        if len(li) != length:
            raise TypeError("each row of m_b must be of the same size")


def get_col(mat, index):
    """get column at index"""
    col = []
    for row in mat:
        col.append(row[index])
    return col


def test_compatible_size(m_a, m_b):
    """test if 2 matrices can be multiplied"""
    if len(m_a[0]) != len(get_col(m_b, 0)):
        raise ValueError("m_a and m_b can't be multiplied")


def mul_1d(l_1, l_2):
    """multiply 2 1d matrices"""
    sum = 0
    for index, _ in enumerate(l_1):
        sum += l_1[index] * l_2[index]
    return sum


def matrix_mul(m_a, m_b):
    """multiply two matrices"""
    # testing for correct type for m_a and m_b
    test_matrix(m_a, m_b)
    test_compatible_size(m_a, m_b)

    result = []
    for val in m_a:
        row = []
        for index in range(len(m_b[0])):
            row.append(mul_1d(val, get_col(m_b, index)))
        result.append(row)
    return result
