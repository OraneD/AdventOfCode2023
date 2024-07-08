#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:27:46 2024

@author: orane
"""

def collect_input(inp):
    for line in inp.split("\n"):
        if line.split(":")[0] == "Time" :
            time = int("".join([x for x in line.split(":")[1].split()]))
        elif line.split(":")[0] == "Distance" :
            distance = int("".join([x for x in line.split(":")[1].split()]))
    return time, distance

def brute_force(time, distance):
    win = []
    for speed in range(1, time):
        dist = speed * (time-speed)
        if dist > distance :
            win.append(dist)             
    return len(win)
    

def main():
    with open("input.txt", "r") as file:
        inp = file.read()
    time, distance = collect_input(inp)
    print(brute_force(time,distance))
    
main()
    
