#!/usr/bin/python3
def roman_to_int(roman_string):
    con = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    if not roman_string or type(roman_string) != str:
        return 0
    for i in range(len(roman_string)):
        if i > 0 and con[roman_string[i]] > con[roman_string[i - 1]]:
            number += con[roman_string[i]] - 2 * con[roman_string[i - 1]] 
        else:
            number = number + con[roman_string[i]]
    return number
