#!/usr/bin/python3
for i in range(100):
    end = ', ' if i < 99 else '\n'
    print("{}".format(i), end=end)
