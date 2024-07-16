#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:08:44 2024

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
start = find_start(parsed_inp)
lst_first = find_first(start)
previous_idx = start
for idx in lst_first :
    if idx :
        count = 0
        starting_type = find_pipe_type(idx, parsed_inp)
        print(f"Starting from {starting_type}")
        next_idx = idx
        while find_pipe_type(next_idx, parsed_inp) != "S":
            if find_pipe_type(idx, parsed_inp) != ".":
                count += 1
                previous_idx, next_idx = find_next(previous_idx, next_idx)
            else :
                break
        print((count+1)/2)
            

            
    