#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 01:15:43 2023

@author: orane
"""
import re
def load_input(file):
    with open(file, 'r') as f :
        lines = f.readlines()
    return lines




def evaluate(line):
    sets = line.split(":")[1].split(";")
    for tirage in sets :
        nb_green = int(re.findall(r"\d+ green", tirage)[0].split()[0]) if re.search("green", tirage) else 0
        nb_red = int(re.findall(r"\d+ red", tirage)[0].split()[0]) if re.search("red", tirage) else 0
        nb_blue = int(re.findall(r"\d+ blue", tirage)[0].split()[0]) if re.search("blue", tirage) else 0
        if nb_green > 13 or nb_red > 12 or nb_blue > 14 :
            return False
    return True

def main() :
    inp = load_input("input.txt")
    result = 0
    for i, line in enumerate(inp):
        if evaluate(line) :
            result += i + 1
    print(result)
    
main()
            
