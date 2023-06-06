#!/usr/bin/python3

def uppercase(str):
    j = 0
    for i in str:
        j += 1
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            print("{}".format(chr(ord(i) - (ord('a') - ord('A')))),
                  end=("" if j != len(str) else "\n"))
        else:
            print("{}".format(i),
                  end=("" if j != len(str) else "\n"))
