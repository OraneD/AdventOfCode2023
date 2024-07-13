#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 21:18:16 2024

@author: orane
"""
import math
from itertools import cycle


def parse_file(inp):
    dico = {}
    instructions =  inp.split("\n")[0]
    path = inp.split("\n")[2:-1]
    for tup in path :
        location = tup.split("=")[0].strip()
        ways =(tup.split("=")[1].strip().split(",")[0].strip("("), tup.split("=")[1].strip().split(",")[1].strip(")"))
        dico[location] = ways
    return instructions, dico

def find_way(start, direction, path):
    if direction == "R" :
        i = 1
    elif direction == "L" :
        i = 0
    return path[start.strip()][i]

def find_z(start, instructions, path):
    for i, instruction in enumerate(cycle(instructions)):
        if start[-1] == "Z":
            return i
        start = find_way(start, instruction, path).strip()
    return -1
        
def main_p2():
    with open("input.txt", "r") as file:
        inp = file.read()  
    instructions, path = parse_file(inp)
    starts = [x for x in path.keys() if x[-1] == "A"]
    ghost_ways = []
    for start in starts :
        ghost_ways.append(find_z(start, instructions, path))
    return math.lcm(*ghost_ways)

print(main_p2())