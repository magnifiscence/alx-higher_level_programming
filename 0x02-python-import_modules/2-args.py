#!/usr/bin/python3

if __name__ == "__main__":
    """print list and number of arguments"""
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if size> 1:
        print("{} argument:".format(size))
        for i in range(1, size + 1):
            print("{}: {}".format(i, arg[i]))

        elif size == 0:
            print("{} arguments.".format(size))

        else:
            print("{} argument:".format(size))
            print("{}: {}".format(size, arg[1]))
