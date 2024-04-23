#!/usr/bin/python3
def uppercase(str):
    upp_str = ''
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            upp_str = upp_str + chr(ord(x)-32)
        else:
            upp_str = upp_str + x
    print('{}'.format(upp_str))
