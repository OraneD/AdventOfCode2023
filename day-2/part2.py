#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 01:46:29 2023

@author: orane
"""

import re
def load_input(file):
    with open(file, 'r') as f :
        lines = f.readlines()
    return lines




def get_cubes_numbers(line):
    sets = line.split(":")[1].split(";")
    green, red, blue = [], [], []
    for tirage in sets :
        green.append(int(re.findall(r"\d+ green", tirage)[0].split()[0])) if re.search("green", tirage) else 0
        red.append(int(re.findall(r"\d+ red", tirage)[0].split()[0])) if re.search("red", tirage) else 0
        blue.append(int(re.findall(r"\d+ blue", tirage)[0].split()[0])) if re.search("blue", tirage) else 0
    return green, red, blue

def get_max(green, red, blue):
    max_green = max(green)
    max_blue = max(blue)
    max_red = max(red)
    return max_green, max_blue, max_red

def main() :
    inp = load_input("input.txt")
    result = 0
    for line in inp:
        nb_green, nb_red, nb_blue = get_cubes_numbers(line)
        max_green, max_red, max_blue = get_max(nb_green, nb_red, nb_blue)
        result += max_green * max_red * max_blue

    print(result)
    
main()
            