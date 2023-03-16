#!/usr/bin/python3
def roman_to_int(roman_string:str):
    con = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    number = 0
    roman_numerals = list(roman_string)
    for i in range(len(roman_numerals)):
        if i == 0:
            number = con[roman_numerals[i]]
            continue
        if con[roman_numerals[i]] <= con[roman_numerals[i - 1]]:
            number = number + con[roman_numerals[i]]
        elif con[roman_numerals[i]] > con[roman_numerals[i - 1]]:
            number = con[roman_numerals[i]] - number
    return number
    