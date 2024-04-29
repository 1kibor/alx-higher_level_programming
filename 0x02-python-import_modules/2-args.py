#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    number_of_args = len(argv) - 1
    if number_of_args < 1:
        print("{} arguments.".format(number_of_args))
    elif number_of_args == 1:
        print("{} argument:".format(number_of_args))
    else:
        print("{} arguments:".format(number_of_args))
    for x in range(number_of_args):
        print("{}: {:s}".format(x + 1, argv[x + 1]))
