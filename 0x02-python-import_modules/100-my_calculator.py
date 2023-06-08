#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>"
              .format(sys.argv[0]))
        sys.exit(1)
    else:
        ops = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.argv[2] not in ops.keys():
            print("Unknown operator. Available operators: +, -, * and /")
        else:
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], ops[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))))
