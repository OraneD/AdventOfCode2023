#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:40:58 2024

@author: orane
"""

example = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

def parse_input(inp):
    return [[x for x in line ]for line in inp.split("\n")]

def name_universe(map_):
    name = 1
    for line in map_:
        for i, char in enumerate(line) :
            if char == "#":
                line[i] = str(name)
                name += 1
    return map_
            

def find_empty(map_):
    map_ = name_universe(map_)
    empty_lines = [i for i in range(len(map_)) if all(x == "." for x in map_[i])]    
    empty_columns = []
    i = 0
    while i < len(map_[0]):
        for j in range(len(map_)):
            empty = True
            if map_[j][i] != ".":
                empty = False
                break
        if empty == True :
            empty_columns.append(i)
        i +=1
    return (empty_lines, empty_columns)
            
def expand_universe(map_):
    for i, empty_line in enumerate(empty_lines):
        map_.insert(empty_line + i, ["."]*len(map_[0]))
    for i, empty_col in enumerate(empty_columns):
        for j in range(len(map_)):
            map_[j].insert(empty_col + i, ".")
    return map_
            

        
map_ = parse_input(example)
empty_lines, empty_columns = find_empty(map_)
map_expended = expand_universe(map_)
for line in map_expended :
    print(line)


    