#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 19:25:31 2024

@author: orane
"""
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

def main():
    with open("input.txt", "r") as file:
        inp = file.read()  
    instructions, path = parse_file(inp)
    start = "AAA"
    c = 0
    for direction in cycle(instructions):
       if start == "ZZZ":
        break
       start = find_way(start, direction, path).strip()
       c += 1

    print(f"Result : {c}")
    
main()
        
        