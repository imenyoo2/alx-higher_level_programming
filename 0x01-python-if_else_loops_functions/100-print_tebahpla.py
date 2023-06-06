#!/usr/bin/python3
# 26: the number of alphabets
arr = [ord('z'), ord('Z')]
toggle = 0
for i in range(26):
    print("{}".format(chr(arr[toggle] - i)), end="")
    if toggle == 0: toggle = 1
    else: toggle = 0
