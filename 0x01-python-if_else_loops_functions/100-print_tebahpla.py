#!/usr/bin/python3
for c in reversed(range(1, 27)):
    print("{}".format(chr(c + 64) if c % 2 != 0 else chr(c + 96)), end='')
