#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    argv = sys.argv[1:]

    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, "" if argc == 1 else "s"))
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))
