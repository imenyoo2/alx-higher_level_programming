#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv[1:]) <= 1:
        print("{} argument".format(len(sys.argv[1:])), end="")
    else:
        print(len(sys.argv[1:]), "arguments", end="")
    if len(sys.argv[1:]) == 0:
        print(".")
    else:
        print(":")
        j = 1
        for i in sys.argv[1:]:
            print("{}: {}".format(j, i))
            j += 1
