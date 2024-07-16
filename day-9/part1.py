#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:42:19 2024

@author: orane
"""

def parse_input(inp):
    parsed = []
    lines = inp.split("\n")
    for line in lines :
        num = [int(x) for x in line.split() if x.isdigit()]
        parsed.append(num) 
    return parsed


def compute_next_num(parsed_input):
    final = []
    print(parsed_input)
    current = [num for num in parsed_input]
    #print(current)
    while not all(num == 0 for num in current):
        final.append(current)
        current = [current[i+1] - current[i] for i in range(len(current)-1)]
    return sum([line[-1] for line in final])
    

def main():
    with open("input.txt", "r") as file :
        inp = file.read()
    parsed = parse_input(inp)
    c = 0
    for line in parsed :
        if line != []:
            c += compute_next_num(line)
    print(c)

main()



    
        