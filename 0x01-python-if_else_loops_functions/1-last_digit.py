#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
text = ""
last_digit = number % 10 if number > 0 else -(-number % 10)
if last_digit > 5:
    text = "and is greater than 5"
elif last_digit == 0:
    text = "and is 0"
elif last_digit < 6:
    text = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} {text}")
