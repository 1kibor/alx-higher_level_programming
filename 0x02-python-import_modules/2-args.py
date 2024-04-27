#!/usr/bin/python3
if __name__ =="__main__":
    from sys import argv
    x_args = len(argv) - 1

    if x_args == 0:
        print("{} arguments.".format(x_args))

    elif x_args == 1:
        print("{} argument:".format(x_args))

    else:
        print("{} arguments:".format(x_args))

        for i in range(x_args):
            print("{}: {:s}".format(i + 1, argv[i + 1]))
