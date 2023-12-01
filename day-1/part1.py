#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:21:46 2023

@author: orane
"""

import re

def load_input(file):
    with open(file,  "r") as file:
        return file.readlines()


def find_digits(line):
    return(re.findall("\d", line))

def compute_value(digits):
    if len(digits) > 1 :
        number = digits[0] + digits[-1]
        return int(number)
    number = digits[0] + digits[0]
    return int(number)

def main() :
    lines = load_input("input.txt")
    total = 0
    for line in lines :
        digits = find_digits(line)
        value = compute_value(digits)
        total += value
    print(total)

main()
    
       