#!/usr/bin/python3

if __name__ == "__main__":
    """print list and number of arguments"""
    import sys

    count = len(sys.argv)
    if count == 0:
        print("0 arguments.\n")
    elif count == 1:
        print("1 argument:\n")
    else:
        print("{} arguments:".format(count))
        for i in range(count):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
