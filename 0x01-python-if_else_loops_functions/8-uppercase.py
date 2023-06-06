#!/usr/bin/python3

def uppercase(str):
    for i in str:
        print("{}".format(chr(ord(i) - (ord('a') - ord('A')))
                          if (ord(i) >= ord('a') and
                              ord(i) <= ord('z')) else i),
              end="")
    print()
