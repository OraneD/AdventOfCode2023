#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:17:26 2024

@author: orane
"""

def collect_input(inp):
    for line in inp.split("\n"):
        if line.split(":")[0] == "Time" :
            time = [int(x) for x in line.split(":")[1].split()]
        elif line.split(":")[0] == "Distance" :
            distance = [int(x) for x in line.split(":")[1].split()]
    return time, distance
            
def compute_time(time, distance):
    total_win = []
    for t, d in zip(time, distance):
        win = []
        for speed in range(1, t):
            dist = speed * (t-speed)
            if dist > d :
                win.append(dist)
        total_win.append(win)               
    return total_win

def compute_win(total_win):
    first = len(total_win[0])
    for lst in total_win[1:] :
        first *= len(lst)
    return first

def main():
    with open("input.txt", "r") as file:
        inp = file.read()
    time, distance = collect_input(inp)
    total_win = compute_time(time, distance)
    result = compute_win(total_win)
    print(result)

main()
    
                
        

    