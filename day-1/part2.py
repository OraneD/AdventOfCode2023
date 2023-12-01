#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:45:57 2023

@author: orane
"""
import regex as re

def load_input(file):
    with open(file,  "r") as file:
        return file.readlines()


def find_digits(line):
    return(re.findall("\d|one|two|three|four|five|six|seven|eight|nine", line,overlapped=True))

def compute_value(digits):
    numbers = range(1,10)
    number_letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    dico = {i : str(j) for i,j in zip(number_letters, numbers)}
    if len(digits) > 1 :
        digit_1 = digits[0] if re.search("\d", digits[0]) else dico[digits[0]]
        digit_2 = digits[-1] if re.search("\d", digits[-1]) else dico[digits[-1]]
        number = digit_1 + digit_2
        return int(number)
    number = digits[0] + digits[0] if re.search("\d", digits[0]) else dico[digits[0]] + dico[digits[0]]
    return int(number)

def main() :
    lines = load_input("input.txt")

    total = 0
    for line in lines :
        digits = find_digits(line)
        value = compute_value(digits)
        total += value
    print(f"total : {total}")


if __name__ == "__main__" : 
    main()