#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    result = 0
    for x in range(len(argv) -1 ):
        result += int(argv[x + 1])
        print("{}".format(result))
