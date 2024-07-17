#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:40:58 2024

@author: orane
"""
def parse_input(inp):
    return [[x for x in line ] for line in inp.split("\n") if [x for x in line] != []]

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
            
def expand_universe(map_, empty_lines, empty_columns):
    for i, empty_line in enumerate(empty_lines):
        map_.insert(empty_line + i, ["."]*len(map_[0]))
    for i, empty_col in enumerate(empty_columns):
        for j in range(len(map_)):
            map_[j].insert(empty_col + i, ".")
    return map_
            
def find_galaxy(map_):
    galaxy = []
    for i, line in enumerate(map_):
        for j, char in enumerate(line) :
            if char != ".":
                galaxy.append((i,j))
    return galaxy

def make_pairs(galaxy):
    pairs = []
    for i, element in enumerate(galaxy) :
        remaining = galaxy[i + 1:]
        for rest in remaining :
            pairs.append((element,rest))
    return pairs

def find_way(start,dest):
    horizontal = abs(start[1] - dest[1])
    vertical = abs(start[0] - dest[0])
    return horizontal + vertical

    
def main():
    with open("input.txt", "r") as file :
        inp = file.read()
    map_ = parse_input(inp)
    empty_lines, empty_columns = find_empty(map_)
    map_expended = expand_universe(map_, empty_lines, empty_columns)
    galaxy = find_galaxy(map_expended)
    pairs = make_pairs(galaxy)
    result = 0
    for pair in pairs :
        start, dest = pair[0], pair[1]
        path_length = find_way(start,dest)
        result += path_length
    print(result)
main()
    
    
    

    