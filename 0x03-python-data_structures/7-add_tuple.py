#!/usr/bin/python
def add_tuple(tuple_a=(), tuple_b=()):
    length = min(len(tuple_a), len(tuple_b))
    buffer = []
    for i in range(2):
        if i > length - 1:
            buffer.append(0)
            if len(tuple_a) > length:
                buffer[i] += tuple_a[i]
            else:
                buffer[i] += tuple_b[i]
        else:
            buffer.append(tuple_a[i] + tuple_b[i])
    return (buffer[0], buffer[1])
