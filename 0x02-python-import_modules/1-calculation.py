#!/usr/bin/python3
import add, sub, mul, div from calculator_1
if __name__ == "__main__":
    a = 10
    b = 5
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub*(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")
