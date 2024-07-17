#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:43:32 2024

@author: orane
"""

def parse_inp(inp):
    return [line for line in inp.split("\n")]
    
def find_start(parsed_inp):
    for i, line in enumerate(parsed_inp):
        if "S"  in line :
            return i, line.index("S")
        
def find_first(i_start):
    left = (i_start[0], i_start[1]-1)
    if find_pipe_type(left, parsed_inp) in ["7", "J", "|", "."]:
        left = None
    right = (i_start[0], i_start[1]+1)
    if find_pipe_type(right, parsed_inp) in ["F","L", "|", "."]:
        right = None
    up = (i_start[0]-1, i_start[1])
    if find_pipe_type(up, parsed_inp) in ["-", ".", "L", "J"]:
        up = None
    down = (i_start[0]+1, i_start[1])
    if find_pipe_type(down, parsed_inp) in ["-", ".", "F", "7"]:
        down = None
    return [left, right, up, down]

def find_pipe_type(idx, parsed_inp):
    return parsed_inp[idx[0]][idx[1]]

def find_next(previous_idx, idx):
    pipe = find_pipe_type(idx, parsed_inp)
    new_previous = idx
    if pipe == "|":
        next_idx = (idx[0] + 1, idx[1]) if (idx[0] + 1, idx[1]) != previous_idx else (idx[0] - 1, idx[1])
    if pipe == "-":
        next_idx = (idx[0], idx[1] +1) if (idx[0], idx[1] +1) != previous_idx else (idx[0], idx[1] -1)
    if pipe == "L" :
        next_idx = (idx[0] -1, idx[1] ) if (idx[0] -1, idx[1]) != previous_idx else (idx[0], idx[1] +1)
    if pipe == "J" :
        next_idx = (idx[0] , idx[1] -1) if (idx[0], idx[1] -1) != previous_idx else (idx[0] -1, idx[1])
    if pipe == "7" :
        next_idx = (idx[0] +1, idx[1] ) if (idx[0] +1, idx[1]) != previous_idx else (idx[0], idx[1] -1)
    if pipe == "F" :
        next_idx = (idx[0], idx[1] +1) if (idx[0], idx[1] +1) != previous_idx else (idx[0] +1, idx[1])
    type_next = find_pipe_type(next_idx, parsed_inp)
    return new_previous, next_idx
    
with open("input.txt", "r") as file :
    inp = file.read()
parsed_inp = parse_inp(inp) 
new_map = [[x for x in line] for line in parsed_inp]
start = find_start(parsed_inp)
lst_first = find_first(start)
previous_idx = start
idx = lst_first[1]
if idx :
    starting_type = find_pipe_type(idx, parsed_inp)
    print(f"Starting from {starting_type}")
    next_idx = idx
    c = 0
    while find_pipe_type(next_idx, parsed_inp) != "S":
        if find_pipe_type(idx, parsed_inp) != ".":
            new_map[previous_idx[0]][previous_idx[1]] = "*" if new_map[previous_idx[0]][previous_idx[1]] != "S" else "S"
            previous_idx, next_idx = find_next(previous_idx, next_idx)
            c += 1
        else :
            break
    print(c)

    with open("new_map.txt", "w") as file :
        for line in new_map :
            file.write("".join(line) + "\n")
with open("new_map.txt", "r") as file :
    new_map = file.read()
new_map_parsed = parse_inp(new_map)

for i, line in enumerate(new_map):
    for j, letter in enumerate(line):
        if letter == "."
