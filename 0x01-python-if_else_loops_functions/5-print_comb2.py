#!/usr/bin/python3
for i in range(100):
    end = ', ' if i < 99 else '\n'
    print("{}".format(i if i > 9 else '0' + str(i)), end=end)
