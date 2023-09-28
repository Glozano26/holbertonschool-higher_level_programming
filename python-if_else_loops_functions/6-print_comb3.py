#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        n = i * 10 + j
        if n == 89:
            print("{:02}".format(n))
        else:
            print("{:02}, ".format(n), end="")
