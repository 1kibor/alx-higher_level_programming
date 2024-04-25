#!/usr/bin/python3
for letr in range(122, 96, -1):
    print("{:c}".format(letr if (letr % 2 == 0) else (letr - 32)), end='')
