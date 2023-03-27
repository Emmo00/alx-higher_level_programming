#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    chars = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            chars += 1
    except NameError:
        pass
    finally:
        print("")
        return chars
