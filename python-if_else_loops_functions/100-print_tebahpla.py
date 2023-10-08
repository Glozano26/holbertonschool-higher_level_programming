#!/usr/bin/python3
for low, upp in zip(range(122, 97, -2), range(89, 64, -2)):
    print("{}{}".format(chr(low), chr(upp)), end="")
